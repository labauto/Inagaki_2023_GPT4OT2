# Import necessary libraries
import opentrons.protocol_api

# Load the robot
robot = opentrons.protocol_api.Robot()

# Define the 6-well plate
plate_6 = robot.load_labware('corning_96_wellplate_360ul_flat', '1')

# Define containers and reagents
pbs_container = robot.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
pbs_minus = pbs_container.wells('A1')

d_mem_container = robot.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')
d_mem = d_mem_container.wells('A1')

# Pipette setup
pipette = robot.load_instrument('p300_multi', 'left', tip_racks=[])

# Protocol
# Step 1: Aspirate old medium from each well of the 6-well plate
for well in plate_6.wells():
    pipette.pick_up_tip()
    pipette.aspirate(300, well.bottom())
    pipette.drop_tip()

# Step 2: Dispense PBS(-) into each well of the 6-well plate
for well in plate_6.wells():
    pipette.pick_up_tip()
    pipette.aspirate(200, pbs_minus)
    pipette.dispense(200, well.top())
    pipette.drop_tip()

# Step 3: Dispense D-MEM into each well of the 6-well plate
for well in plate_6.wells():
    pipette.pick_up_tip()
    pipette.aspirate(100, d_mem)
    pipette.dispense(100, well.top())
    pipette.drop_tip()


:*************************


