from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Assistant',
    'description': 'Protocol for automated laboratory experiment using Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    p1000_tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[p1000_tiprack])

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, tuberack['A1'])
        for _ in range(5):
            p1000.dispense(800, well).aspirate(800, well)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, tuberack['A2'], well, new_tip='never')
        p1000.drop_tip()
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, tuberack['A3'], well, new_tip='never')
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment("Experiment finished.")
