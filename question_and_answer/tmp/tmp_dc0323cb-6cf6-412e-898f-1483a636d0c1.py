from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '7')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '8')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', '3')

    # Pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Protocol steps
    # Step 1: Wash the 6 well plate with PBS(-)
    pbs = tuberack.wells_by_name()['A1']
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, pbs)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add trypsin solution (0.25%)
    trypsin = tuberack.wells_by_name()['A2']
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 3: Wait for 5 minutes
    protocol.delay(minutes=5)

    # Step 4: Add cell culture medium (DMEM)
    dmem = tuberack.wells_by_name()['A3']
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Experiment finished
    protocol.comment("The experiment is successfully completed.")
