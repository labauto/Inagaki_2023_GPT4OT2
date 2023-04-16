from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Laboratory Experiment',
    'author': 'Your Name',
    'description': 'Automated cell culture experiment using Opentrons robot.',
    'apiLevel': '2.10'  # Specify your desired API level here
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware and modules
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    dmem = tuberack.wells_by_name()['A3']

    # Protocol Steps
    # Step 1: Wash 6 well plate with PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, pbs_minus)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml trypsin solution (0.25%)
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    protocol.delay(minutes=5)  # Wait for 5 minutes

    # Step 3: Add 1 mL of DMEM
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment('Experiment is finished.')
