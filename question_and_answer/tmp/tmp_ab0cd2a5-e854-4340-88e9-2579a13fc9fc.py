# Import required Opentrons modules
from opentrons import simulate, protocol_api

# Create a protocol object to run on the Opentrons machine
metadata = {
 'protocolName': 'HMSc spheroids',
 'author': 'Your Name Here',
}
protocol = protocol_api.ProtocolContext(metadata=metadata)

# Define the location of the source and destination plates
source_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
destination_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

# Define the location of the tip rack
tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

# Define the pipettes to be used in the experiment
p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
p300.pick_up_tip()
for well in destination_plate.rows_by_index()[0]:
    p300.aspirate(100, source_plate['A1'])
    p300.move_to(well.top())
    p300.dispense(100)
p300.drop_tip()

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
p300.pick_up_tip()
for well in destination_plate.rows_by_index()[1]:
    p300.aspirate(100, source_plate['A1'])
    p300.move_to(well.top())
    p300.dispense(100)
p300.drop_tip()

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
p300.pick_up_tip()
for well in destination_plate.rows_by_index()[1]:
    p300.aspirate(0.1, source_plate['B1'])
    p300.move_to(well.top())
    p300.dispense(0.1)
    p300.aspirate(1, source_plate['C1'])
    p300.move_to(well.top())
    p300.dispense(1)
    p300.aspirate(1, source_plate['D1'])
    p300.move_to(well.top())
    p300.dispense(1)
p300.drop_tip()

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
p300.pick_up_tip()
for well in destination_plate.rows_by_index()[0]:
    p300.aspirate(100, source_plate['A2'])
    p300.move_to(well.top())
    p300.dispense(100)
p300.drop_tip()

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
p300.pick_up_tip()
for well in destination_plate.rows_by_index()[1]:
    p300.aspirate(100, source_plate['A2'])
    p300.move_to(well.top())
    p300.dispense(100)
p300.drop_tip()
