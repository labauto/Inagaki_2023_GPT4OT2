Sure, here's a sample Python script that uses Opentrons machine to exchange hMSC cell culture medium using PBS(-) and D-MEM.

Please note that this script is only meant to be a guide and should be adjusted to fit your specific experiment. Additionally, make sure to follow proper safety and sterilization protocols when handling biological samples and equipment.

```
# Import the necessary libraries
from opentrons import labware, instruments, robot

# Define the labware configuration
plate_name = 'corning_6_wellplate_16.8ml_flat'
if plate_name not in labware.list():
    labware.create(
        plate_name,
        grid=(2, 3),
        spacing=(19.15, 19.15),
        diameter=16.8,
        depth=19.85,
        volume=16800
    )
plate = labware.load(plate_name, '1')

# Define the instrument configuration
pipette_name = 'p10_multi'
if pipette_name not in instruments.list():
    instruments.create(
        pipette_name,
        axis='a',
        channels=8,
        name='Opentrons P10 Multi-Channel Pipette',
        min_volume=0.5,
        max_volume=10,
        tip_racks=[labware.load('opentrons_96_tiprack_10ul', '2')]
    )
pipette = instruments.P10_Multi(mount='left')

# Define the volumes needed for the experiment
pbs_vol = 200  # µL
dmem_vol = 100  # µL

# Define the well order for the protocol
well_order = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2']

# Exchange media in each well
for well in well_order:
    # Move pipette to well to aspirate media
    pipette.pick_up_tip()
    pipette.mix(5, 10, plate[well])
    pipette.aspirate(pbs_vol, plate[well])
    pipette.mix(1, 10, plate[well])  # Mix and aspirate PBS
    pipette.aspirate(dmem_vol, plate[well])  # Add DMEM
    pipette.dispense(dmem_vol + pbs_vol, plate[well])  # Dispense DMEM and PBS
    pipette.mix(5, 10, plate[well])  # Mix solution
    pipette.drop_tip()

# Pause the robot for operator to remove plate
robot.pause()  
```

This script assumes that your robot is connected to your computer and the necessary Opentrons API is properly installed. It also assumes that you have calibrated the robot and have the necessary labware and pipette configured. 

Before running the script, make sure to double-check the volumes and well order to ensure it matches your specific experiment.


:*************************


