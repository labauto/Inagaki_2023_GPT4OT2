# Import necessary packages
from opentrons import robot, labware, instruments

# Define labware
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
wellplate = labware.load('corning_6_wellplate_16.8ml_flat', '2')

# Define pipette
pipette = instruments.P1000_Single(
    mount='left',
    tip_racks=[tuberack['C1']])

# Step 1: Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('A1'),
    mix_after=(5, 1),
    new_tip='always'
)

pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('A2'),
    mix_after=(5, 1),
    new_tip='always'
)

pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('A3'),
    mix_after=(5, 1),
    new_tip='always'
)

pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('B1'),
    mix_after=(5, 1),
    new_tip='always'
)

pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('B2'),
    mix_after=(5, 1),
    new_tip='always'
)

pipette.transfer(1,
    tuberack['A1'],
    wellplate.wells('B3'),
    mix_after=(5, 1),
    new_tip='always'
)

# Step 2: After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
pipette.transfer(1,
    tuberack['B1'],
    wellplate.wells('A1', to='B3'),
    mix_after=(5, 1),
    new_tip='always'
)

# Step 3: Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
pipette.transfer(1,
    tuberack['C1'],
    wellplate.wells('A1', to='B3'),
    new_tip='always'
)

# Step 4: Finish the experiment.
robot.home()


:*************************


