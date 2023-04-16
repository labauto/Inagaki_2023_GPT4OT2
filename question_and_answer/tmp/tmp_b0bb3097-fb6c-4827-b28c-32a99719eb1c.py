from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '2')
    tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    reservoir = protocol.load_labware('nest_1_reservoir_195ml', '4')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300ul])

    # Protocol
    lysosome_staining_solution = reservoir.wells_by_name()['A1']
    cell_culture_wells = ['A1', 'A2', 'A3']

    for well_name in cell_culture_wells:
        well = plate_6_well.wells_by_name()[well_name]
        p300.pick_up_tip()
        p300.transfer(1000, lysosome_staining_solution, well, new_tip='never')
        p300.blow_out(well.top())
        p300.return_tip()

    protocol.comment("Protocol is complete.")
