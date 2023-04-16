Script: 

# Import opentrons and labware
from opentrons import robot, labware, instruments

# Load labware
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
plate = labware.load('corning_6_wellplate_16.8ml_flat', '2')

# Load pipette
p1000 = instruments.P1000_Single(mount='left', tip_racks=[tuberack['A1']])

# Wash the plate
for well in plate.wells():
    p1000.transfer(1000, tuberack['A2'].bottom(), well.bottom(), air_gap=20, 
    new_tip='always')
    p1000.aspirate(1000, well.bottom())
    for _ in range(5):
        p1000.dispense(1000, well.bottom())
        p1000.aspirate(1000, well.bottom())

# Add trypsin solution
for well in plate.wells():
    p1000.transfer(1000, tuberack['A3'].bottom(), well.bottom(), air_gap=20, 
    new_tip='always')
    
# Add cell culture medium
for well in plate.wells():
    p1000.transfer(1000, tuberack['A4'].bottom(), well.bottom(), air_gap=20, 
    new_tip='always')

# Finish
robot.home()


:*************************


