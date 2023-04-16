import os
from opentrons import robot, instruments, containers

# Declare the robot
robot = robot.Robot()

# Declare the pipettes
pipette_left = instruments.Pipette(
    axis="a",
    max_volume=20,
    min_volume=0.5,
    channels=1,
)

# Declare the containers
plate = containers.load("6-well-plate", "1")
 PBS_container = containers.load("tube-rack", "2")
 DMEM_container = containers.load("tube-rack", "3")

# Begin the experiment

# Add PBS (-) to each well
robot.pick_up_tip()
for well in plate.wells():
    pipette_left.aspirate(2, PBS_container.wells("A1"))
    pipette_left.dispense(2, well)
    pipette_left.drop_tip()

# Exchange the medium with D-MEM
robot.pick_up_tip()
for well in plate.wells():
    pipette_left.aspirate(2, DMEM_container.wells("A1"))
    pipette_left.dispense(2, well)
    pipette_left.drop_tip()

# End the experiment
robot.home()


:*************************


