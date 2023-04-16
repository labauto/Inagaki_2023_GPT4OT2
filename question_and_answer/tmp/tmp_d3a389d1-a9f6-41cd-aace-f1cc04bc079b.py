from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Assistant',
    'description': 'A script for running an experiment using Opentrons machine.',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', 3)

    # Pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagent containers
    pbs_minus = tube_rack['A1']  # PBS(-)
    trypsin_solution = tube_rack['A2']  # Trypsin solution (0.25%)
    cell_culture_medium = tube_rack['A3']  # Cell culture medium (DMEM)

    # Protocol steps

    # Step 1: Wash 6-well plate with PBS(-) by pipetting up and down 5 times.
    # For each well, use 1 ml of PBS(-).
    for well in well_plate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(1000, pbs_minus)
            pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish
    # and wait for 5 minutes.
    for well in well_plate.wells():
        pipette.transfer(1000, trypsin_solution, well)
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6-well plate.
    for well in well_plate.wells():
        pipette.transfer(1000, cell_culture_medium, well)

    # Step 4: Finish the experiment.
    protocol.comment('The experiment is complete.')
