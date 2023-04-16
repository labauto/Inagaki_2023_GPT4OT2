# Import the Opentrons API
import opentrons

# Create a connection to the Opentrons machine
robot = opentrons.robot

# Define the pipette and tip racks
pipette = robot.load_instrument('p10_single_v1.5', mount='right')
tip_racks = [robot.load_labware('opentrons_96_tiprack_10ul', slot) for slot in ['2', '5']]

# Define the labware for the cell culture plate and immunostaining reagents
cell_plate = robot.load_labware('corning_6_wellplate_16.2ml_flat', '1')
immunostaining_plate = robot.load_labware('nunc_96_wellplate_92.4ul', '4')

# Define the locations of the reagents in the immunostaining plate
primary_antibody = immunostaining_plate['A1']
lysosome_antibody = immunostaining_plate['A2']
secondary_antibody = immunostaining_plate['A3']
mounting_medium = immunostaining_plate['A4']

# Define the locations of the cells in the cell culture plate
cell_locations = [(well, 1) for well in cell_plate.rows('A')]

# Add primary antibody to cells and incubate
pipette.pick_up_tip(tip_racks[0].well('A1'))
for cell_location in cell_locations:
    pipette.aspirate(3, primary_antibody)
    pipette.dispense(3, cell_location[0])
pipette.drop_tip()

robot.pause('Incubate cells with primary antibody')

# Wash cells with PBS buffer
pipette.pick_up_tip(tip_racks[0].well('A2'))
for cell_location in cell_locations:
    pipette.aspirate(10, cell_location[0])
    pipette.dispense(20, cell_location[0])
    pipette.aspirate(20, cell_location[0])
    pipette.dispense(30, cell_location[0])
pipette.drop_tip()

robot.pause('Wash cells with PBS buffer')

# Add lysosome antibody to cells and incubate
pipette.pick_up_tip(tip_racks[0].well('A3'))
for cell_location in cell_locations:
    pipette.aspirate(3, lysosome_antibody)
    pipette.dispense(3, cell_location[0])
pipette.drop_tip()

robot.pause('Incubate cells with lysosome antibody')

# Wash cells with PBS buffer
pipette.pick_up_tip(tip_racks[0].well('A4'))
for cell_location in cell_locations:
    pipette.aspirate(10, cell_location[0])
    pipette.dispense(20, cell_location[0])
    pipette.aspirate(20, cell_location[0])
    pipette.dispense(30, cell_location[0])
pipette.drop_tip()

robot.pause('Wash cells with PBS buffer')

# Add secondary antibody to cells and incubate
pipette.pick_up_tip(tip_racks[1].well('A1'))
for cell_location in cell_locations:
    pipette.aspirate(3, secondary_antibody)
    pipette.dispense(3, cell_location[0])
pipette.drop_tip()

robot.pause('Incubate cells with secondary antibody')

# Wash cells with PBS buffer
pipette.pick_up_tip(tip_racks[1].well('A2'))
for cell_location in cell_locations:
    pipette.aspirate(10, cell_location[0])
    pipette.dispense(20, cell_location[0])
    pipette.aspirate(20, cell_location[0])
    pipette.dispense(30, cell_location[0])
pipette.drop_tip()

robot.pause('Wash cells with PBS buffer')

# Add mounting medium to cells
pipette.pick_up_tip(tip_racks[1].well('A3'))
for cell_location in cell_locations:
    pipette.aspirate(8, mounting_medium)
    pipette.dispense(8, cell_location[0])
pipette.drop_tip()
