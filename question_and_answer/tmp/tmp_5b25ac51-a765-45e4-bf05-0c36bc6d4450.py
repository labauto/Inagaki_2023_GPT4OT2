from opentrons import labware, instruments, robot

# Load labware
tube_rack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
plate = labware.load('corning_6_wellplate_16.8ml_flat', '2')

# Load pipettes
pipette_1000 = instruments.P1000_Single(mount='right')

# Define volumes
PBS_volume = 1000  # µL
trypsin_volume = 1000  # µL
medium_volume = 1000  # µL

# Define commands
def wash_plate():
    pipette_1000.pick_up_tip()
    for well in plate.wells():
        pipette_1000.aspirate(PBS_volume, tube_rack.wells('A1'))
        pipette_1000.dispense(PBS_volume, well)
        pipette_1000.aspirate(PBS_volume, well)
        pipette_1000.dispense(PBS_volume, well)
    pipette_1000.drop_tip()

def add_trypsin():
    pipette_1000.pick_up_tip()
    for well in plate.wells():
        pipette_1000.aspirate(trypsin_volume, tube_rack.wells('A2'))
        pipette_1000.dispense(trypsin_volume, well)
    pipette_1000.drop_tip()

def add_medium():
    pipette_1000.pick_up_tip()
    for well in plate.wells():
        pipette_1000.aspirate(medium_volume, tube_rack.wells('A3'))
        pipette_1000.dispense(medium_volume, well)
    pipette_1000.drop_tip()

# Run the commands
wash_plate()
robot.pause("Please wait for 5 minutes after adding trypsin solution.")
add_medium()
