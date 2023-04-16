from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Automated Labware Experiment',
    'author': 'Your Name',
    'description': 'Automated laboratory experiment using Opentrons machine.',
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Load pipette
    pipette_1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1000])

    # 1. Wash the 6 well plate with PBS(-)
    wells = well_plate.wells()
    pbs_minus = tube_rack.wells_by_name()['A3']
    for well in wells:
        pipette_1000.pick_up_tip()
        pipette_1000.aspirate(1000, pbs_minus)
        for _ in range(5):
            pipette_1000.dispense(800, well)
            pipette_1000.aspirate(800, well)
        pipette_1000.dispense(1000, pbs_minus)
        pipette_1000.drop_tip()

    # 2. Add trypsin solution to the cell culture dish
    trypsin = tube_rack.wells_by_name()['C3']
    for well in wells:
        pipette_1000.pick_up_tip()
        pipette_1000.transfer(1000, trypsin, well, new_tip='never')
        pipette_1000.drop_tip()

    # 3. Wait for 5 minutes
    protocol.delay(minutes=5)

    # 4. Add cell culture medium (DMEM) to the 6 well plate
    dmem = tube_rack.wells_by_name()['D3']
    for well in wells:
        pipette_1000.pick_up_tip()
        pipette_1000.transfer(1000, dmem, well, new_tip='never')
        pipette_1000.drop_tip()

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.10')
    run(protocol)
