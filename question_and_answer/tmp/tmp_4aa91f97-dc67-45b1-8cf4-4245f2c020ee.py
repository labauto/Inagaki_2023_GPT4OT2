
# Import libraries
import opentrons

# Load robot and labware
robot = opentrons.robot.api.Robot()

# Load labware to deck
plate_96_well = robot.load_labware('96-well-plate', slot='1')
plate_6_well = robot.load_labware('6-well-plate', slot='2')

# Load pipettes
pipette_1000 = robot.load_instrument('p1000_single', 'right', tip_racks=[])
pipette_200 = robot.load_instrument('p200_single', 'left', tip_racks=[])

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
pipette_1000.transfer(100, plate_6_well.wells('A1'), plate_96_well.wells('A1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('A2'), plate_96_well.wells('B1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('A3'), plate_96_well.wells('C1', length=12), new_tip='always')

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
pipette_1000.transfer(100, plate_6_well.wells('B1'), plate_96_well.wells('D1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('B2'), plate_96_well.wells('E1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('B3'), plate_96_well.wells('F1', length=12), new_tip='always')

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
pipette_200.transfer(0.1, plate_6_well.wells('C1'), plate_96_well.wells('D1', length=12), new_tip='always')
pipette_200.transfer(1, plate_6_well.wells('C2'), plate_96_well.wells('E1', length=12), new_tip='always')
pipette_200.transfer(1, plate_6_well.wells('C3'), plate_96_well.wells('F1', length=12), new_tip='always')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
pipette_1000.transfer(100, plate_6_well.wells('D1'), plate_96_well.wells('A1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('D2'), plate_96_well.wells('B1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('D3'), plate_96_well.wells('C1', length=12), new_tip='always')

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
pipette_1000.transfer(100, plate_6_well.wells('E1'), plate_96_well.wells('D1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('E2'), plate_96_well.wells('E1', length=12), new_tip='always')
pipette_1000.transfer(100, plate_6_well.wells('E3'), plate_96_well.wells('F1', length=12), new_tip='always')

# End
robot.home()


:*************************


