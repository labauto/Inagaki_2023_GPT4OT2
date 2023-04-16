
# Python code to run Opentrons Machine

# Imports
from opentrons import robot, containers, instruments

# Robot Setup 
robot.head_speed(x = 18000, y = 18000, z = 5000, a = 700, b = 700)

# Containers
plate_1 = containers.load('96-flat', 'A1')
plate_2 = containers.load('96-flat', 'B1')

tiprack_1000 = containers.load('tiprack-1000ul', 'C1')

# Pipettes SetUp
p1000 = instruments.Pipette(
	axis='a',
	max_volume=1000,
	min_volume=1000,
	tip_racks=[tiprack_1000]
)

# Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
p1000.transfer(
	100, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

# Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
p1000.transfer(
	100, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
p1000.transfer(
	0.1, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

p1000.transfer(
	1, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

p1000.transfer(
	1, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
p1000.transfer(
	100, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'),
	mix_after = True
)

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
p1000.transfer(
	100, 
	plate_1.wells('A1', to='H12'), 
	plate_2.wells('A1', to='H12'), 
	mix_after = True
)

robot.home()


:*************************


