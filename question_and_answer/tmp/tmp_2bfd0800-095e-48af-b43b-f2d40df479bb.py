
#Python Script

# Import Opentrons library
from opentrons import robot, containers, instruments

# Connect robot to Opentrons API
robot.connect()

# Set up labware
medium_container = containers.load('trough-12row', 'A2') # container for DMEM
high_glucose_container = containers.load('trough-12row', 'A3') # container for DMEM high glucose
plate96 = containers.load('96-flat', 'B1') # container for 96 well plates

# Set up pipettes
pipette = instruments.P50_Multi(mount='right', tip_racks=[])

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
for well in plate96.wells('A1', length=8, step=12):
    pipette.transfer(100, medium_container.wells('A1'), well, new_tip='always')

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
for well in plate96.wells('B1', length=8, step=12):
    pipette.transfer(100, high_glucose_container.wells('A1'), well, new_tip='always')

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
dex_container = containers.load('tube-rack-2ml', 'B2') # container for Dexamethasone
aa_container = containers.load('tube-rack-2ml', 'B3') # container for Ascorbic acid
bgp_container = containers.load('tube-rack-2ml', 'B4') # container for beta-glycerophosphate

for well in plate96.wells('B1', length=8, step=12):
    pipette.transfer(0.1, dex_container.wells('A1'), well, mix_after=(1, 50), new_tip='always')
    pipette.transfer(1, aa_container.wells('A1'), well, mix_after=(1, 50), new_tip='always')
    pipette.transfer(1, bgp_container.wells('A1'), well, mix_after=(1, 50), new_tip='always')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
cells_container = containers.load('tube-rack-2ml', 'C1') # container for hMSC cells (2,500 cells/100 µl)

for well in plate96.wells('A1', length=8, step=12):
    pipette.transfer(100, cells_container.wells('A1'), well, new_tip='always')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
for well in plate96.wells('B1', length=8, step=12):
    pipette.transfer(100, cells_container.wells('A1'), well, new_tip='always')

# End
robot.disconnect()


:*************************


