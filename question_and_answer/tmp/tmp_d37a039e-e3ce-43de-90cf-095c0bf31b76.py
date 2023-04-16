from opentrons import api, types

# create the protocol with an API version
metadata = {'apiLevel': '2.7'}
protocol = api.ProtocolContext(metadata=metadata)

# load the 6 well plate
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

# create pipette
p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[])

# Define the locations
src_well = types.Location(Point(x=0, y=0, z=0), plate)
dest_well = types.Location(Point(x=0, y=0, z=0), plate)

# transfer medium between wells
p300.pick_up_tip()
p300.aspirate(150, src_well)  # Aspirate 150ul from the source well
p300.dispense(150, dest_well)  # Dispense the 150ul to the destination well
p300.drop_tip()
