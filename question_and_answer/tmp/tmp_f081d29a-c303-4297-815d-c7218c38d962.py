# Import the necessary modules for the program
from opentrons import labware, instruments

# Load the labware and the pipette

# 10 Tube Rack Falcon
tr = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')

# P1000 Single
p1000 = instruments.P1000_Single(mount='right', tip_racks=[tr['A1']])

# Corning 6 Well Plate
wellplate = labware.load('corning_6_wellplate_16.8ml_flat', '2')

# Start the experiment
# Wash the 6 well plate with PBS(-) by pipetting up and down 5 times
for well in wellplate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tr["A1"].bottom())
	p1000.dispense(1000, well.top(z=7))
	for _ in range(4):
		p1000.aspirate(1000, well.bottom(z=-10))
		p1000.dispense(1000, well.top(z=7))
	p1000.drop_tip()

# Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
for well in wellplate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tr["A1"].bottom())
	p1000.dispense(1000, well.bottom(z=-10))
	p1000.drop_tip()

# Add 1 mL of cell culture medium (DMEM) to the 6 well plate.
for well in wellplate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tr["A1"].bottom())
	p1000.dispense(1000, well.bottom(z=-10))
	p1000.drop_tip()

# Finish the experiment
print('Experiment finished!')


:*************************


