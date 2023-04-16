
# Import necessary packages
import opentrons
from opentrons import instruments, containers

# Labware setup
plate = containers.load('6-well','A1')

# Pipette setup
pipette = instruments.P300_Single(
    mount='left',
    tip_racks=[containers.load('tiprack-200ul', 'B1')]
)

# Protocol 

# Step 1: Dispense 2 ml of PBS into each well

pipette.distribute(2 ml, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')

# Step 2: Dispense 200 ul of E-Cadherin antibody into each well

pipette.distribute(200 ul, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')

# Step 3: Incubate the plate in an appropriate incubator for 1 hour 
opentrons.run.incubate(
    plate,
    time = 1 hour,
    temperature=37°C,
    shaking=True
)

# Step 4: Remove the plate from the incubator and wash it twice with PBS

for i in range (2):
    pipette.distribute(2 ml, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')
    opentrons.run.wash(
        plate, 
        buffer=PBS,
        times=2
    )

# Step 5: Dispense 200 ul of secondary antibody into each well

pipette.distribute(200 ul, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')

# Step 6: Incubate the plate in an appropriate incubator for 1 hour 
opentrons.run.incubate(
    plate,
    time = 1 hour,
    temperature=37°C,
    shaking=True
)

# Step 7: Remove the plate from the incubator and wash it twice with PBS

for i in range (2):
    pipette.distribute(2 ml, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')
    opentrons.run.wash(
        plate, 
        buffer=PBS,
        times=2
    )

# Step 8: Dispense 200 ul of visualization reagent into each well

pipette.distribute(200 ul, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')

# Step 9: Incubate the plate in an appropriate incubator for 1 hour 
opentrons.run.incubate(
    plate,
    time = 1 hour,
    temperature=37°C,
    shaking=True
)

# Step 10: Remove the plate from the incubator and wash it twice with PBS

for i in range (2):
    pipette.distribute(2 ml, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='always')
    opentrons.run.wash(
        plate, 
        buffer=PBS,
        times=2
    )

# Step 11: Visualize the cells using a fluorescence microscope
# Note: This step should be done manually and will not be automated.


:*************************


