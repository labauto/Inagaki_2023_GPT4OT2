

# Python Code

# Import necessary packages
import opentrons

# Initialize robot
robot = opentrons.Robot()

# Pick up tip
tiprack = robot.load_labware('opentrons_96_tiprack_300ul', '1')
pipette = robot.pick_up_tip(tiprack.wells('A1'))

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
for i in range(1, 97):
    pipette.transfer(100,
                     '2:DMEM',
                     '3:' + str(i),
                     new_tip='never')
    
# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
for i in range(1, 97):
    pipette.transfer(100,
                     '4:DMEM High Glucose',
                     '5:' + str(i),
                     new_tip='never')

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
for i in range(1, 97):
    pipette.transfer(0.1,
                     '6:Dex',
                     '5:' + str(i),
                     new_tip='never')
    pipette.transfer(1,
                     '7:AA',
                     '5:' + str(i),
                     new_tip='never')
    pipette.transfer(1,
                     '8:BGP',
                     '5:' + str(i),
                     new_tip='never')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
for i in range(1, 97):
    pipette.transfer(100,
                     '9:hMSC cells',
                     '3:' + str(i),
                     new_tip='never')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
for i in range(1, 97):
    pipette.transfer(100,
                     '9:hMSC cells',
                     '5:' + str(i),
                     new_tip='never')

# Drop tip
robot.drop_tip(pipette)

# End
print('Experiment Completed!')


:*************************


