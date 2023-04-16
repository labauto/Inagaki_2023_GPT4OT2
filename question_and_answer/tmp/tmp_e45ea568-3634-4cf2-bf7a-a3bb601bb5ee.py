from opentrons import labware, instruments, robot

robot.head_speed(x=18000,  y=18000,  z=5000,  a=700, b=700) # Set the speed of the robot head

# Define labware
p1000rack = labware.load('opentrons_10_tiprack_1000ul', '1')
trypsin_tube = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
cell_plate = labware.load('corning_6_wellplate_16.8ml_flat', '3')

# Define pipette
p1000 = instruments.P1000_Single(mount='right', tip_racks=[p1000rack])

# Define volumes
well_volume = 1000
trypsin_volume = 1000 * 0.25 / 100

# Wash plate
for well in range(6):
    p1000.pick_up_tip()
    p1000.transfer(well_volume, trypsin_tube.wells(0), cell_plate.wells(well), mix_after=(5, 1000))
    p1000.drop_tip()

# Add trypsin
for well in range(6):
    p1000.pick_up_tip()
    p1000.transfer(trypsin_volume, trypsin_tube.wells(0), cell_plate.wells(well), new_tip='never')
    p1000.mix(5, well_volume, cell_plate.wells(well))
    p1000.drop_tip()

# Add DMEM
for well in range(6):
    p1000.pick_up_tip()
    p1000.transfer(well_volume, trypsin_tube.wells(0), cell_plate.wells(well), new_tip='never')
    p1000.mix(5, well_volume, cell_plate.wells(well))
    p1000.drop_tip()

# Finish experiment
robot.comment("Done")

