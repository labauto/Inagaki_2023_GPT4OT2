# Import the Opentrons library
from opentrons import protocol_api

# Create a protocol object
protocol = protocol_api.ProtocolContext()

# Define the locations of the reagents in the Opentrons robot
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
p1000 = protocol.load_instrument('p1000_single', 'right')
reagent1 = protocol.load_labware('usascientific_12_reservoir_22ml', '2').wells()[0]
reagent2 = protocol.load_labware('usascientific_12_reservoir_22ml', '2').wells()[1]

# Define the positions of the wells to be modified
wells_to_be_modified = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2']

# Define the volume of the pipette to be used
pipette_volume = 250

# Define the number of times the pipette should be used in each well
pipette_repeats = 4

# Define the volume of the reagents to use
reagent1_volume = 5*pipette_volume*pipette_repeats
reagent2_volume = 10*pipette_volume*pipette_repeats

# Define the speed at which the pipette should move
pipette_speed = 300

# Exchange medium for each well
for well in wells_to_be_modified:
   # Pick up the pipette
   p1000.pick_up_tip()

   # Transfer the contents of the well to a waste reservoir
   p1000.aspirate(pipette_volume, plate[well])
   p1000.dispense(pipette_volume, reagent1.top())
   p1000.aspirate(pipette_volume, reagent1.top())

   # Rinse the pipette tip with PBS(-) solution
   for i in range(pipette_repeats):
      p1000.dispense(pipette_volume, plate[well])
      p1000.aspirate(pipette_volume, reagent1.top())

   # Transfer the PBS(-) solution to a waste reservoir
   p1000.dispense(reagent1_volume, reagent1.top())

   # Transfer D-MEM solution to the well
   p1000.aspirate(reagent2_volume, reagent2.top())
   p1000.dispense(reagent2_volume, plate[well])

   # Rinse the pipette tip with D-MEM solution
   for i in range(pipette_repeats):
      p1000.aspirate(pipette_volume, reagent2.top())
      p1000.dispense(pipette_volume, plate[well])

   # Drop the pipette tip
   p1000.drop_tip()
