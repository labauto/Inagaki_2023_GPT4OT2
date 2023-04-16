from opentrons import labware, instruments, robot

# Load labware
tiprack = labware.load('tiprack-1000ul', '4')
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
trypsin = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')

# Load pipettes
pipette = instruments.P1000_Single(mount='left', tip_racks=[tiprack])

# Define reagent locations
PBS = trypsin.wells('A1')
trypsin_solution = trypsin.wells('A2')
cell_culture_medium = trypsin.wells('A3')

# Define volumes
PBS_volume = 1000 # 1 ml
trypsin_volume = 1000 # 1 ml
cell_culture_medium_volume = 1000 # 1 ml

# Wash the 6 well plate with PBS(-)
for well in plate.wells():
    # Check if there are enough tips left, if not, pause the robot and ask user to restock the tips
    if pipette.tip_racks[0].next_tip(1000) is None:
        robot.pause()
        print('Please restock tip rack in slot 4 and press resume when ready.')
    # Aspirate PBS and dispense into each well
    pipette.pick_up_tip()
    pipette.aspirate(PBS_volume, PBS)
    pipette.dispense(PBS_volume, well)
    pipette.blow_out()
    pipette.drop_tip()

# Add trypsin solution to the cell culture dish and wait for 5 minutes
pipette.pick_up_tip()
pipette.aspirate(trypsin_volume, trypsin_solution)
pipette.dispense(trypsin_volume, plate.wells('A1','B1','C1','D1','E1','F1'))
pipette.mix(5, trypsin_volume, plate.wells('A1','B1','C1','D1','E1','F1'))
pipette.blow_out()
pipette.drop_tip()
robot.pause(minutes=5)

# Add cell culture medium to the 6 well plate
for well in plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(cell_culture_medium_volume, cell_culture_medium)
    pipette.dispense(cell_culture_medium_volume, well)
    pipette.blow_out()
    pipette.drop_tip()

# Finish the experiment
robot.home()
