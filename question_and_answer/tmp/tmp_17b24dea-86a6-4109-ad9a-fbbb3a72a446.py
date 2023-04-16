# Import Opentrons API modules
from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('6-well-plate', '1')
tiprack = labware.load('tiprack-200ul', '2')

# Define pipette
p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack])

# Define reagent locations
lysotracker = plate['A1']
primary_antibody = plate['A2']
secondary_antibody = plate['A3']
mounting_medium = plate['A4']

# Define steps of experiment
# Dispense Lysotracker
p300.pick_up_tip()
p300.aspirate(200, lysotracker)
p300.dispense(200, plate.wells('A1', to='F1'))
p300.drop_tip()

# Dispense primary antibody
p300.pick_up_tip()
p300.aspirate(200, primary_antibody)
p300.dispense(200, plate.wells('A2', to='F2'))
p300.drop_tip()

# Dispense secondary antibody
p300.pick_up_tip()
p300.aspirate(200, secondary_antibody)
p300.dispense(200, plate.wells('A3', to='F3'))
p300.drop_tip()

# Dispense mounting medium
p300.pick_up_tip()
p300.aspirate(200, mounting_medium)
p300.dispense(200, plate.wells('A4', to='F4'))
p300.drop_tip()
