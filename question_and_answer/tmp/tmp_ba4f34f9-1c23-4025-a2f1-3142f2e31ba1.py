
# Import libraries
from opentrons import robot, containers, instruments

# Initialize robot
robot.connect()

# Initialize labware
plate = containers.load('6-well-plate', 'A1')
tiprack_1 = containers.load('tiprack-200ul', 'B1')

# Initialize instruments
pipette = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_1]
)

# Take the cells from the 6-well plate
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B1'))
pipette.blow_out(plate.wells('B1'))
pipette.drop_tip()

# Add the cell suspension to the wells in the 6-well plate
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B2'))
pipette.blow_out(plate.wells('B2'))
pipette.drop_tip()

# Add the antibody solution to the wells in the 6-well plate
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B3'))
pipette.blow_out(plate.wells('B3'))
pipette.drop_tip()

# Incubate the cells and antibody solution in the 6-well plate at 37 degrees Celsius for 1 hour
robot.pause()

# Add a wash buffer to the wells to remove unbound antibodies
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B4'))
pipette.blow_out(plate.wells('B4'))
pipette.drop_tip()

# Incubate the cells and wash buffer in the 6-well plate at room temperature for 15 minutes
robot.pause()

# Add the secondary antibody solution to the wells
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B5'))
pipette.blow_out(plate.wells('B5'))
pipette.drop_tip()

# Incubate the cells and secondary antibody solution in the 6-well plate at room temperature for 30 minutes
robot.pause()

# Add a wash buffer to the wells to remove unbound antibodies
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B6'))
pipette.blow_out(plate.wells('B6'))
pipette.drop_tip()

# Incubate the cells and wash buffer in the 6-well plate at room temperature for 15 minutes
robot.pause()

# Add a fixative solution to the wells
pipette.pick_up_tip()
pipette.aspirate(200, plate.wells('A1'))
pipette.dispense(200, plate.wells('B7'))
pipette.blow_out(plate.wells('B7'))
pipette.drop_tip()

# Visualize the immunostained cells with fluorescence microscopy
robot.pause()


:*************************


