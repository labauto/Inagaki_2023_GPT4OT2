from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Opentrons',
    'apiLevel': '2.0'
}

def prepare_medium(protocol: protocol_api.ProtocolContext, pipette, medium_tube, dest_wells, volume):
    for well in dest_wells:
        pipette.pick_up_tip()
        pipette.aspirate(volume, medium_tube)
        pipette.dispense(volume, well)
        pipette.blow_out()
        pipette.drop_tip()

def add_supplements(protocol: protocol_api.ProtocolContext, pipette, supplement_tubes, dest_wells, volumes):
    for well in dest_wells:
        for tube, volume in zip(supplement_tubes, volumes):
            pipette.pick_up_tip()
            pipette.aspirate(volume, tube)
            pipette.dispense(volume, well)
            pipette.blow_out()
            pipette.drop_tip()

def transfer_cells(protocol: protocol_api.ProtocolContext, pipette, cell_tube, dest_wells, volume):
    for well in dest_wells:
        pipette.pick_up_tip()
        pipette.aspirate(volume, cell_tube)
        pipette.dispense(volume, well)
        pipette.blow_out()
        pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    medium1 = protocol.load_labware('nest_6_tuberack_nest_15ml_conical', 1)
    medium2 = protocol.load_labware('nest_6_tuberack_nest_15ml_conical', 2)
    supplements = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3)
    cells = protocol.load_labware('nest_6_tuberack_nest_15ml_conical', 4)
    plate_os_neg = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    plate_os_pos = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right')
    p300 = protocol.load_instrument('p300_single_gen2', 'left')

    # Reagents
    dmem = medium1.wells_by_name()['A1']
    dmem_high_glucose = medium2.wells_by_name()['A1']
    dex = supplements.wells_by_name()['A1']
    aa = supplements.wells_by_name()['B1']
    bgp = supplements.wells_by_name()['C1']
    hmsc_cells = cells.wells_by_name()['A1']

    # Wells for both OS- and OS+ plates
    os_neg_wells = plate_os_neg.wells()
    os_pos_wells = plate_os_pos.wells()

    # Prepare medium (DMEM) for OS-
    prepare_medium(protocol, p300, dmem, os_neg_wells, 100)

    # Prepare medium (DMEM high glucose) for OS+
    prepare_medium(protocol, p300, dmem_high_glucose, os_pos_wells, 100)

    # Add supplements to OS+ wells
    add_supplements(protocol, p20, [dex, aa, bgp], os_pos_wells, [0.1, 1, 1])

    # Transfer hMSC cells to OS- wells
    transfer_cells(protocol, p300, hmsc_cells, os_neg_wells, 100)

    # Transfer hMSC cells to OS+ wells
    transfer_cells(protocol, p300, hmsc_cells, os_pos_wells, 100)


if __name__ == "__main__":
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.0')
    run(protocol)

