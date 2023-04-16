from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Laboratory Experiment',
    'author': 'Your Name',
    'description': 'Automated cell culture trypsinization experiment using Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', 3)

    # Pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    dmem = tuberack.wells_by_name()['A3']

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, pbs)
        for _ in range(5):
            pipette.dispense(1000, well)
            pipette.aspirate(1000, well)
        pipette.dispense(1000, pbs)
        pipette.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish
    for well in plate.wells():
        pipette.transfer(1000, trypsin, well)

    # Pause for 5 minutes (300 seconds)
    protocol.delay(seconds=300)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in plate.wells():
        pipette.transfer(1000, dmem, well)

    # Step 4: Finish the experiment
    protocol.comment("Experiment finished.")
