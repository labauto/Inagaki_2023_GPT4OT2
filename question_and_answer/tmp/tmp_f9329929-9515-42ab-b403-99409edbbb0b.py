from opentrons import protocol_api

metadata = {
    'protocolName': 'E-Cadherin Immunostaining on iPS Cells',
    'author': 'Your Name',
    'description': 'E-Cadherin immunostaining on iPS cells in a 6 well plate',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # Pipettes
    pipette_300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])

    # Stock solutions
    solution_1 = reservoir.wells_by_name()['A1']
    solution_2 = reservoir.wells_by_name()['A2']
    wash_buffer = reservoir.wells_by_name()['A3']

    # Staining process
    for well in well_plate.wells():
        # Add solution_1 (primary antibody)
        pipette_300.pick_up_tip()
        pipette_300.aspirate(100, solution_1)
        pipette_300.dispense(100, well)
        pipette_300.drop_tip()

        # Wash
        pipette_300.pick_up_tip()
        for _ in range(3):
            pipette_300.aspirate(300, wash_buffer)
            pipette_300.dispense(300, well)
        pipette_300.drop_tip()

        # Add solution_2 (secondary antibody)
        pipette_300.pick_up_tip()
        pipette_300.aspirate(100, solution_2)
        pipette_300.dispense(100, well)
        pipette_300.drop_tip()

        # Wash
        pipette_300.pick_up_tip()
        for _ in range(3):
            pipette_300.aspirate(300, wash_buffer)
            pipette_300.dispense(300, well)
        pipette_300.drop_tip()

    # Finalize by removing any remaining buffer
    for well in well_plate.wells():
        pipette_300.pick_up_tip()
        pipette_300.aspirate(300, well)
        pipette_300.dispense(300, reservoir.wells_by_name()['A12'])
        pipette_300.drop_tip()

    protocol.comment("The immunostaining process is complete.")
