# Import Necessary Packages
from opentrons import protocol_api

# Load Protocol API
protocol = protocol_api.Protocol()

# Load Labware
tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)

# Load Pipette
pipette = protocol.load_instrument('p1000_single', 'right', tip_racks = [tuberack['A1']])

# Washing the 6 Well Plate with PBS(-)
for well in plate.wells():
    pipette.aspirate(1000, tuberack['A1'].wells()[0])
    for _ in range(5):
        pipette.dispense(1000, well)
        pipette.aspirate(1000, well)
    pipette.dispense(1000, well)

# Adding Trypsin Solution
for well in plate.wells():
    pipette.aspirate(1000, tuberack['A1'].wells()[1])
    pipette.dispense(1000, well)
    protocol.delay(minutes = 5)

# Adding Cell Culture Medium
for well in plate.wells():
    pipette.aspirate(1000, tuberack['A1'].wells()[2])
    pipette.dispense(1000, well)

# Finish the Experiment
protocol.home()


:*************************


