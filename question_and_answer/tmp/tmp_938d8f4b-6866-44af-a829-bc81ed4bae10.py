
import opentrons

# Initialize robot
robot = opentrons.Robot()

# Initialize labware
t_75_flask = robot.load_labware('t_75_flask', slot='1')
countess_3 = robot.load_module('countess3', '3')
tube_rack = robot.load_labware('tube_rack_2ml','4')
hepa_filter = robot.load_module('hepa_filter', '5')
hepa_filter.activate_fan(speed='low')
plate = robot.load_labware('96_wellplate_200ul', '7')

# Pipettes 
pipette_left = robot.load_instrument('p10_single', 'left')

# Seeding cells
pipette_left.set_flow_rate(aspirate=100, dispense=100)
pipette_left.pick_up_tip()

# Countess 3 cell count
countess_3.start_count() 

# Dispense cells into 96 well plate
pipette_left.aspirate(volume=60)
pipette_left.dispense(volume=60, dest=plate.wells('A1'), new_tip='never')

# Pipette 4X and 2X concentrations
pipette_left.pick_up_tip()
pipette_left.aspirate(volume=35, src=tube_rack['A1'])
pipette_left.dispense(volume=35, dest=tube_rack['A2'])
pipette_left.aspirate(volume=35, src=tube_rack['A2'])
pipette_left.dispense(volume=35, dest=tube_rack['A3'])
pipette_left.aspirate(volume=35, src=tube_rack['A3'])
pipette_left.dispense(volume=35, dest=tube_rack['A4'])
pipette_left.aspirate(volume=35, src=tube_rack['A4'])
pipette_left.dispense(volume=35, dest=tube_rack['A5'])
pipette_left.aspirate(volume=35, src=tube_rack['A5'])
pipette_left.dispense(volume=35, dest=tube_rack['A6'])
pipette_left.aspirate(volume=35, src=tube_rack['A6'])
pipette_left.dispense(volume=35, dest=tube_rack['B1'])
pipette_left.aspirate(volume=100, src=tube_rack['C1'])
pipette_left.dispense(volume=100, dest=tube_rack['C2'])
pipette_left.aspirate(volume=100, src=tube_rack['C2'])
pipette_left.dispense(volume=100, dest=tube_rack['C3'])
pipette_left.aspirate(volume=100, src=tube_rack['C3'])
pipette_left.dispense(volume=100, dest=tube_rack['C4'])
pipette_left.aspirate(volume=100, src=tube_rack['C4'])
pipette_left.dispense(volume=100, dest=tube_rack['C5'])
pipette_left.aspirate(volume=100, src=tube_rack['C5'])
pipette_left.dispense(volume=100, dest=tube_rack['C6'])
pipette_left.aspirate(volume=100, src=tube_rack['C6'])
pipette_left.dispense(volume=100, dest=tube_rack['D1'])
pipette_left.aspirate(volume=100, src=tube_rack['D1'])
pipette_left.dispense(volume=100, dest=tube_rack['D2'])
pipette_left.aspirate(volume=100, src=tube_rack['D2'])
pipette_left.dispense(volume=100, dest=tube_rack['D3'])
pipette_left.aspirate(volume=100, src=tube_rack['D3'])
pipette_left.dispense(volume=100, dest=tube_rack['D4'])
pipette_left.aspirate(volume=100, src=tube_rack['D4'])
pipette_left.dispense(volume=100, dest=tube_rack['D5'])
pipette_left.aspirate(volume=100, src=tube_rack['D5'])
pipette_left.dispense(volume=100, dest=tube_rack['D6'])

# Add thapsigargin to cells
pipette_left.aspirate(volume=80, src=tube_rack['C1'])
pipette_left.dispense(volume=80, dest=plate.wells('A1'))
pipette_left.aspirate(volume=80, src=tube_rack['C2'])
pipette_left.dispense(volume=80, dest=plate.wells('B1'))
pipette_left.aspirate(volume=80, src=tube_rack['C3'])
pipette_left.dispense(volume=80, dest=plate.wells('C1'))
pipette_left.aspirate(volume=80, src=tube_rack['C4'])
pipette_left.dispense(volume=80, dest=plate.wells('D1'))
pipette_left.aspirate(volume=80, src=tube_rack['C5'])
pipette_left.dispense(volume=80, dest=plate.wells('E1'))
pipette_left.aspirate(volume=80, src=tube_rack['C6'])
pipette_left.dispense(volume=80, dest=plate.wells('F1'))
pipette_left.aspirate(volume=80, src=tube_rack['D1'])
pipette_left.dispense(volume=80, dest=plate.wells('D4'))
pipette_left.aspirate(volume=80, src=tube_rack['D2'])
pipette_left.dispense(volume=80, dest=plate.wells('E4'))
pipette_left.aspirate(volume=80, src=tube_rack['D3'])
pipette_left.dispense(volume=80, dest=plate.wells('F4'))
pipette_left.drop_tip()

# 72 hours after drug treatment
pipette_left.pick_up_tip()

# CellTox Green reagent
pipette_left.aspirate(volume=15, src=tube_rack['B2'])
pipette_left.dispense(volume=15, dest=plate.wells('A1'))
pipette_left.aspirate(volume=15, src=tube_rack['B2'])
pipette_left.dispense(volume=15, dest=plate.wells('B1'))

# Heater Shaker
heater_shaker = robot.load_module('heater_shaker', '6')
heater_shaker.start_shaking(speed=500, orbit=2)

# Cell Titer Glo 2.0
pipette_left.aspirate(volume=80, src=tube_rack['B1'])
pipette_left.dispense(volume=80, dest=plate.wells('A1'))

# Heater Shaker
heater_shaker.start_shaking(speed=500, orbit=2)

# Biotek microplate reader
biotek_microplate_reader = robot.load_module('biotek_microplate_reader', '2')
biotek_microplate_reader.read_fluorescence(excitation=485, emission=520)
biotek_microplate_reader.read_luminescence()

# End
robot.home()


:*************************


