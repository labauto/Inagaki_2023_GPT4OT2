from opentrons import robot, labware, instruments

# Connect to the robot
robot.connect()

# Load the labware
plate = labware.load('6-well-plate', 'B1')

# Define the pipette and tip rack
pipette = instruments.P300_Single(mount='left', tip_racks=[labware.load('tiprack-200ul', 'A1')])

# Define the media volumes
pbs_volume = 300  # µL
dmem_volume = 200  # µL


# Start the experiment
# Pick up some tips
pipette.pick_up_tip()

# First exchange: remove media with PBS(-), and then add PBS(-)
pipette.aspirate(pbs_volume, plate[0].bottom(2))  # Remove media from well A1
pipette.dispense(pbs_volume, plate[0].bottom(2))  # Add PBS(-) to well A1

# Second exchange: remove PBS(-) with D-MEM, then add new D-MEM
pipette.aspirate(dmem_volume, plate[0].bottom(2))  # Remove PBS(-) from well A1
pipette.dispense(dmem_volume, plate[0].bottom(2))  # Add new D-MEM to well A1

# Return the tips and disconnect from the robot
pipette.drop_tip()
robot.disconnect()
