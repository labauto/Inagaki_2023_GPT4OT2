from opentrons import robot, containers, instruments

robot.head_speed(x=20000, y=15000, z=10000, a=1000, b=1000)

#Define the containers
plate = containers.load('6-well-plate', 'A1', '6-well-plate')
pbsm = containers.load('trough-12row', 'A2', 'PBS-medium')
dmem = containers.load('trough-12row', 'A3', 'D-MEM')

#Define the pipette
pipette = instruments.P300_Multi(mount='right', tip_racks=['B1','B2'])

#Pick up tip
pipette.pick_up_tip()

#Exchange the cell culture medium
#From PBS-medium to 6-well-plate
for well in plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'):
    pipette.transfer(200, pbsm.wells('A1').bottom(), well.bottom(), air_gap = 10)

#Drop tip
pipette.drop_tip()

#Pick up tip
pipette.pick_up_tip()

#From D-MEM to 6-well-plate
for well in plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'):
    pipette.transfer(200, dmem.wells('A1').bottom(), well.bottom(), air_gap = 10)

#Drop tip
pipette.drop_tip()

robot.home()


:*************************


