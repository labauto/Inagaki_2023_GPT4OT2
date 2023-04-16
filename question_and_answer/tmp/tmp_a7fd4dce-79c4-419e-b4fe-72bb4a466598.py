# Import the Opentrons SDK
from opentrons import protocols, labware, instruments

# Define the labware
plate = labware.load('6-well plate', '1')

# Define the pipettes to be used
pipette = instruments.P300_Single(mount='left')

# Define the reagents and commands
pipette.pick_up_tip()

pipette.transfer(150, plate['A1'], plate['A2'], new_tip='never')

pipette.drop_tip()
