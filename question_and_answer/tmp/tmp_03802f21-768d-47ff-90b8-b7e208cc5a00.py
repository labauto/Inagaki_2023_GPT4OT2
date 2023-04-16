from opentrons import robot, labware, instruments

# load labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')

# load pipette
p1000 = instruments.P1000_Single(mount = 'left', tip_racks = [tuberack['A1']])

# Wash Plate
# I will split the 2000 µL into two commands
# to avoid aspirating more than the maximum volume
p1000.pick_up_tip()
p1000.aspirate(1000, tuberack['A1'].wells('A1'))
p1000.aspirate(1000, tuberack['A1'].wells('A1'))
p1000.distribute(1000, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'))
p1000.distribute(1000, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'))
p1000.drop_tip()

# Add Trypsin
p1000.pick_up_tip()
p1000.aspirate(1000, tuberack['A1'].wells('A2'))
p1000.distribute(1000, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'))
p1000.drop_tip()

# Wait 5 minutes
robot.pause("Wait 5 minutes")

# Add Cell Culture Medium
p1000.pick_up_tip()
p1000.aspirate(1000, tuberack['A1'].wells('A3'))
p1000.distribute(1000, plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'))
p1000.drop_tip()

# Finish Experiment
robot.comment("Experiment is finished.")


:*************************


