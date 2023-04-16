# Importing necessary modules
from opentrons import simulate, protocol_api

# metadata
metadata = {
    'protocolName': 'Plate washing and cell harvesting',
    'author': 'Author Name Here',
    'description': 'Script to automate plate washing and cell harvesting',
    'apiLevel': '2.11'
}

# Create a protocol object
protocol = protocol_api.ProtocolContext()

# Load labware
p1000_tip_rack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
pipette_1000 = protocol.load_instrument('p1000_single', mount='right', tip_racks=[p1000_tip_rack])

falcon_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
cell_culture_plate = falcon_tube_rack['A1']
wash_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

# Plate washing and cell harvesting steps
# Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
pipette_1000.pick_up_tip()
for well in wash_plate.wells():
    pipette_1000.distribute(1000, cell_culture_plate, well, new_tip='never')
    for _ in range(5):
        pipette_1000.aspirate(1000, well)
        pipette_1000.dispense(1000, well)
pipette_1000.drop_tip()

# After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
pipette_1000.pick_up_tip()
pipette_1000.aspirate(1000, falcon_tube_rack['B1'])
pipette_1000.dispense(1000, cell_culture_plate)
protocol.delay(minutes=5)

# Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
pipette_1000.pick_up_tip()
for well in wash_plate.wells():
    pipette_1000.aspirate(1000, falcon_tube_rack['C1'])
    pipette_1000.dispense(1000, well)
pipette_1000.drop_tip()

# Finish the experiment.
protocol.comment("Your experiment is finished. Congratulations!")

# Simulating the protocol run
simulate.run(protocol, 'output') # use 'docker' instead of 'output' to run on a robot
