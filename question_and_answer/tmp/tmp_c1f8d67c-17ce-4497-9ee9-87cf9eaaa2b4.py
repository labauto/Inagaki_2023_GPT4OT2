# Imports
import opentrons

# Setting up robot
robot = opentrons.Robot()

# Mounting pipette
pipette = robot.mount_pipette('p300_single', 'right')

# Loading labware
plate = robot.load_labware("96-flat", '4')

# Moving pipette to plate
pipette.pick_up_tip()
pipette.move_to(plate.wells('A1'))

# Exchange hMSC cell culture medium
# Take PBS(-)
pipette.aspirate(200, plate.wells('A2'))
# Dispense into well
pipette.dispense(200, plate.wells('A1'))
# Take D-MEM
pipette.aspirate(200, plate.wells('A3'))
# Dispense into well
pipette.dispense(200, plate.wells('A1'))

# Moving pipette back to start position
pipette.drop_tip()
pipette.move_to(plate.wells('A1'))

# Clean up robot
robot.reset()


:*************************


