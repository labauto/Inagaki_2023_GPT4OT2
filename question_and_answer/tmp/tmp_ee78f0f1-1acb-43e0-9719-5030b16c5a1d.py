#importing modules
from opentrons import robot, containers, instruments

#creating robot
r = robot.Robot()

#creating containers for hMSC cells, PBS(-) and D-MEM
container_hMSC = containers.load('6-well-plate', 'A1', 'hMSC')
container_PBS = containers.load('trough-12row', 'B1', 'PBS')
container_D_MEM = containers.load('trough-12row', 'C1', 'D-MEM')

#creating pipettes
pipette_left = instruments.Pipette(axis='a')
pipette_right = instruments.Pipette(axis='b')

#exchanging cell culture medium
pipette_left.pick_up_tip()
pipette_left.aspirate(200, container_hMSC['A1'])
pipette_left.dispense(200, container_PBS['A1'])
pipette_left.drop_tip()

pipette_right.pick_up_tip()
pipette_right.aspirate(200, container_PBS['B1'])
pipette_right.dispense(200, container_hMSC['A1'])
pipette_right.drop_tip()

pipette_left.pick_up_tip()
pipette_left.aspirate(200, container_hMSC['A1'])
pipette_left.dispense(200, container_D_MEM['A1'])
pipette_left.drop_tip()

pipette_right.pick_up_tip()
pipette_right.aspirate(200, container_D_MEM['B1'])
pipette_right.dispense(200, container_hMSC['A1'])
pipette_right.drop_tip()


:*************************


