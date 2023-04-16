# Import necessary modules
from opentrons import protocol_api

# Create a Protocol object
metadata = {'apiLevel': '2.0'}
protocol = protocol_api.ProtocolContext(metadata=metadata)

# Define the location of the reagents and labware
tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 1)
cell_plate = protocol.load_labware('greiner_6_wellplate_16.2mm', 2)
pbs = protocol.load_labware('nest_12_reservoir_15ml', 3).wells()[:8]

# Define the pipettes
pipette = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])

# Define the transfer steps
pipette.pick_up_tip()
for well in cell_plate.wells()[:3]:
    pipette.transfer(100, pbs[0], well, new_tip='never')

pipette.transfer(100, pbs[1], cell_plate['A4'], new_tip='never')
pipette.transfer(100, pbs[2], cell_plate['B4'], new_tip='never')

pipette.drop_tip()
