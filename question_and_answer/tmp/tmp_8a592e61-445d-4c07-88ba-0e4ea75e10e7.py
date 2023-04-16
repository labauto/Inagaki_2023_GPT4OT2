
# Import libraries
import opentrons

# Initialize robot
robot = opentrons.Robot()

# Call liquid handler
pipette = robot.load_instrument('p300_multi', 'left')

# Create 6 well plate
plate = robot.load_labware("6-well-plate", '1')

# Pick up pipette tip
pipette.pick_up_tip()

# Transfer 1.5 ml of media from tube to well A1
pipette.aspirate(1.5, 'tube')
pipette.dispense(1.5, plate.wells('A1'))

# Wait for media to settle
robot.pause()

# Transfer 0.3 ml of dithizone solution to well A2
pipette.aspirate(0.3, 'dithizone_solution')
pipette.dispense(0.3, plate.wells('A2'))

# Wait for solution to settle
robot.pause()

# Add 0.5 ml of hMSC cells to well A2
pipette.aspirate(0.5, 'hMSC_cells')
pipette.dispense(0.5, plate.wells('A2'))

# Wait for cells to settle
robot.pause()

# Incubate cells for 1 hour
robot.delay(minutes=60)

# Transfer 0.5 ml of media from well A2 to well B1
pipette.aspirate(0.5, plate.wells('A2'))
pipette.dispense(0.5, plate.wells('B1'))

# Wait for media to settle
robot.pause()

# Incubate cells for 1 hour
robot.delay(minutes=60)

# Transfer 0.5 ml of cells from well B1 to well C1
pipette.aspirate(0.5, plate.wells('B1'))
pipette.dispense(0.5, plate.wells('C1'))

# Wait for cells to settle
robot.pause()

# Place 6 well plate in imaging chamber
imagining_chamber = robot.load_labware("imaging_chamber", '2')

# Move plate to imaging chamber
robot.move_labware(plate, '2', 'imaging_chamber')

# Run imaging process
robot.run_imaging_process()

# Transfer 0.2 ml of media from tube to well D1
pipette.aspirate(0.2, 'tube')
pipette.dispense(0.2, plate.wells('D1'))

# Wait for media to settle
robot.pause()

# Transfer 0.3 ml of HRP solution to well D2
pipette.aspirate(0.3, 'HRP_solution')
pipette.dispense(0.3, plate.wells('D2'))

# Wait for solution to settle
robot.pause()

# Add 0.5 ml of hMSC cells to well D2
pipette.aspirate(0.5, 'hMSC_cells')
pipette.dispense(0.5, plate.wells('D2'))

# Wait for cells to settle
robot.pause()

# Incubate cells for 1 hour
robot.delay(minutes=60)

# Place 6 well plate in imaging chamber
imagining_chamber = robot.load_labware("imaging_chamber", '2')

# Move plate to imaging chamber
robot.move_labware(plate, '2', 'imaging_chamber')

# Run imaging process
robot.run_imaging_process()

# Eject tip
pipette.drop_tip()


:*************************


