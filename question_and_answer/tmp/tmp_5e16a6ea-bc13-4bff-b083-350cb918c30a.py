from opentrons import robot, labware, instruments


# labware setup
# load labware to the robot
plate = labware.load('corning_6_wellplate_16.8ml_flat', 1)
tray = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)

# pipette setup
# load pipette to the robot
p1000 = instruments.P1000_Single(mount='left', tip_racks=[tray['A1']])

# commands
# wash the 6 well plate with PBS(-) by pipetting up and down 5 times
p1000.set_flow_rate(aspirate=200, dispense=200)
p1000.pick_up_tip()
for i in range(5):
    p1000.aspirate(1000, plate['A1'])
    p1000.dispense(1000, plate['A1'])
    p1000.aspirate(1000, plate['B1'])
    p1000.dispense(1000, plate['B1'])
    p1000.aspirate(1000, plate['C1'])
    p1000.dispense(1000, plate['C1'])
    p1000.aspirate(1000, plate['D1'])
    p1000.dispense(1000, plate['D1'])
    p1000.aspirate(1000, plate['E1'])
    p1000.dispense(1000, plate['E1'])
    p1000.aspirate(1000, plate['F1'])
    p1000.dispense(1000, plate['F1'])
p1000.drop_tip()

# add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
p1000.set_flow_rate(aspirate=200, dispense=200)
p1000.pick_up_tip()
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['A1'])
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['B1'])
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['C1'])
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['D1'])
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['E1'])
p1000.aspirate(1000, tray['A2'])
p1000.dispense(1000, plate['F1'])
p1000.drop_tip()
robot.pause(minutes=5)

# add 1 mL of cell culture medium (DMEM) to the 6 well plate
p1000.set_flow_rate(aspirate=200, dispense=200)
p1000.pick_up_tip()
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['A1'])
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['B1'])
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['C1'])
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['D1'])
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['E1'])
p1000.aspirate(1000, tray['A3'])
p1000.dispense(1000, plate['F1'])
p1000.drop_tip()

# finish the experiment
robot.home()


:*************************


