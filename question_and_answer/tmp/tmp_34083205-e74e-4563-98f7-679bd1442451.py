
#Importing necessary packages
import opentrons
from opentrons import robot, labware, instruments

#Initiate robot
robot.connect()

#Setting up labware
plate = labware.load('96-flat', '1')
tips = labware.load('tiprack-200ul', '4')
tube_rack = labware.load('tube-rack-15_50ml', '7')

#Setting up pipettes
p200 = instruments.Pipette(
    axis='b',
    max_volume=200,
    min_volume=20,
    tip_racks=[tips]
)

#Cleaning robot
p200.set_flow_rate(aspirate=100, dispense=100)
p200.pick_up_tip()
p200.aspirate(200, tube_rack['A1'].bottom(5))
p200.dispense(200, tube_rack['A1'].bottom(5))
p200.drop_tip()

#Seeding cells
p200.pick_up_tip()
p200.aspirate(60, tube_rack['A2'])
p200.dispense(60, plate['A5':'C5'].bottom(2))
p200.drop_tip()

#Adding medium as negative control
p200.pick_up_tip()
for col in plate.columns()[:3]:
    p200.aspirate(60, tube_rack['A3'])
    p200.dispense(60, col.bottom(2))
p200.drop_tip()

#Adding drug dilutions on the second day
#Adding initial stocks
p200.pick_up_tip()
for i, col in enumerate(plate.columns()):
    if i>2:
        break
    p200.aspirate(35, tube_rack['A1'])
    p200.dispense(35, col.bottom(2))
p200.drop_tip()

#Preparing 4X concentrations
p200.pick_up_tip()
for i, col in enumerate(plate.columns()[3:9]):
    if i>5:
        break
    p200.aspirate(100, tube_rack['A{}'.format(i+2)])
    p200.dispense(100, col.bottom(2))
    p200.aspirate(100, tube_rack['A{}'.format(i+2)])
    p200.dispense(100, col.bottom(2))
p200.drop_tip()

#Preparing 2X concentrations
p200.pick_up_tip()
for i, col in enumerate(plate.columns()[3:9]):
    if i>5:
        break
    p200.aspirate(100, tube_rack['C{}'.format(i+1)])
    p200.dispense(100, col.bottom(2))
    p200.aspirate(100, tube_rack['D{}'.format(i+1)])
    p200.dispense(100, col.bottom(2))
p200.drop_tip()

#Adding the drug to the 96 well plate
p200.pick_up_tip()
for i, col in enumerate(plate.columns()[3:9]):
    if i>5:
        break
    p200.aspirate(60, tube_rack['C{}'.format(i+1)])
    p200.dispense(60, col.bottom(2))
    p200.aspirate(60, tube_rack['D{}'.format(i+1)])
    p200.dispense(60, col.bottom(2))
p200.drop_tip()

#Adding CellTox Green reagent
p200.pick_up_tip()
for col in plate.columns():
    p200.aspirate(15, tube_rack['B2'])
    p200.dispense(15, col.bottom(2))
p200.drop_tip()

#Shaking and incubating
robot.run(
    '''
    Set Heater Shaker module to 500rpm for 2 minutes
    Incubate plate at RT for 15 minutes
    ''')

#Reading plate fluorescence
robot.run(
    '''
    Read plate fluorescence at 485nm excitation and 520nm emission using the Biotek microplate reader
    ''')

#Adding Cell Titer Glo 2.0 reagent
p200.pick_up_tip()
for col in plate.columns():
    p200.aspirate(80, tube_rack['B1'])
    p200.dispense(80, col.bottom(2))
p200.drop_tip()

#Shaking and incubating
robot.run(
    '''
    Set Heater Shaker module to 500rpm for 2 minutes
    Incubate plate at RT for 10 minutes
    ''')

#Reading plate luminescence
robot.run(
    '''
    Read plate luminescence using the Biotek microplate reader
    ''')


:*************************


