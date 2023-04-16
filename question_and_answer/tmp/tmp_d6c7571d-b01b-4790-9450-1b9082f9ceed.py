
from opentrons import robot, labware, instruments

robot.reset()

# Declare the labware
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
plate = labware.load('corning_6_wellplate_16.8ml_flat', '2')

# Declare the pipette
p1000 = instruments.P1000_Single(mount='right', tip_racks=[tuberack['A1']])

# Wash the 6 well plate with PBS(-)
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, tuberack['A1'].wells('PBS(-)'))
    p1000.dispense(1000, well)
    for i in range(5):
        p1000.aspirate(1000, well)
        p1000.dispense(1000, well)
    p1000.drop_tip()

# Add 1 ml of trypsin solution
p1000.pick_up_tip()
p1000.aspirate(1000, tuberack['A1'].wells('Trypsin Solution'))
for well in plate.wells():
    p1000.dispense(1000, well)
p1000.drop_tip()

# Wait 5 minutes
robot.pause(minutes=5)

# Add 1 mL of cell culture medium
p1000.pick_up_tip()
p1000.aspirate(1000, tuberack['A1'].wells('Cell Culture Medium'))
for well in plate.wells():
    p1000.dispense(1000, well)
p1000.drop_tip()

# Finish the experiment
robot.home()


:*************************


