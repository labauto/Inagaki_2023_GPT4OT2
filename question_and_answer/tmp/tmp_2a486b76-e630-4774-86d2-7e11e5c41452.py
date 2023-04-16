Certainly, here is a Python script for exchanging hMSC cell culture medium using PBS(-) and D-MEM, using an Opentrons robot:

```
# Import necessary libraries for the Opentrons API
from opentrons import labware, instruments, robot

# Define the plate to be used
plate = labware.load('6-well-plate', 'B1')

# Define the pipettes to be used
pipette_1 = instruments.P300_Single(mount='left')
pipette_2 = instruments.P300_Single(mount='right')

# Define the volumes and plate positions for each step of the protocol
media_vol = 250
wash_vol = 500
plate_pos = plate.bottom(2)

# Define the media and wash solutions to be used
media = 'D-MEM' # Replace with desired media
wash = 'PBS(-)' # Replace with desired wash

# Step 1: Remove old media with wash solution
pipette_1.pick_up_tip()
for well in plate.columns()[0]:
    pipette_1.transfer(wash_vol, well.bottom(0.5), pipette_1.trash_container.top()) # Remove old media
pipette_1.drop_tip()

# Step 2: Rinse with wash solution and remove
pipette_2.pick_up_tip()
for well in plate.columns()[0]:
    pipette_2.transfer(wash_vol, pipette_2.trash_container.top(), well.bottom(0.5)) # Rinse with wash
pipette_2.drop_tip()

# Step 3: Add new media
pipette_1.pick_up_tip()
for well in plate.columns()[0]:
    pipette_1.transfer(media_vol, media, well.bottom(0.5)) # Add new media
pipette_1.drop_tip()
```

This script will use a 6-well plate, with the robot's pipettes replacing the old media with wash solution, rinsing the wells with wash solution, and finally adding new media to each well. Note that you will need to replace 'D-MEM' and 'PBS(-)' in the script with the appropriate media and wash solutions for your specific experiment.


:*************************


