from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Opentrons',
    'description': 'Automated cell culture experiment',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 4)
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    PBS = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    DMEM = tuberack.wells_by_name()['A3']

    # Protocol steps
    # Step 1: Wash the 6 well plate with PBS(-)
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, PBS)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 mL trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, DMEM)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
