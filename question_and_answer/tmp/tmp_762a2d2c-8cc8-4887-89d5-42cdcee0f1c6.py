 from opentrons import robot, containers, instruments

# Set up the robot
robot.connect()

# Set up the pipette
pipette = instruments.P300_Single(mount='left')

# Set up the containers
tubes = containers.load('tube-rack-2ml', 'A1')
dish = containers.load('96-flat', 'B1')

# Wash the cell culture dish with PBS(-)
for _ in range(5):
    pipette.pick_up_tip()
    pipette.aspirate(2, tubes['A1'])
    pipette.dispense(2, dish)
    pipette.drop_tip()

# Add 3 ml of trypsin solution to the cell culture dish
pipette.pick_up_tip()
pipette.aspirate(3, tubes['A1'])
pipette.dispense(3, dish)
pipette.drop_tip()

# Incubate for 5 minutes
robot.pause(minutes=5)

# Add 10 mL of cell culture medium to the cell culture dish
pipette.pick_up_tip()
pipette.aspirate(10, tubes['A1'])
pipette.dispense(10, dish)
pipette.drop_tip()

# Finish the experiment
robot.disconnect()
