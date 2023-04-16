
from opentrons import robot

#Set robot speed and volume
robot.speed_factor = 0.5
well_volume = 200

#Mount and calibrate the pipette
robot.connect()
robot.home()
robot.calibrate_plunger()

#Pickup tip
robot.pick_up_tip()

#Aspirate PBS(-) and dispense into each well
for x in range(1,7):
    robot.aspirate(well_volume, 'A1')
    robot.dispense(well_volume, 'A'+str(x))

#Discard tip
robot.drop_tip()

#Pickup new tip
robot.pick_up_tip()

#Aspirate D-MEM and dispense into each well
for x in range(1,7):
    robot.aspirate(well_volume, 'B1')
    robot.dispense(well_volume, 'A'+str(x))

#Discard tip
robot.drop_tip()

#Home robot
robot.home()

#Disconnect robot
robot.disconnect()


:*************************


