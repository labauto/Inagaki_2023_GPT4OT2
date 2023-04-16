# Import necessary packages
import opentrons
from opentrons import instruments, containers

# Load robot and labware
robot = opentrons.Robot()
plates = containers.load("6-well", robot.deck)
pipette = instruments.Pipette(axis="a", max_volume=200)

# Exchanging cell culture medium using PBS(-), D-MEM
robot.pause('Please load PBS(-), D-MEM into the labware before continuing.')
for plate_num, plate in enumerate(plates):
    # Dispense PBS(-), D-MEM into correct wells
    pipette.distribute(200, source_container=pbs,
                       dest_container=plate.wells("A1"),
                       blow_out=True)
    pipette.distribute(200, source_container=dmem,
                       dest_container=plate.wells("A2"),
                       blow_out=True)
    # Remove existing cell culture medium
    pipette.pick_up_tip()
    for well in plate.rows("A"):
        pipette.aspirate(200, well)
    pipette.drop_tip()
    # Shake plate to mix
    robot.move_head(plate_num, x=plate.width/2, y=plate.length/2)
    robot.move_head(plate_num, z=2.2)
    robot.move_head(plate_num, z=0.2)

# Finish
print('Done!')


:*************************


