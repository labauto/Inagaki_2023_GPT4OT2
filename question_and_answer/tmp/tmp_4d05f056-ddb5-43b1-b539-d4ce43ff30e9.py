from opentrons import robot, containers, instruments

# Load the labware
plate = robot.load_labware('corning_6_wellplate_16.8ml_flat', slot='1')
p1000 = robot.load_instrument('p1000_single', mount = 'right', tip_racks = [robot.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', slot='2')])

# Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
for well in plate.wells():
    p1000.flow_rate.aspirate = 50
    p1000.flow_rate.dispense = 50
    p1000.pick_up_tip()
    p1000.aspirate(1000, well)
    for _ in range(5):
        p1000.dispense(1000, well)
        p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.drop_tip()

# After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.drop_tip()
    
# Then, add 1 ml of cell culture medium (DMEM) to the 6 well plate
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, well)
    p1000.dispense(1000, well)
    p1000.drop_tip()
    
# Finish the experiment
robot.home()


:*************************


