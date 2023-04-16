from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining iPS cells',
    'author': 'Your Name <your_email@example.com>',
    'description': 'Prepare immunostained iPS cells to visualize E-Cadherin',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Stock solutions
    cells = well_plate.wells_by_name()['A1']
    cell_culture_solution = reservoir.wells_by_name()['A1']
    primary_antibody_solution = reservoir.wells_by_name()['A2']
    secondary_antibody_solution = reservoir.wells_by_name()['A3']
    wash_buffer = reservoir.wells_by_name()['A4']

    wells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2']

    # Protocol steps
    for well_name in wells:
        well = well_plate.wells_by_name()[well_name]

        # Aspirate old media and cells
        pipette.pick_up_tip()
        pipette.transfer(2000, well, pipette.waste_container.bottom(), new_tip='never')
        pipette.drop_tip()

        # Wash cells with 500 uL wash buffer twice
        for _ in range(2):
            pipette.pick_up_tip()
            pipette.transfer(500, wash_buffer, well, new_tip='never')
            pipette.transfer(500, well, pipette.waste_container.bottom(), new_tip='never')
            pipette.drop_tip()

        # Add 500 uL of primary antibody solution
        pipette.pick_up_tip()
        pipette.transfer(500, primary_antibody_solution, well, new_tip='never')
        pipette.drop_tip()

    # Incubate with primary antibody for desired time
    protocol.delay(minutes=90) # Adjust incubation time as needed

    for well_name in wells:
        well = well_plate.wells_by_name()[well_name]

        # Aspirate primary antibody solution
        pipette.pick_up_tip()
        pipette.transfer(500, well, pipette.waste_container.bottom(), new_tip='never')
        pipette.drop_tip()

        # Wash cells with 500 uL wash buffer three times
        for _ in range(3):
            pipette.pick_up_tip()
            pipette.transfer(500, wash_buffer, well, new_tip='never')
            pipette.transfer(500, well, pipette.waste_container.bottom(), new_tip='never')
            pipette.drop_tip()

        # Add 500 uL of secondary antibody solution
        pipette.pick_up_tip()
        pipette.transfer(500, secondary_antibody_solution, well, new_tip='never')
        pipette.drop_tip()

    # Incubate with secondary antibody for desired time
    protocol.delay(minutes=60) # Adjust incubation time as needed

    for well_name in wells:
        well = well_plate.wells_by_name()[well_name]

        # Aspirate secondary antibody solution
        pipette.pick_up_tip()
        pipette.transfer(500, well, pipette.waste_container.bottom(), new_tip='never')
        pipette.drop_tip()

        # Wash cells with 500 uL wash buffer three times
        for _ in range(3):
            pipette.pick_up_tip()
            pipette.transfer(500, wash_buffer, well, new_tip='never')
            pipette.transfer(500, well, pipette.waste_container.bottom(), new_tip='never')
            pipette.drop_tip()

    # Add 2000 uL of new cell culture solution to each well
    for well_name in wells:
        well = well_plate.wells_by_name()[well_name]
        pipette.transfer(2000, cell_culture_solution, well)

