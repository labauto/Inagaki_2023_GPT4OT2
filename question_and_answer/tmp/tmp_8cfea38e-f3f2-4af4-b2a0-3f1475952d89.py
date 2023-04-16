
# Python Script
from opentrons import robot, containers, instruments

# Connect to the robot
robot.connect()

# Set up the labware
plate_6well = containers.load('6-flat', '1', '6-flat plate')
plate_96well = containers.load('96-flat', '2', '96-flat plate')

# Set up the pipette
pipette = instruments.P300_Single(
    axis='b',
    max_volume=300,
)

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
for well in plate_96well.wells_by_name()['A1':'H12']:
    pipette.transfer(
        100,
        plate_6well.wells_by_name()['A1'],
        well,
    )

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
for well in plate_96well.wells_by_name()['A1':'H12']:
    pipette.transfer(
        100,
        plate_6well.wells_by_name()['A2'],
        well,
    )

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 
# 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
dex_vol = 0.1
aa_vol = 1
bgp_vol = 1
for well in plate_96well.wells_by_name()['A1':'H12']:
    pipette.transfer(
        dex_vol,
        plate_6well.wells_by_name()['A3'],
        well,
    )
    pipette.transfer(
        aa_vol,
        plate_6well.wells_by_name()['A4'],
        well,
    )
    pipette.transfer(
        bgp_vol,
        plate_6well.wells_by_name()['A5'],
        well,
    )

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
for well in plate_96well.wells_by_name()['A1':'H12']:
    pipette.transfer(
        100,
        plate_6well.wells_by_name()['A6'],
        well,
    )

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
for well in plate_96well.wells_by_name()['A1':'H12']:
    pipette.transfer(
        100,
        plate_6well.wells_by_name()['A7'],
        well,
    )

# Disconnect the robot
robot.disconnect()


:*************************


