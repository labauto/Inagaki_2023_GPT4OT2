import opentrons

# Connect to the robot
robot = opentrons.Robot.get_instance()

# Load the 6-well plate with hMSC cell culture
well_plate = robot.load_labware('6-well-plate', slot=1)

# Load 2 sources of media
pbs_minus = robot.load_labware('trough-12row', slot=2).wells('A1')
d_mem = robot.load_labware('trough-12row', slot=3).wells('A1')

# Create a pipette
pipette = robot.load_instrument('p300_single', mount='left', tip_racks=[])

# Exchange the media
for well in well_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(200, pbs_minus)
    pipette.dispense(200, well)
    pipette.aspirate(200, d_mem)
    pipette.dispense(200, well)
    pipette.drop_tip()

# Disconnect from the robot
robot.disconnect()


:*************************


