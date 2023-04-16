from opentrons import protocol_api

metadata = {
    'protocolName': 'Medium Exchange Protocol',
    'author': 'Opentrons Assistant',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 5)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 1)
    trash = protocol.load_labware('agilent_1_reservoir_290ml', 4)

    # Pipettes
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tips])

    # Reagent
    pbs_minus = tuberack.wells_by_name()['A1']
    d_mem = tuberack.wells_by_name()['A2']
    
    # Protocol
    for well_index in well_plate.wells():
        # Remove culture medium
        p300_multi.pick_up_tip()
        p300_multi.transfer(200, well_index, trash['A1'].top(), new_tip='never')

        # Wash with PBS(-)
        p300_multi.transfer(200, pbs_minus, well_index, mix_after=(3, 150), new_tip='never')

        # Remove PBS(-)
        p300_multi.transfer(200, well_index, trash['A1'].top(), new_tip='never')

        # Add D-MEM medium
        p300_multi.transfer(200, d_mem, well_index, mix_after=(1, 150), new_tip='never')
        p300_multi.drop_tip()

