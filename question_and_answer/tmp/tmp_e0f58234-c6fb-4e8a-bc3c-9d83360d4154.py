# import Opentrons API
from opentrons import labware, instruments, robot

# set up labware
plate = labware.load('6-well-plate', '2')
tip_rack = labware.load('tiprack-200ul', '1')

# set up pipette
pipette = instruments.P300_Single(
    mount='left',
    tip_racks=[tip_rack],
)

# set up buffer and media bottles
pbs = labware.load('point', '3')
dmem = labware.load('point', '4')

# set up buffer and media volumes
buffer_vol = 200   # volume of PBS(-) buffer
media_vol = 800   # volume of D-MEM media

# set up well indices to exchange medium
source_well = 'A1'
wells_to_fill = ['A2', 'A3', 'A4', 'A5', 'A6']

# fill wells with buffer and aspirate
robot.comment("Adding PBS buffer to well {}".format(source_well))
pipette.pick_up_tip()
pipette.transfer(buffer_vol, pbs, plate.wells(source_well),
                 new_tip='never', blow_out=True)
pipette.mix(3, buffer_vol, plate.wells(source_well))
pipette.blow_out()
pipette.return_tip()

for destination_well in wells_to_fill:
    robot.comment("Exchanging medium for well {}".format(destination_well))
    pipette.pick_up_tip()
    pipette.transfer(buffer_vol, plate.wells(source_well), plate.wells(destination_well),
                     new_tip='never', blow_out=True)
    pipette.wait_for_volume(50)
    pipette.transfer(media_vol, dmem, plate.wells(destination_well),
                     new_tip='never', blow_out=True)
    pipette.mix(3, media_vol, plate.wells(destination_well))
    pipette.blow_out()
    pipette.return_tip()
