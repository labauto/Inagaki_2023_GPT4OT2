# Import the Opentrons API
from opentrons import labware, instruments, robot

# Define the labware
plate = labware.load('6-well-plate', '1')
trough = labware.load('trough-12row', '2')

# Define the instruments
pipette = instruments.P300_Single(mount='right')

# Define the volumes
medium_volume = 300  # uL
wash_volume = 500  # uL

# Define the wells to exchange medium
wells_to_exchange = [well for well in plate.wells() if well.row == 'B']

# Exchange medium using PBS(-)
for well in wells_to_exchange:
    pipette.pick_up_tip()
    # Add PBS(-)
    pipette.transfer(wash_volume, trough.wells(0), well.top(), new_tip='never')
    # Aspirate PBS(-)
    pipette.air_gap(10)
    pipette.drop_tip()

# Exchange medium using D-MEM
for well in wells_to_exchange:
    pipette.pick_up_tip()
    # Add D-MEM medium
    pipette.transfer(medium_volume, trough.wells(1), well.top(), new_tip='never')
    # Aspirate medium
    pipette.air_gap(10)
    pipette.drop_tip()

# Return the tip to the tip rack
pipette.home()
