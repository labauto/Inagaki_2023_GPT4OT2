from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Automated Lab Experiment',
    'author': 'Your Name',
    'description': 'Automated lab experiment using Opentrons'
}

def run(protocol: protocol_api.ProtocolContext):

    # Load Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    wellplate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Load Pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagent Locations
    pbs_minus = tuberack.wells_by_name()['A1']
    trypsin_solution = tuberack.wells_by_name()['A2']
    cell_culture_medium = tuberack.wells_by_name()['A3']

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-) by pipetting up and down 5 times
    for well in wellplate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(1000, pbs_minus)
            pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, trypsin_solution)
        pipette.dispense(1000, well)
        pipette.drop_tip()
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, cell_culture_medium)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment('Experiment finished successfully!')
