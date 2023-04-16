from opentrons import labware, instruments, robot

# Define the labware
plate_6_well = labware.load('6-well-plate', '1')
trough_1 = labware.load('trough-12row', '2')
trough_2 = labware.load('trough-12row', '3')

# Define the pipettes
pipette_300 = instruments.P300_Single(
    mount='left',
    tip_racks=[labware.load('opentrons-tiprack-300ul', '4')],
    trash_container=labware.load('point', '5')
)

# Define the reagents
PBS_minus = trough_1.wells('A1')
D_MEM = trough_2.wells('A1')

# Define the volumes to aspirate and dispense
volume_to_aspirate = 200
volume_to_dispense = 200

# Define the transfer method
def exchange_medium(well_location, from_location, to_location):
    pipette_300.pick_up_tip()
    pipette_300.aspirate(volume_to_aspirate, from_location)
    pipette_300.dispense(volume_to_dispense, well_location)
    pipette_300.aspirate(volume_to_aspirate, well_location)
    pipette_300.dispense(volume_to_dispense, to_location)
    pipette_300.drop_tip()

# Perform the experiment
for well in plate_6_well.wells():
    exchange_medium(well, PBS_minus, D_MEM)
