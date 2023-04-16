#Script for running the Opentrons robot

#import robot library
from opentrons import robot

#import labware
from opentrons import labware

#import Pipettes
from opentrons import instruments

#load robot
robot.connect()

#load labware
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
tiprack = labware.load('tiprack-1000ul', '2')
plate = labware.load('corning_6_wellplate_16.8ml_flat', '3')

#load pipette
p1000 = instruments.P1000_Single(mount='right', tip_racks=[tiprack])

#Wash the 6 well plate with PBS(-) by pipetting up and down 5 times
p1000.distribute(1, tuberack['A1'], plate.wells(), air_gap=10,touch_tip=True, disposal_vol = 0)
repeats = 0
while(repeats < 5):
    p1000.aspirate(1000, plate.wells())
    p1000.dispense(1000, plate.wells())
    p1000.blow_out(plate.wells())
    repeats += 1
    
#Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
p1000.distribute(1, tuberack['B1'], plate.wells(),air_gap=10,touch_tip=True, disposal_vol = 0)
robot.delay(minutes=5)

#Add 1 mL of cell culture medium (DMEM) to the 6 well plate
p1000.distribute(1, tuberack['C1'], plate.wells(), air_gap=10,touch_tip=True, disposal_vol = 0)

#Finish the experiment
robot.home()
robot.disconnect()


:*************************


