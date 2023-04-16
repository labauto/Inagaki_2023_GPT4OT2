
# Import Opentrons library
from opentrons import robot

# Setup robot and enable commands
robot.connect()
robot.home()

# Load and mount tiprack
tiprack1 = robot.load_labware('opentrons_96_filtertiprack_200ul', 3)
robot.mount_labware('opentrons_96_filtertiprack_200ul', 3, 'tiprack1')

# Load 6-well plate
plate_6well = robot.load_labware('nest_6_wellplate_3ml_deepwell', 1)

# Load 96-well plate
plate_96well = robot.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 2)

# Create 6-well to 96-well pipette
pipette6_96 = robot.new_pipette(
    axis='a',
    nozzle_type='p10_multi',
    min_volume=20,
    max_volume=200,
    name='pipette6_96',
    tip_racks=[tiprack1]
)

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
for i in range(8):
    for j in range(12):
        source_well = plate_6well.wells(i, j)
        dest_wells = plate_96well.wells(i*12+j, length=1)
        pipette6_96.transfer(100, source_well, dest_wells, 'DMEM')

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
for i in range(8):
    for j in range(12):
        source_well = plate_6well.wells(i+8, j)
        dest_wells = plate_96well.wells(i*12+j, length=1)
        pipette6_96.transfer(100, source_well, dest_wells, 'DMEM High Glucose')

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
for i in range(8):
    for j in range(12):
        dest_wells = plate_96well.wells(i*12+j, length=1)
        pipette6_96.distribute(0.1, plate_6well.wells(i+8,j,'Dexamethasone'), dest_wells)
        pipette6_96.distribute(1, plate_6well.wells(i+8,j,'Ascorbic Acid'), dest_wells)
        pipette6_96.distribute(1, plate_6well.wells(i+8,j,'beta-Glycerophosphate'), dest_wells)


# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
for i in range(8):
    for j in range(12):
        source_well = plate_6well.wells(i, j)
        dest_wells = plate_96well.wells(i*12+j, length=1)
        pipette6_96.transfer(100, source_well, dest_wells, 'hMSC cells')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
for i in range(8):
    for j in range(12):
        source_well = plate_6well.wells(i+8, j)
        dest_wells = plate_96well.wells(i*12+j, length=1)
        pipette6_96.transfer(100, source_well, dest_wells, 'hMSC cells')

robot.home()

# End
print("Experiment finished successfully")


:*************************


