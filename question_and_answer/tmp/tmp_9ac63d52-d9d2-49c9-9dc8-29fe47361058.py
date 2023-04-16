 from opentrons import robot, containers, instruments

# Set up the robot
robot.connect()

# Set up the containers
trough = containers.load('trough-12row', 'A1')
dish = containers.load('96-flat', 'B1')

# Set up the pipette
pipette = instruments.Pipette(
    axis='a',
    max_volume=2,
    min_volume=0.5,
    tip_racks=[trough.rows('A1')]
)

# Wash the cell culture dish with PBS(-)
for _ in range(5):
    pipette.transfer(2, trough.wells('A1'), dish.wells('A1'), mix_after=(2, 10))

# Add 3 ml of trypsin solution to the cell culture dish
pipette.transfer(3, trough.wells('A2'), dish.wells('A1'), mix_after=(2, 10))

# Incubate for 5 minutes
robot.pause('Incubate for 5 minutes')

# Add 10 mL of cell culture medium to the cell culture dish
pipette.transfer(10, trough.wells('A3'), dish.wells('A1'), mix_after=(2, 10))

# Finish the experiment
robot.home()
