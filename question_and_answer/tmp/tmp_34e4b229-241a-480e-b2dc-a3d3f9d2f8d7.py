from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    dmem = tuberack.wells_by_name()['A3']

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-) by pipetting up and down 5 times
    for well in plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, pbs)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait 5 minutes
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
    p1000.drop_tip()
    
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
    p1000.drop_tip()

    # Step 4: Finish the experiment
    # No action required; experiment is finished after the completion of the previous steps
