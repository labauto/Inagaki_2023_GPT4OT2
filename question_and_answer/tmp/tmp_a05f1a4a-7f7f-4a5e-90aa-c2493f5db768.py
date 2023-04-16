from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reagent_reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_1])

    # Reagents
    pbs_minus = reagent_reservoir.wells_by_name()['A1']
    d_mem = reagent_reservoir.wells_by_name()['A2']

    # Protocol
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        
        # Remove old cell culture medium
        p300.transfer(2000, well, p300.waste_container.top(), new_tip='never')

        # Wash with PBS(-) solution
        p300.transfer(1000, pbs_minus, well, mix_after=(3, 1000), new_tip='never')

        # Remove PBS(-) solution
        p300.transfer(1000, well, p300.waste_container.top(), new_tip='never')

        # Add fresh D-MEM medium
        p300.transfer(2000, d_mem, well, new_tip='never')
        
        p300.drop_tip()
