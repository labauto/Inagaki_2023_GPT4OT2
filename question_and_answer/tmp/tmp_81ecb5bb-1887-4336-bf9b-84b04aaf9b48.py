
#Import necessary packages
from opentrons import labware, instruments, robot

#Define the labware
six_well = labware.load('6-well-plate', '1')

#Define the pipette
pipette = instruments.P300_Single(mount='left', tip_racks=[labware.load('tiprack-200ul', '2')])

#First step: Take 1 mL of PBS buffer in a clean 1.5 mL tube
pipette.transfer(1000, six_well.wells('A1'), labware.load('1.5-ml-tube', '3').wells('A1'), new_tip='always')

#Second step: Add 4 µL of FITC-conjugated anti-lysosomal antibody 
pipette.transfer(4, labware.load('1.5-ml-tube', '3').wells('A1'), six_well.wells('A1'), new_tip='always')

#Third step: Incubate for 1 hour at 37°C
robot.pause("Incubate for 1 hour at 37°C")

#Fourth step: Wash with 1 mL PBS buffer 
pipette.transfer(1000, six_well.wells('A1'), labware.load('1.5-ml-tube', '3').wells('A1'), new_tip='always')

#Fifth step: Incubate for 10 minutes at room temperature
robot.pause("Incubate for 10 minutes at room temperature")

#Sixth step: Wash with 1 mL PBS buffer 
pipette.transfer(1000, six_well.wells('A1'), labware.load('1.5-ml-tube', '3').wells('A1'), new_tip='always')

#Seventh step: Add 4 µL of DAPI stain
pipette.transfer(4, labware.load('1.5-ml-tube', '3').wells('A1'), six_well.wells('A1'), new_tip='always')

#Eighth step: Incubate for 10 minutes at room temperature
robot.pause("Incubate for 10 minutes at room temperature")

#Ninth step: Wash with 1 mL PBS buffer 
pipette.transfer(1000, six_well.wells('A1'), labware.load('1.5-ml-tube', '3').wells('A1'), new_tip='always')

#Tenth step: Observe under fluorescent microscope
robot.pause("Observe under fluorescent microscope")


:*************************


