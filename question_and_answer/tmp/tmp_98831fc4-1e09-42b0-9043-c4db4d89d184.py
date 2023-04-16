
#Importing required libraries
import opentrons
from opentrons import labware, instruments, modules


#Initialize the robot & defining labware
robot = opentrons.Robot('OT2')
tiprack = labware.load('opentrons-tiprack-200ul', '7')
mag_deck = modules.load('magdeck', '1')
plate = labware.load('96-flat', '3')
trash = labware.load('point', '4')

#Defining pipettes
pipette200 = instruments.Pipette(axis='a', max_volume=200, 
tip_racks=[tiprack], trash_container=trash)

#Cleaning the inside of the robot with 70 % ethanol
pipette200.drop_tip()
pipette200.pick_up_tip()
pipette200.aspirate(200, labware.load('point', '9'))
pipette200.dispense(200, trash)

#Turning on HEPA filter at low fan speed
pipette200.drop_tip()
robot.toggle_low_fan_speed()

#Seeding A549 cells
#Preparing cell suspension
cells= labware.load('point', '6')
mag_deck.engage(height=1)
pipette200.pick_up_tip()
pipette200.aspirate(60, cells)
pipette200.distribute(60, mag_deck.wells('A1'), [x.top() for x in plate.rows('A')], touch_tip=True)
pipette200.distribute(60, mag_deck.wells('B1'), [x.top() for x in plate.rows('B')], touch_tip=True)
pipette200.distribute(60, mag_deck.wells('C1'), [x.top() for x in plate.rows('C')], touch_tip=True)

#Addition of medium
pipette200.aspirate(80, labware.load('point', '10'))
pipette200.dispense(80, plate.wells('A5'))
pipette200.dispense(80, plate.wells('B5'))
pipette200.dispense(80, plate.wells('C5'))

#Addition of drug
#Preparing drug dilutions
drug_stocks = labware.load('point', '8')

for tube in drug_stocks.rows('A')[0:7]:
    pipette200.pick_up_tip()
    pipette200.aspirate(100, tube)
    pipette200.dispense(100, plate.cols('D')[0])
    pipette200.dispense(100, plate.cols('E')[0])
    pipette200.dispense(100, plate.cols('F')[0])
    
for tube in drug_stocks.rows('C')[0:6]:
    pipette200.pick_up_tip()
    pipette200.aspirate(100, tube)
    pipette200.dispense(100, plate.cols('G')[0])
    pipette200.dispense(100, plate.cols('H')[0])
   
for tube in drug_stocks.rows('D')[0:6]:
    pipette200.pick_up_tip()
    pipette200.aspirate(100, tube)
    pipette200.dispense(100, plate.cols('G')[1])
    pipette200.dispense(100, plate.cols('H')[1])
   
#72 hours incubation
robot.home()
robot.delay(minutes=72)

#Addition of CellTox Green reagent
#Pick up 20microL tip from Slot 10
pipette 200.pick_up_tip()

#Transfer 15microL of CellTox Green reagent
pipette200.aspirate(15, labware.load('point', '11'))
pipette200.dispense(15, plate.wells('A1'))
pipette200.dispense(15, plate.wells('B1'))
pipette200.dispense(15, plate.wells('C1'))
pipette200.dispense(15, plate.wells('D1'))
pipette200.dispense(15, plate.wells('E1'))
pipette200.dispense(15, plate.wells('F1'))
pipette200.dispense(15, plate.wells('G1'))
pipette200.dispense(15, plate.wells('H1'))
pipette200.dispense(15, plate.wells('A2'))
pipette200.dispense(15, plate.wells('B2'))
pipette200.dispense(15, plate.wells('C2'))
pipette200.dispense(15, plate.wells('D2'))
pipette200.dispense(15, plate.wells('E2'))
pipette200.dispense(15, plate.wells('F2'))
pipette200.dispense(15, plate.wells('G2'))
pipette200.dispense(15, plate.wells('H2'))
pipette200.dispense(15, plate.wells('A3'))
pipette200.dispense(15, plate.wells('B3'))
pipette200.dispense(15, plate.wells('C3'))
pipette200.dispense(15, plate.wells('D3'))
pipette200.dispense(15, plate.wells('E3'))
pipette200.dispense(15, plate.wells('F3'))
pipette200.dispense(15, plate.wells('G3'))
pipette200.dispense(15, plate.wells('H3'))
pipette200.dispense(15, plate.wells('A4'))
pipette200.dispense(15, plate.wells('B4'))
pipette200.dispense(15, plate.wells('C4'))
pipette200.dispense(15, plate.wells('D4'))
pipette200.dispense(15, plate.wells('E4'))
pipette200.dispense(15, plate.wells('F4'))
pipette200.dispense(15, plate.wells('A5'))
pipette200.dispense(15, plate.wells('B5'))
pipette200.dispense(15, plate.wells('C5'))

#Orbital shaking
pipette200.drop_tip()
robot.move_to(plate.well('A1'))
robot.run_finite_instructions('A1', [
    ('shake_orbital', {'amplitude': [1, 5], 'duration': [1000, 10000]}),
])

#Incubation at RT
robot.delay(minutes=15)

#Read fluorescence at 485 nm excitation and 520 nm emission
pipette200.drop_tip()
robot.run_finite_instructions('A1', [
    ('read_fluorescence', {'excitation': [485], 'emission': [520]})
])

#Cell viability assay
pipette200.pick_up_tip()
pipette200.aspirate(80, labware.load('point', '12'))
pipette200.dispense(80, plate.wells('A1'))
pipette200.dispense(80, plate.wells('B1'))
pipette200.dispense(80, plate.wells('C1'))
pipette200.dispense(80, plate.wells('D1'))
pipette200.dispense(80, plate.wells('E1'))
pipette200.dispense(80, plate.wells('F1'))
pipette200.dispense(80, plate.wells('G1'))
pipette200.dispense(80, plate.wells('H1'))
pipette200.dispense(80, plate.wells('A2'))
pipette200.dispense(80, plate.wells('B2'))
pipette200.dispense(80, plate.wells('C2'))
pipette200.dispense(80, plate.wells('D2'))
pipette200.dispense(80, plate.wells('E2'))
pipette200.dispense(80, plate.wells('F2'))
pipette200.dispense(80, plate.wells('G2'))
pipette200.dispense(80, plate.wells('H2'))
pipette200.dispense(80, plate.wells('A3'))
pipette200.dispense(80, plate.wells('B3'))
pipette200.dispense(80, plate.wells('C3'))
pipette200.dispense(80, plate.wells('D3'))
pipette200.dispense(80, plate.wells('E3'))
pipette200.dispense(80, plate.wells('F3'))
pipette200.dispense(80, plate.wells('G3'))
pipette200.dispense(80, plate.wells('H3'))
pipette200.dispense(80, plate.wells('A4'))
pipette200.dispense(80, plate.wells('B4'))
pipette200.dispense(80, plate.wells('C4'))
pipette200.dispense(80, plate.wells('D4'))
pipette200.dispense(80, plate.wells('E4'))
pipette200.dispense(80, plate.wells('F4'))



:*************************


