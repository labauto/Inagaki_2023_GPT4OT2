from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    trough = protocol.load_labware('usascientific_12_reservoir_22ml', '3')
    
    # Pipettes
    p300_single = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])
    
    # Reagents
    pbs = trough['A1']
    dmem = trough['A2']

    # Perform operation on each well
    for well in six_well_plate.wells():
        # Aspirate old medium and discard
        p300_single.pick_up_tip()
        p300_single.aspirate(1000, well)
        p300_single.dispense(1000, pbs)
        p300_single.drop_tip()

        # Wash with PBS(-)
        p300_single.pick_up_tip()
        p300_single.transfer(1000, pbs, well, new_tip='never')
        p300_single.mix(3, 1000, well)
        p300_single.aspirate(1000, well)  # Remove PBS(-)
        p300_single.dispense(1000, pbs)
        p300_single.drop_tip()

        # Add fresh D-MEM
        p300_single.pick_up_tip()
        p300_single.transfer(1000, dmem, well, new_tip='never')
        p300_single.mix(3, 1000, well)
        p300_single.drop_tip()
