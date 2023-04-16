from opentrons import labware, instruments, robot

# Load labware
plate_6well = labware.load('corning_6_wellplate_16.8_ml_flat', '1')

tip_rack_10 = labware.load('tiprack-10ul', '2')
tip_rack_300 = labware.load('tiprack-200ul', '3')

buffer = labware.load('96-deep-well', '4')

# Load pipettes
p10 = instruments.P10_Single(mount='right', tip_racks=[tip_rack_10])
p300 = instruments.P300_Single(mount='left', tip_racks=[tip_rack_300])

# Define incubation times
WASH_TIME = 30

# Define reagents and volumes
primary_antibody = buffer.wells('A1')
secondary_antibody = buffer.wells('A2')
wash_buffer1 = buffer.columns('3')[0]
wash_buffer2 = buffer.columns('4')[0]
mounting_medium = buffer.wells('H1')

# Define well coordinates for each step
cell_wells = plate_6well.rows('A')[:6]
primary_ab_wells = plate_6well.rows('B')[:6]
secondary_ab_wells = plate_6well.rows('C')[:6]
wash1_wells = plate_6well.rows('D')[:6]
wash2_wells = plate_6well.rows('E')[:6]
mounting_wells = plate_6well.rows('F')[:6]

# Dispense primary antibody and incubate
for well in primary_ab_wells:
    p10.pick_up_tip()
    p10.transfer(2, primary_antibody, well, new_tip='never')
    p10.mix(3, 10, well)
    p10.drop_tip()

robot.pause('Incubate for 1 hour at 37°C and 5% CO2. Then remove media and wash cells twice with 1x PBS. Add 2 mL of 4% paraformaldehyde in PBS for 20 min at room temperature. Then wash cells once more with 1x PBS.')

# Dispense secondary antibody and incubate
for well in secondary_ab_wells:
    p10.pick_up_tip()
    p10.transfer(2, secondary_antibody, well, new_tip='never')
    p10.mix(3, 10, well)
    p10.drop_tip()

robot.pause(f'Incubate {WASH_TIME} sec at room temperature. Then remove media and wash cells three times with 1x PBS. Prepare mounting medium.')

# Dispense wash buffer 1
for well in wash1_wells:
    p300.pick_up_tip()
    p300.transfer(300, wash_buffer1, well, new_tip='never')
    p300.mix(3, 200, well)
    p300.drop_tip()

robot.pause(f'Incubate {WASH_TIME} sec at room temperature. Remove washing buffer 1.')

# Dispense wash buffer 2
for well in wash2_wells:
    p300.pick_up_tip()
    p300.transfer(300, wash_buffer2, well, new_tip='never')
    p300.mix(3, 200, well)
    p300.drop_tip()

robot.pause(f'Incubate {WASH_TIME} sec at room temperature. Remove washing buffer 2.')

# Dispense mounting medium
for well in mounting_wells:
    p300.pick_up_tip()
    p300.transfer(100, mounting_medium, well, new_tip='never')
    p300.mix(3, 70, well)
    p300.drop_tip()

robot.pause('Cover wells to prevent evaporation and image appropriate channels with fluorescence microscope.')

