from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Assistant',
    'description': 'Automated lab experiment protocol for Opentrons OT-2',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    wellplate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Protocol Steps
    # 1. Wash the 6 well plate with PBS(-) by pipetting up and down 5 times.
    pbs_minus = tuberack.wells_by_name()['A1']
    for well in wellplate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(1_000, pbs_minus)
            pipette.dispense(1_000, well)
        pipette.drop_tip()

    # 2. Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
    trypsin = tuberack.wells_by_name()['A2']
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1_000, trypsin)
        pipette.dispense(1_000, well)
        pipette.drop_tip()
    protocol.delay(minutes=5)

    # 3. Add 1 mL of cell culture medium (DMEM) to the 6 well plate.
    dmem = tuberack.wells_by_name()['A3']
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1_000, dmem)
        pipette.dispense(1_000, well)
        pipette.drop_tip()

    # 4. Finish the experiment.
