import opentrons

#connect to robot
robot =opentrons.robot.Robot()

#set pipette and tiprack
left_pipette = robot.load_instrument('p300_multi', 'left')
tiprack_300 = robot.load_labware('opentrons_96_tiprack_300ul', '8')

#set source and destination
source_well = robot.load_labware('usascientific_6_wellplate_2.4ml_deep', '1')
destination_well = robot.load_labware('usascientific_6_wellplate_2.4ml_deep', '2')

#exchange medium
for row in source_well.rows():
	for col in source_well.cols():
		left_pipette.pick_up_tip(tiprack_300.wells(row, col))
		left_pipette.aspirate(300, source_well.wells(row, col))
		left_pipette.dispense(300, destination_well.wells(row, col))
		left_pipette.drop_tip()

#replace medium with PBS(-)
for row in destination_well.rows():
	for col in destination_well.cols():
		left_pipette.pick_up_tip(tiprack_300.wells(row, col))
		left_pipette.aspirate(300, source_well.wells(row, col))
		left_pipette.dispense(300, destination_well.wells(row, col))
		left_pipette.drop_tip()

#replace medium with D-MEM
for row in destination_well.rows():
	for col in destination_well.cols():
		left_pipette.pick_up_tip(tiprack_300.wells(row, col))
		left_pipette.aspirate(300, source_well.wells(row, col))
		left_pipette.dispense(300, destination_well.wells(row, col))
		left_pipette.drop_tip()


:*************************


