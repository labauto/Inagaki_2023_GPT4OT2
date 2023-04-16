# Imports
from opentrons import protocol_api

# Labware and Pipettes
# Load labware modules
plate = protocol_api.load_labware('corning_6_wellplate_16.8ml_flat', 1)
tuberack = protocol_api.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)

# Load pipette modules
p1000 = protocol_api.load_instrument('p1000_single', 'right', tip_racks = [tuberack['A1']])

# Protocol
# Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
for well in plate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tuberack['A2'])
	p1000.dispense(1000, well)
	p1000.aspirate(1000, well)
	p1000.dispense(1000, tuberack['A2'])
	p1000.aspirate(1000, tuberack['A2'])
	p1000.dispense(1000, well)
	p1000.aspirate(1000, well)
	p1000.dispense(1000, tuberack['A2'])
	p1000.aspirate(1000, tuberack['A2'])
	p1000.dispense(1000, well)
	p1000.aspirate(1000, well)
	p1000.dispense(1000, tuberack['A2'])
	p1000.aspirate(1000, tuberack['A2'])
	p1000.dispense(1000, well)
	p1000.aspirate(1000, well)
	p1000.dispense(1000, tuberack['A2'])
	p1000.drop_tip()

# After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
for well in plate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tuberack['A3'])
	p1000.dispense(1000, well)
	p1000.drop_tip()

# Wait for 5 minutes
protocol_api.delay(minutes=5)

# Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
for well in plate.wells():
	p1000.pick_up_tip()
	p1000.aspirate(1000, tuberack['A4'])
	p1000.dispense(1000, well)
	p1000.drop_tip()

# Finish the experiment.
protocol_api.home()


:*************************


