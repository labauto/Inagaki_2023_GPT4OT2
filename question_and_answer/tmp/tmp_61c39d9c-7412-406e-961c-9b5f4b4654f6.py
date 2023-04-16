Certainly! Here's an example of a Python script that runs on an Opentrons machine and performs the experiment you described:

```
from opentrons import labware, instruments, robot

# Set up the labware
plate_6_well = labware.load('corning_6_wellplate_16.8ml_flat', 'B1')
trough = labware.load('trough-12row', 'A1')
tiprack_50ul = labware.load('tiprack-200ul', 'B2')
tiprack_300ul = labware.load('tiprack-200ul', 'B3')

# Set up the instruments
p50 = instruments.P50_Single(
    mount='left',
    tip_racks=[tiprack_50ul]
)
p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_300ul]
)

# Define the volumes and locations for the reagents
media_volume = 50  # uL
pbs_volume = 100  # uL
scm130_volume = 100  # uL
media_location = trough.wells('A1')
pbs_location = trough.wells('A2')
scm130_location = trough.wells('A3')

# Perform the experiment
robot.comment('Starting experiment')
for well in plate_6_well.wells():
    # Remove the old media
    robot.comment(f'Removing media from well {well}')
    p300.transfer(media_volume, well.bottom(2), p300.trash_container.top())

    # Rinse with PBS(-)
    robot.comment(f'Rinsing well {well} with PBS(-)')
    p300.transfer(pbs_volume, pbs_location, well.bottom(2))
    p300.transfer(pbs_volume, well.bottom(2), p300.trash_container.top())

    # Add new media
    robot.comment(f'Adding new media to well {well}')
    p50.pick_up_tip()
    p50.transfer(media_volume, media_location, well, new_tip='never')
    p50.drop_tip()

    # Add SCM130
    robot.comment(f'Adding SCM130 to well {well}')
    p300.transfer(scm130_volume, scm130_location, well.bottom(2))

robot.comment('Experiment complete')
```

This script uses Opentrons' Python API to control the robot's pipettes and labware. It sets up the labware, defines the volumes and locations for the reagents, and performs the experiment for each well in the 6-well plate.

In the experiment, the robot performs the following steps for each well:

1. Remove the old media
2. Rinse the well with PBS(-)
3. Add new media
4. Add SCM130

Let me know if you have any questions about the script or how to run it on your Opentrons machine!


:*************************


