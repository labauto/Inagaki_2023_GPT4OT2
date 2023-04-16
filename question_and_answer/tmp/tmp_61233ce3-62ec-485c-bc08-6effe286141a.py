
# Python Script for hMSC Spheroid Culture

# Import opentrons library
from opentrons import robot

# Initialize the robot
robot.connect()

# Initialize the labware
plate_6well = robot.labware.load('6-well plate', '1')
plate_96well = robot.labware.load('96-well plate', '2')

# Initialize the tips
p300 = robot.instruments.P300_Single

# Start the experiment

# Step 1: Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
def add_medium_OSminus():

    # Pick up the tip
    p300.pick_up_tip()
    
    # Aspirate the medium from 6 well plate
    p300.aspirate(volume=100, location=plate_6well['A1'])
    
    # Dispense the medium to each well in the 96 well plate
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'A')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'B')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'C')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'D')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'E')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'F')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'G')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'H')])

    # Drop the tip
    p300.drop_tip()

# Step 2: Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
def add_medium_OSplus():

    # Pick up the tip
    p300.pick_up_tip()
    
    # Aspirate the medium from 6 well plate
    p300.aspirate(volume=100, location=plate_6well['A2'])
    
    # Dispense the medium to each well in the 96 well plate
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'I')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'J')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'K')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'L')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'M')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'N')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'O')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'P')])

    # Drop the tip
    p300.drop_tip()

# Step 3: Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
def add_supplements_OSplus():

    # Pick up the tip
    p300.pick_up_tip()
    
    # Aspirate the supplements from 6 well plate
    p300.aspirate(volume=0.1, location=plate_6well['A3'])
    p300.aspirate(volume=1, location=plate_6well['A4'])
    p300.aspirate(volume=1, location=plate_6well['A5'])
    
    # Dispense the supplements to each well in the 96 well plate
    for i in range(1,13):
        p300.dispense(volume=0.1, location=plate_96well[(i, 'I')])
    for i in range(1,13):
        p300.dispense(volume=1, location=plate_96well[(i, 'J')])
    for i in range(1,13):
        p300.dispense(volume=1, location=plate_96well[(i, 'K')])
    for i in range(1,13):
        p300.dispense(volume=0.1, location=plate_96well[(i, 'L')])
    for i in range(1,13):
        p300.dispense(volume=1, location=plate_96well[(i, 'M')])
    for i in range(1,13):
        p300.dispense(volume=1, location=plate_96well[(i, 'N')])
    for i in range(1,13):
        p300.dispense(volume=0.1, location=plate_96well[(i, 'O')])
    for i in range(1,13):
        p300.dispense(volume=1, location=plate_96well[(i, 'P')])

    # Drop the tip
    p300.drop_tip()

# Step 4: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
def add_cells_OSminus():

    # Pick up the tip
    p300.pick_up_tip()
    
    # Aspirate the cells from 6 well plate
    p300.aspirate(volume=100, location=plate_6well['A1'])
    
    # Dispense the cells to each well in the 96 well plate
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'A')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'B')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'C')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'D')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'E')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'F')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'G')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'H')])

    # Drop the tip
    p300.drop_tip()

# Step 5: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
def add_cells_OSplus():

    # Pick up the tip
    p300.pick_up_tip()
    
    # Aspirate the cells from 6 well plate
    p300.aspirate(volume=100, location=plate_6well['A1'])
    
    # Dispense the cells to each well in the 96 well plate
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'I')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'J')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'K')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'L')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'M')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'N')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'O')])
    for i in range(1,13):
        p300.dispense(volume=100, location=plate_96well[(i, 'P')])

    # Drop the tip
    p300.drop_tip()

# Main function
def run_experiment():
    add_medium_OSminus()
    add_medium_OSplus()
    add_supplements_OSplus()
    add_cells_OSminus()
    add_cells_OSplus()
    print("Experiment Finished")

# Run the experiment
run_experiment()

# Disconnect the robot
robot.disconnect()


:*************************


