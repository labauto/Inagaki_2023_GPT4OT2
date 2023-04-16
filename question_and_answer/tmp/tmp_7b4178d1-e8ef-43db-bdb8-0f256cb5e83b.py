# Import the necessary modules from the Opentrons SDK
from opentrons import simulate, protocol_api

# Create a Python function that takes in as input the location of the plate well 
# and returns a tuple of the x, y, and z coordinates of the well
def get_well_location(well):
    row, col = well.split()[0], well.split()[1]
    row_num = ord(row) - 65 # Convert the alphabets to numbers
    col_num = int(col) - 1
    well_pos = (col_num * 18 + 9, row_num * 18 + 9, 15) # Offset from the center of the well
    return well_pos

# Define a function that will be used to execute the protocol 
def run(protocol: protocol_api.ProtocolContext):
    
    # Set a variable to track the number of tips that have been used
    tips_used = 0
    
    # Load the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_tiprack_300ul', '2')
    
    # Load the pipette
    pipette = protocol.load_instrument('p300_multi', 'right')
    
    # Define the starting position of the pipette
    pipette.starting_tip = tiprack.wells()[0]
    
    # Define the volume to be dispensed
    dispense_vol = 50

    # Immunostaining iPS cells to mitotic spindles
    # Add fixative agent to the wells
    for well, vol in zip(plate.wells(), [200, 200, 200, 200, 200, 200]):
        pipette.pick_up_tip()
        pipette.aspirate(vol, well)
        pipette.dispense(vol, well.bottom(z=10))
        pipette.mix(5, vol, well)
        pipette.drop_tip()
        tips_used += 1
    
    # Wait for 5 minutes to let the fixative agent take effect
    protocol.delay(minutes=5)
    
     # Wash the wells twice with PBS
    for i in range(2):
        for well in plate.wells():
            well_pos = get_well_location(str(well))
            wash_pos = (well_pos[0], well_pos[1], 5)
            pipette.pick_up_tip()
            pipette.aspirate(200, well.bottom(z=10))
            pipette.dispense(200, wash_pos)
            pipette.mix(5, 150, opentrons_96_tiprack_300ul.columns_by_name()['12'])
            pipette.drop_tip()
            tips_used += 1
    
    # Wait for 5 minutes to let the PBS soak in
    protocol.delay(minutes=5)
    
     # Immunostain the cells
    for well, vol in zip(plate.wells(), [50, 50, 50, 50, 50, 50]):
        pipette.pick_up_tip()
        pipette.aspirate(vol, well.bottom(z=2))
        pipette.dispense(vol, well.bottom(z=10))
        pipette.mix(5, vol, well)
        pipette.drop_tip()
        tips_used += 1
    
    # Wait for 30 minutes to let the immunostain 
    # agent attach to the lysosomes
    protocol.delay(minutes=30)
    
    # Wash the wells twice with PBS
    for i in range(2):
        for well in plate.wells():
            well_pos = get_well_location(str(well))
            wash_pos = (well_pos[0], well_pos[1], 5)
            pipette.pick_up_tip()
            pipette.aspirate(200, well.bottom(z=10))
            pipette.dispense(200, wash_pos)
            pipette.mix(5, 150, opentrons_96_tiprack_300ul.columns_by_name()['12'])
            pipette.drop_tip()
            tips_used += 1
    
    # Wait for 5 minutes to let the PBS soak in
    protocol.delay(minutes=5)
    
    # Add mounting medium to the wells
    for well, vol in zip(plate.wells(), [100, 100, 100, 100, 100, 100]):
        pipette.pick_up_tip()
        pipette.aspirate(vol, well.bottom(z=2))
        pipette.dispense(vol, well.bottom(z=10))
        pipette.mix(5, vol, well)
        pipette.drop_tip()
        tips_used += 1
    
    protocol.comment("Protocol complete. Tips used = {}".format(tips_used))

# Simulate the protocol
simulate.run(run)
