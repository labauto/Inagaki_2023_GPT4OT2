# Import the Opentrons module
from opentrons import labware, instruments, robot

# Define your labware
tiprack_1000 = labware.load('opentrons_96_tiprack_1000ul', '1')
tiprack_200 = labware.load('opentrons_96_tiprack_300ul', '2')
trough = labware.load('trough-12row', '3')
plate = labware.load('6-well-plate-16.8-ml', '4')

# Define your pipettes
pipette_1000 = instruments.P1000_Single(
    mount='right',
    tip_racks=[tiprack_1000]
)
pipette_200 = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack_200]
)

# Define the volumes you'll be using
wash_volume = 1000
trypsin_volume = 1000
medium_volume = 1000

# Define your protocol
def run_custom_protocol():
    # Wash plate with PBS(-)
    for i, well in enumerate(plate.wells()):
        pipette_1000.pick_up_tip()
        pipette_1000.aspirate(wash_volume, trough.wells('A1'))
        pipette_1000.dispense(wash_volume, well)
        for j in range(5):
            pipette_1000.aspirate(wash_volume, well)
            pipette_1000.dispense(wash_volume, well)
        pipette_1000.drop_tip()

    # Add trypsin and wait
    pipette_200.pick_up_tip()
    for well in plate.wells():
        pipette_200.aspirate(trypsin_volume, trough.wells('A2'))
        pipette_200.dispense(trypsin_volume, well)
    pipette_200.drop_tip()
    robot.pause(300)

    # Add cell culture medium
    pipette_1000.pick_up_tip()
    for well in plate.wells():
        pipette_1000.aspirate(medium_volume, trough.wells('A3'))
        pipette_1000.dispense(medium_volume, well)
    pipette_1000.drop_tip()

# Run your protocol
run_custom_protocol()
