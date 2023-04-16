from opentrons import robot, containers, instruments

#Define robot
robot.reset()

#Define containers
plate1 = containers.load('6-well-plate', 'A1')
trash = containers.load('point', 'B2', 'trash')
pbs_minus = containers.load('trough-12row', 'A2', 'PBS-minus')
dm_mem = containers.load('trough-12row', 'A3', 'D-MEM')

#Define pipette
pipette = instruments.Pipette(axis='b', max_volume=200,
                              name='pipette',
                              trash_container=trash,
                              tip_racks=[])

#Exchange hMSC cell culture medium
for well in plate1.wells():
    pipette.pick_up_tip()
    pipette.aspirate(200, pbs_minus.wells(0))
    pipette.dispense(200, well)
    pipette.drop_tip()
    pipette.pick_up_tip()
    pipette.aspirate(200, dm_mem.wells(0))
    pipette.dispense(200, well)
    pipette.drop_tip()

robot.home()


:*************************


