
# Import necessary libraries
import opentrons
from opentrons import labware, instruments

# Specify deck
tiprack_200 = labware.load('tiprack-200ul', '10')
plate_96well = labware.load('96-flat', '11')

# Specify pipettes
pipette_200 = instruments.Pipette(
    axis='b',
    max_volume=200,
    min_volume=0,
    tip_racks=[tiprack_200])

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
pipette_200.distribute(
    100,
    'DMEM',
    plate_96well.wells('A1', length=8, step=1),
    new_tip='once')

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
pipette_200.distribute(
    100,
    'DMEM high glucose',
    plate_96well.wells('B1', length=8, step=1),
    new_tip='once')

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
pipette_200.distribute(
    0.1,
    'Dexamethasone',
    plate_96well.wells('B1', length=8, step=1),
    new_tip='once')

pipette_200.distribute(
    1,
    'Ascorbic acid',
    plate_96well.wells('B1', length=8, step=1),
    new_tip='once')

pipette_200.distribute(
    1,
    'beta-glycerophosphate',
    plate_96well.wells('B1', length=8, step=1),
    new_tip='once')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
pipette_200.distribute(
    100,
    'hMSC Cells',
    plate_96well.wells('A1', length=8, step=1),
    new_tip='once')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
pipette_200.distribute(
    100,
    'hMSC Cells',
    plate_96well.wells('B1', length=8, step=1),
    new_tip='once')

# End
pipette_200.drop_tip()


:*************************


