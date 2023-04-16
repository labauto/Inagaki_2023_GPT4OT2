# Import required library
from opentrons import robot, instruments, containers

# Define pipette, pipette tip, and container
pipette = instruments.P50_Single(mount="left", tip_racks=[])
tips = containers.load("tiprack-200ul", 'B1')
plate = containers.load("6-flat", 'A1')

# Fill a reservoir with PBS and D-MEM
pbs_reservoir = containers.load("trough-12row", 'B2')
pbs_reservoir.wells('A1').fill("PBS")
dm_reservoir = containers.load("trough-12row", 'A2')
dm_reservoir.wells('A1').fill("D-MEM")

# Aspirate PBS and D-MEM from their respective reservoirs
pipette.distribute(
    200, pbs_reservoir.wells('A1'), plate.rows('A', 'B', 'C', 'D', 'E', 'F'), new_tip='always')

pipette.distribute(
    200, dm_reservoir.wells('A1'), plate.rows('A', 'B', 'C', 'D', 'E', 'F'), new_tip='always')

# Move the pipette tip to trash
pipette.drop_tip()


:*************************


