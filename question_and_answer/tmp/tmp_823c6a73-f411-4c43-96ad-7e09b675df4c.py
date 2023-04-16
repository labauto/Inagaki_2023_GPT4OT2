
#Initialize Opentrons
from opentrons import labware, instruments, modules

#Define Labware
plate = labware.load('96-flat', '1')
tubes = labware.load('tube-rack-2ml', '2')

#Define Pipettes
pipette = instruments.P300_Single(mount='left', tip_racks=[labware.load('tiprack-200ul', '3')])

#Define Modules
heater_shaker = modules.load('tempdeck', '4')

#Clean the robot with 70% ethanol
pipette.drop_tip()
pipette.aspirate(100, tubes.wells('A1'))
pipette.aspirate(50, plate.wells('A1'))
pipette.dispense(100, plate.wells('A1'))
pipette.dispense(50, tubes.wells('A1'))

#Turn on the HEPA filter
heater_shaker.set_fan_speed(10)

#Seeding A549 cells
#Take a 24–48 hours old T-75 flask of A549 cells
#Take a cell count using the automated Countess 3 machine
#Adjust the cell volume in 10% Ham’s F12K medium 
#Dispense 60 microl of cells in each well
pipette.pick_up_tip()
for well in plate.wells('A1', 'C5'):
    pipette.aspirate(60, tubes.wells('A1'))
    pipette.dispense(60, well)

#Add medium in wells A5-C5 as negative controls
for well in plate.wells('A5', 'C5'):
    pipette.aspirate(60, tubes.wells('A2'))
    pipette.dispense(60, well)

#Add Thapsigargin dilutions
#Transfer 35microL of 1mM Thapsigargin to tubes C1 to C6
pipette.aspirate(35, tubes.wells('A1'))
pipette.dispense(35, tubes.wells('C1', 'C6'))

#Prepare 4X concentrations
#Transfer 100microL of 4X concentration of thapsigargin to tubes C1 to C6
pipette.aspirate(100, tubes.wells('A2', 'A7'))
pipette.dispense(100, tubes.wells('C1', 'C6'))

#Prepare 2X concentrations
#First add 100microL of medium to tubes C1, C3, C5 and D1 to D6
pipette.aspirate(100, tubes.wells('A2'))
pipette.dispense(100, tubes.wells('C1', 'C3', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'))

#Transfer 100microL of 4X concentration of thapsigargin to tubes C1 to C6
pipette.aspirate(100, tubes.wells('A2', 'A7'))
pipette.dispense(100, tubes.wells('C1', 'C6', 'D1', 'D6'))

#Add drug to 96 well plate in triplicate
pipette.aspirate(100, tubes.wells('C1', 'D1'))
pipette.dispense(100, plate.wells('A1', 'F1'))

#Add increasing concentrations of thapsigargin
pipette.aspirate(100, tubes.wells('C2', 'D2'))
pipette.dispense(100, plate.wells('A2', 'F2'))

pipette.aspirate(100, tubes.wells('C3', 'D3'))
pipette.dispense(100, plate.wells('A3', 'F3'))

pipette.aspirate(100, tubes.wells('C4', 'D4'))
pipette.dispense(100, plate.wells('A4', 'F4'))

pipette.drop_tip()

#Cell Viability Assay
#Add CellTox Green reagent
pipette.pick_up_tip()
pipette.aspirate(15, tubes.wells('B2'))
pipette.dispense(15, plate.wells('A1', 'H1', 'A2', 'H2', 'A3', 'H3', 'A4', 'F4', 'A5', 'C5'))

#Shake plate
heater_shaker.engage(speed=500, d=2)

#Incubate at RT for 15 minutes
heater_shaker.deactivate()

#Read fluorescence at 485 nm excitation and 520 nm emission

#Cell Viability Assay
#Add CellTiter Glo 2.0 reagent
pipette.aspirate(80, tubes.wells('B1'))
pipette.dispense(80, plate.wells('A1', 'H1', 'A2', 'H2', 'A3', 'H3', 'A4', 'F4', 'A5', 'C5'))

#Shake plate
heater_shaker.engage(speed=500, d=2)

#Incubate at RT for 10 minutes
heater_shaker.deactivate()

#Read plate for luminescence

#Drop Tip
pipette.drop_tip()


:*************************


