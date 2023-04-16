# Import necessary libraries and modules
from opentrons import labware, instruments, robot

# Define labware and pipettes
tiprack_200ul = labware.load('opentrons-tiprack-300ul', '1')
plate_6_well = labware.load('corning-6-well-plate-2.4ml-flat', '2')
pipette_200ul = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack_200ul]
)

# Define volumes to dispense and aspiration speed
PBS_volume = 200 #uL
DMEM_volume = 1000 #uL
aspiration_speed = 50 #uL/s

# Define coordinates to access for each well
well_coordinates = {
    'A1': (47.06, 41.00, 0),
    'B1': (39.23, 41.00, 0),
    'C1': (31.40, 41.00, 0),
    'D1': (23.57, 41.00, 0),
    'E1': (15.74, 41.00, 0),
    'F1': (7.91, 41.00, 0)
}

# Define function to transfer medium
def transfer_medium(from_well, to_well, volume):
    pipette_200ul.pick_up_tip()
    pipette_200ul.aspirate(volume, from_well.bottom(2))
    pipette_200ul.move_to(from_well.top(30))
    pipette_200ul.aspirate(10, from_well.top(30))
    pipette_200ul.move_to(from_well.bottom(2))
    pipette_200ul.flow_rate.aspirate = aspiration_speed
    pipette_200ul.dispense(volume, to_well.bottom(2))
    pipette_200ul.blow_out(to_well.top(10))
    pipette_200ul.drop_tip()

# Define function to exchange medium
def exchange_medium(well, first_volume, second_volume):
    # Aspirate and dispense PBS
    transfer_medium(well, well, first_volume)
    
    # Aspirate and dispense DMEM
    transfer_medium(well, well, second_volume)

# Define well order for exchanging medium
well_order = [
    'A1', 'B1', 'C1', 'D1', 'E1', 'F1'
]

# Run experiment
robot.comment("Starting experiment...")

for well in well_order:
    exchange_medium(plate_6_well.wells(well), PBS_volume, DMEM_volume)

robot.comment("Experiment complete!")
