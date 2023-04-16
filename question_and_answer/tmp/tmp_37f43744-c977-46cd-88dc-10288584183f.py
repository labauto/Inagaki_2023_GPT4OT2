 import opentrons

robot = opentrons.Robot()

tiprack = robot.load_labware('opentrons_96_tiprack_300ul')
pipette = robot.load_instrument('p300_multi', 'right', tip_racks=[tiprack])

tube = robot.load_labware('opentrons_15_tuberack_falcon_15ml_conical', slot='1')
cell_plate = robot.load_labware('opentrons_96_aluminumblock_nest_wellplate_100ul', slot='2')

#Add 10 mL of PBS(-)
pipette.transfer(10, tube.wells('A1'), cell_plate.wells('A1'), mix_after=True)

#Wash dish with PBS(-)
for _ in range(5):
    pipette.aspirate(3, cell_plate.wells('A1'))
    pipette.dispense(3, cell_plate.wells('A1'))

#Add 3 mL of trypsin solution
pipette.transfer(3, tube.wells('A2'), cell_plate.wells('A1'), mix_after=True)

#Incubate for 5 min
robot.pause("Incubate for 5 min")

#Add 10 mL of cell culture medium
pipette.transfer(10, tube.wells('A3'), cell_plate.wells('A1'), mix_after=True)

#Incubate for 5 min
robot.pause("Incubate for 5 min")

#Finish experiment
robot.comment("Finish experiment")
