
#Code
#Import libraries
import opentrons

#Set up robot and pipettes
robot = opentrons.Robot(controllers=dict(gantry=dict(port="/dev/ttyACM0")))
robot.home()

pipette_left = robot.get_pipette('left')
pipette_right = robot.get_pipette('right')

#Define variables
os_minus_plate = robot.labware.load('96-flat', '1')
os_plus_plate = robot.labware.load('96-flat', '2')
dm_well = robot.labware.load('trough-12row', '3', 'DMEM')
dm_high_glucose_well = robot.labware.load('trough-12row', '4', 'DMEM High Glucose')
hmsc_well = robot.labware.load('trough-12row', '5', 'hMSC Cells')

#Transfer medium to each well of 96 well plate (OS-)
pipette_left.pick_up_tip()
for x in os_minus_plate.rows():
    for y in x:
        pipette_left.aspirate(100, dm_well.wells('A1'))
        pipette_left.dispense(100, y)
pipette_left.drop_tip()

#Transfer medium to each well of 96 well plate (OS+)
pipette_left.pick_up_tip()
for x in os_plus_plate.rows():
    for y in x:
        pipette_left.aspirate(100, dm_high_glucose_well.wells('A1'))
        pipette_left.dispense(100, y)
pipette_left.drop_tip()

#Add Dexamethasone, Ascorbic acid, and beta-glycerophosphate to each well of 96 well plate (OS+)
pipette_right.pick_up_tip()
for x in os_plus_plate.rows():
    for y in x:
        pipette_right.aspirate(0.1, dm_well.wells('A2'))
        pipette_right.dispense(0.1, y)
        pipette_right.aspirate(1, dm_well.wells('A3'))
        pipette_right.dispense(1, y)
        pipette_right.aspirate(1, dm_well.wells('A4'))
        pipette_right.dispense(1, y)
pipette_right.drop_tip()

#Transfer hMSC cells to each well of 96 well plate (OS-)
pipette_left.pick_up_tip()
for x in os_minus_plate.rows():
    for y in x:
        pipette_left.aspirate(100, hmsc_well.wells('A1'))
        pipette_left.dispense(100, y)
pipette_left.drop_tip()

#Transfer hMSC cells to each well of 96 well plate (OS+)
pipette_left.pick_up_tip()
for x in os_plus_plate.rows():
    for y in x:
        pipette_left.aspirate(100, hmsc_well.wells('A1'))
        pipette_left.dispense(100, y)
pipette_left.drop_tip()

#End
robot.home()


:*************************


