from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Opentrons Automation: Cell Culture Experiment',
    'author': 'Your Name',
    'description': 'Automate washing, trypsinization, and adding cell culture medium'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '5')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    PBS = tube_rack.wells('A1')
    trypsin = tube_rack.wells('A2')
    DMEM = tube_rack.wells('A3')

    # Procedure

    # Step 1: Wash 6-well plate with PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, PBS)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 mL of trypsin solution to cell culture dish and wait for 5 minutes
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, DMEM)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment (no additional actions needed)
