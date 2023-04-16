from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    six_well_plate = protocol.load_labware('corning_6_wellplate_17ml_flat', '3')

    # Pipettes
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    dmem = tuberack.wells_by_name()['A3']

    # Protocol steps
    # Step 1: Wash 6 well plate with PBS(-)
    for well in six_well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, pbs)
        for _ in range(5):
            pipette.dispense(1000, well)
            pipette.aspirate(1000, well)
        pipette.dispense(1000, pbs)    
        pipette.drop_tip()

    # Step 2: Add trypsin solution (0.25%) to the cell culture dish
    for well in six_well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, trypsin)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    protocol.delay(minutes=5)

    # Step 3: Add cell culture medium (DMEM) to the 6 well plate
    for well in six_well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, dmem)
        pipette.dispense(1000, well)
        pipette.drop_tip()
    
    # Step 4: Finish the experiment
    protocol.comment('Experiment Complete')
