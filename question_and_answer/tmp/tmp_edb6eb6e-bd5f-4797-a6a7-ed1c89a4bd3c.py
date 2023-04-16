
# Import libraries 
from opentrons import labware, instruments

# Define labware
six_well = labware.load('6-well-plate', '1')
SCM130 = labware.load('SCM130', '2')
PBS_minus = labware.load('PBS_minus', '3')

# Define pipettes
pipette = instruments.P300_Multi(mount='left')

# Steps
# Step1: Aspirate iPS cell culture medium from 6 well plate
pipette.pick_up_tip()
pipette.aspirate(200, six_well.wells('A1'))

# Step2: Dispense iPS cell culture medium into SCM130
pipette.dispense(200, SCM130.wells('A1'))

# Step3: Aspirate PBS(-) from PBS_minus
pipette.aspirate(200, PBS_minus.wells('A1'))

# Step4: Dispense PBS(-) into 6 well plate
pipette.dispense(200, six_well.wells('A1'))

# Step5: Drop and discard tip
pipette.drop_tip()


:*************************


