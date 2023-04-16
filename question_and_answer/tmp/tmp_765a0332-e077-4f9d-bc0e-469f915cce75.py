from opentrons import robot, containers, instruments 

# Setting up the robot
robot.connect(robot.get_serial_ports_list()[0]) 
robot.home() 

# Defining labware 
plate = containers.load("6-well-plate", "A1") 

# Defining the pipette 
pipette = instruments.P300_Single(mount="right") 

# Separating the wells 
well1 = plate.wells("A1") 
well2 = plate.wells("A2") 
well3 = plate.wells("A3") 
well4 = plate.wells("B1") 
well5 = plate.wells("B2") 
well6 = plate.wells("B3") 

# Defining the PBS(-) and D-MEM 
pbs_minus = containers.load("trough-12row", "B2") 
dmem = containers.load("trough-12row", "C3") 

# Exchanging hMSC cell culture medium 
pipette.pick_up_tip() 
pipette.aspirate(volume= 200, location = well1) 
pipette.dispense(volume=200, location=pbs_minus) 
pipette.aspirate(volume= 200, location = pbs_minus) 
pipette.dispense(volume=200, location=well1) 

pipette.aspirate(volume= 200, location = well2) 
pipette.dispense(volume=200, location=dmem) 
pipette.aspirate(volume= 200, location = dmem) 
pipette.dispense(volume=200, location=well2) 

pipette.aspirate(volume= 200, location = well3) 
pipette.dispense(volume=200, location=pbs_minus) 
pipette.aspirate(volume= 200, location = pbs_minus) 
pipette.dispense(volume=200, location=well3) 

pipette.aspirate(volume= 200, location = well4) 
pipette.dispense(volume=200, location=dmem) 
pipette.aspirate(volume= 200, location = dmem) 
pipette.dispense(volume=200, location=well4) 

pipette.aspirate(volume= 200, location = well5) 
pipette.dispense(volume=200, location=pbs_minus) 
pipette.aspirate(volume= 200, location = pbs_minus) 
pipette.dispense(volume=200, location=well5) 

pipette.aspirate(volume= 200, location = well6) 
pipette.dispense(volume=200, location=dmem) 
pipette.aspirate(volume= 200, location = dmem) 
pipette.dispense(volume=200, location=well6) 

# Disconnecting the robot 
robot.disconnect()


:*************************


