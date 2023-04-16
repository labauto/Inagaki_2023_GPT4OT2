 from opentrons import robot, containers, instruments
     
     # Place the 6 well plate on the P300 single-channel pipette
     plate = containers.load('6-well', 'A1')
     
     # Take the P300 single-channel pipette
     pipette = instruments.P300_Single(mount='left', tip_racks=containers.load('tiprack-200ul', 'B2'))
     
     # Take the PBS(-): 
     pbs = containers.load('trough-12row', 'B1')
     # Take the D-MEM: 
     dmem = containers.load('trough-12row', 'B3')
     
     # Start exchanging the medium for each well.
     for i in range(1, 7):
         pipette.pick_up_tip(pbs.wells(i))
         pipette.aspirate(200)
         pipette.dispense(plate.wells(i))
         pipette.return_tip()
         pipette.pick_up_tip(dmem.wells(i))
         pipette.aspirate(200)
         pipette.dispense(plate.wells(i))
         pipette.return_tip()
     
     # Return all tips to the rack
     robot.commands.return_tip()


:*************************


