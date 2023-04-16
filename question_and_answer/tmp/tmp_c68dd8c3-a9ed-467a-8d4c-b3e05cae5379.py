from opentrons import labware, instruments, robot

# Load the labware and pipettes
tiprack = labware.load('opentrons_96_tiprack_1000ul', '1')
p1000 = instruments.P1000_Single(mount='left', tip_racks=[tiprack])
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
well_plate = labware.load('corning_6_wellplate_16.8ml_flat', '3')

# Define the volumes and locations
wash_volume = 1000  # uL
trypsin_volume = 1000  # uL
medium_volume = 1000  # uL
trypsin_location = tuberack.wells('A1')
medium_location = tuberack.wells('A2')
wells_to_wash = well_plate.wells()

# Wash the plate
for well in wells_to_wash:
    p1000.pick_up_tip()
    p1000.aspirate(wash_volume, medium_location)
    p1000.dispense(wash_volume, well)
    p1000.dispense(wash_volume, well)
    p1000.dispense(wash_volume, well)
    p1000.dispense(wash_volume, well)
    p1000.dispense(wash_volume, well)
    p1000.drop_tip()

# Add trypsin and wait
for well in wells_to_wash:
    p1000.pick_up_tip()
    p1000.aspirate(trypsin_volume, trypsin_location)
    p1000.dispense(trypsin_volume, well)
    p1000.drop_tip()

robot.pause('Wait for 5 minutes')

# Add medium
for well in wells_to_wash:
    p1000.pick_up_tip()
    p1000.aspirate(medium_volume, medium_location)
    p1000.dispense(medium_volume, well)
    p1000.drop_tip()
