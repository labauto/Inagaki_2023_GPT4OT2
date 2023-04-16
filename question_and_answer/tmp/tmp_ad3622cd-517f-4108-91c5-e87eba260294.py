Sure, here's the Python script for running the experiment you described. Please note that this script only includes the steps for operating the Opentrons machine, and assumes that the necessary reagents and equipment are already in place.

```
from opentrons import simulate, protocol_api

metadata = {'apiLevel': '2.5'}

# Define labware
plate_96 = simulate.load('96-PCR-tall', '1')
tube_rack_1 = simulate.load('tube-rack-2ml', '2')
tube_rack_2 = simulate.load('tube-rack-2ml', '3')
tip_rack_20ul = simulate.load('tiprack-20ul', '4')
tip_rack_200ul = simulate.load('tiprack-200ul', '5')

# Define pipettes
pipette_20 = simulate.P20_Single(
    mount='right',
    tip_racks=[tip_rack_20ul]
)

pipette_200 = simulate.P300_Single(
    mount='left',
    tip_racks=[tip_rack_200ul]
)

# Define variables
cell_count = 8000
cell_vol = 60
drug_vol = 20
drug_concentrations = {
    'A1': 1,
    'A2': 0.1,
    'A3': 0.01,
    'A4': 0.001,
    'A5': 0.0001,
    'A6': 0.00005,
    'B1': 0.00001
}

# Define functions
def seed_cells():
    for well in plate_96:
        if well.row == 'A' and well.column < 6:
            pipette_200.transfer(cell_vol, tube_rack_1.wells()[0], well)

def add_drug():
    for column in range(6):
        for row, concentration in drug_concentrations.items():
            if row == 'A1':
                pipette_200.transfer(drug_vol, tube_rack_2.wells()[0], plate_96.wells_by_name()[row+str(column+1)])
            else:
                pipette_200.transfer(drug_vol, plate_96.wells_by_name()[row+str(column+1-3*column)], plate_96.wells_by_name()[row+str(column+1)])

def add_celltox_green():
    for well in plate_96:
        if well.column < 6:
            pipette_20.transfer(15, tube_rack_2.wells()[1], well)

def shake_plate():
    plate_96.properties['shaking_temperature'] = 25
    plate_96.properties['shaking_duration'] = 120
    plate_96.properties['shaking_speed'] = 500
    plate_96.properties['lid_temperature'] = 25
    plate_96.start_shaking()

def incubate_green():
    plate_96.stop_shaking()
    protocol.delay(minutes=15)

def add_celltiter_glo():
    for well in plate_96:
        if well.column < 6:
            pipette_200.transfer(80, tube_rack_2.wells()[0], well)

def incubate_glo():
    plate_96.properties['shaking_duration'] = 120
    plate_96.start_shaking()
    protocol.delay(minutes=10)
    plate_96.stop_shaking()

def run_protocol():
    # Seed cells
    seed_cells()
    
    # Add drug
    add_drug()
    
    # Add negative controls
    for row in 'ABC':
        pipette_200.transfer(20, tube_rack_2.wells()[2], plate_96.wells_by_name()[row+'5'])

    # Add CellTox Green reagent
    add_celltox_green()

    # Shake plate
    shake_plate()

    # Incubate CellTox Green
    incubate_green()

    # Read CellTox Green fluorescence
    print('Reading CellTox Green fluorescence...')
    # TODO: Add code to read fluorescence using Biotek microplate reader

    # Add CellTiter-Glo reagent
    add_celltiter_glo()

    # Shake plate
    shake_plate()

    # Incubate CellTiter-Glo
    incubate_glo()

    # Read CellTiter-Glo luminescence
    print('Reading CellTiter-Glo luminescence...')
    # TODO: Add code to read luminescence using Biotek microplate reader

run_protocol()
```

This script uses Opentrons' Python API to operate the robot. It defines the necessary labware, pipettes, and variables, and defines functions for each step of the experiment. `run_protocol()` calls each function in sequence to run the entire experiment. 

Please note that this script is only a starting point and would need to be customized for the specific experimental conditions and reagents being used. The TODO comments indicate where additional code would be needed to integrate the Opentrons machine with other systems, such as the Biotek microplate reader for measuring fluorescence and luminescence.


:*************************


