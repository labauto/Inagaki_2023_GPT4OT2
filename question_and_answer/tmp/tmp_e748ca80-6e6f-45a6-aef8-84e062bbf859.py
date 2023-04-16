# Opentrons Sample Script

from opentrons import robot, containers, instruments

# Set robot speed
robot.head_speed(x=20, y=20, z=20, a=20, b=20)

# Load labware
tuberack = containers.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
plate = containers.load('corning_6_wellplate_16.8ml_flat', '2')

# Load pipette 
p1000 = instruments.Pipette(
    axis='a',
    max_volume=1000,
    min_volume=100,
    tip_racks=[tuberack['A1']],
    channels=1
)

# Washing the 6 well plate with PBS(-)
for well in plate.wells[:6]:
    p1000.pick_up_tip()
    p1000.aspirate(1000, tuberack['A3'])
    p1000.dispense(1000, well)
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.drop_tip()

# Add 1 ml of trypsin solution (0.25%) to the cell culture dish
for well in plate.wells[:6]:
    p1000.pick_up_tip()
    p1000.aspirate(1000, tuberack['A2'])
    p1000.dispense(1000, well)
    p1000.drop_tip()

# Wait for 5 minutes
robot.pause('Wait 5 minutes')

# Add 1 mL of cell culture medium (DMEM) to the 6 well plate
for well in plate.wells[:6]:
    p1000.pick_up_tip()
    p1000.aspirate(1000, tuberack['A4'])
    p1000.dispense(1000, well)
    p1000.drop_tip()

# Finish the experiment
robot.home()


:*************************


