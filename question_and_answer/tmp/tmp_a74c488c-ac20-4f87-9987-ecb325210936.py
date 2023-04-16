from opentrons import robot, containers, instruments

# Connect to the robot
robot.connect()

# Load labware
plate = containers.load('6-well-plate', 'B1')

# Load pipettes
p1000 = instruments.P1000_Single()

# Define liquids
PBS = 'PBS(-)'
SCM130 = 'SCM130'

# Define wells to aspirate from
aspirate_wells = plate.wells('A1', 'B1', 'C1', 'D1', 'E1', 'F1')

# Define wells to dispense into
dispense_wells = plate.wells('A2', 'B2', 'C2', 'D2', 'E2', 'F2')

# Set dispense volumes for PBS and SCM130
PBS_volume = 800
SCM130_volume = 1000

# Exchange medium
for aspirate, dispense in zip(aspirate_wells, dispense_wells):
    # Aspirate old medium
    p1000.pick_up_tip()
    p1000.aspirate(PBS_volume, aspirate.bottom())
    p1000.aspirate(PBS_volume, aspirate.bottom())
    p1000.drop_tip()
    
    # Wash cells with PBS
    p1000.pick_up_tip()
    p1000.aspirate(PBS_volume, aspirate.bottom())
    p1000.dispense(PBS_volume, dispense.bottom())
    p1000.mix(5, 800, dispense.bottom()) # Mix to resuspend cells
    p1000.drop_tip()
    
    # Add new medium (SCM130)
    p1000.pick_up_tip()
    p1000.aspirate(SCM130_volume, dispense.bottom())
    p1000.dispense(SCM130_volume, dispense.bottom())
    p1000.mix(5, 800, dispense.bottom()) # Mix to resuspend cells
    p1000.drop_tip()
    
# Disconnect from robot
robot.disconnect()
