
import opentrons

# Connect to the robot
robot = opentrons.robot.api.Robot()

# Clean the robot with 70% ethanol
robot.commands.purge_tubes()
robot.commands.set_pipette_flow_rate(rate=50)

# Turn on the HEPA filter at low fan speed
robot.commands.set_fan_speed(speed="low")

# Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day
# Take a 24–48 hours old T-75 flask of A549 cells 
# Count the cells using the automated Countess 3 machine
# Take a cell suspension and dispense in ten 1.5mL snap-capped tubes
# Place the tubes in Slot 6 in the tube rack
# Add the medium in wells A5 to C5 as negative control

robot.commands.aspirate(volume=60, location=robot.fixed_trash['A'])
robot.commands.dispense(volume=60, location=robot.slots['7']['A1'])

# Prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium
# Prepare initial stocks ranging from 10nM to 100microM
# Prepare 4X concentrations of thapsigargin
# Prepare 2X concentrations of thapsigargin

robot.commands.aspirate(volume=35, location=robot.slots['7']['A1'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A1'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['A2'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A2'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['A3'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A3'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['A4'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A4'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['A5'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A5'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['A6'])
robot.commands.dispense(volume=35, location=robot.slots['6']['A6'])
robot.commands.aspirate(volume=35, location=robot.slots['7']['B1'])
robot.commands.dispense(volume=35, location=robot.slots['6']['B1'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C1'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C1'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C2'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C2'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C3'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C3'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C4'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C4'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C5'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C5'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['C6'])
robot.commands.dispense(volume=100, location=robot.slots['7']['C6'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D1'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D1'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D2'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D2'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D3'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D3'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D4'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D4'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D5'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D5'])
robot.commands.aspirate(volume=100, location=robot.slots['6']['D6'])
robot.commands.dispense(volume=100, location=robot.slots['7']['D6'])

# Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate
# Add column-wise the increasing concentrations of thapsigargin
# Wells A5 to C5 contain medium without any cells (medium control)

robot.commands.aspirate(volume=80, location=robot.slots['7']['A1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['A1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['B1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['B1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['C1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['C1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['D1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['D1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['E1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['E1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['F1'])
robot.commands.dispense(volume=80, location=robot.slots['9']['F1'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['D4'])
robot.commands.dispense(volume=80, location=robot.slots['9']['D4'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['E4'])
robot.commands.dispense(volume=80, location=robot.slots['9']['E4'])
robot.commands.aspirate(volume=80, location=robot.slots['7']['F4'])
robot.commands.dispense(volume=80, location=robot.slots['9']['F4'])

# Read the fluorescence at 485 nm excitation and 520 nm emission
# Add CellTox Green reagent

robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense(volume=15, location=robot.slots['9']['A1'])
robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense(volume=15, location=robot.slots['9']['B1'])
robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense(volume=15, location=robot.slots['9']['C1'])
robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense(volume=15, location=robot.slots['9']['D1'])
robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense(volume=15, location=robot.slots['9']['E1'])
robot.commands.aspirate(volume=15, location=robot.slots['10']['B2'])
robot.commands.dispense


:*************************


