from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
tipracks = [labware.load('opentrons_96_tiprack_20ul', slot)
            for slot in ['2', '3']]

# Define pipettes
p20 = instruments.P20_Single(
    mount='left',
    tip_racks=tipracks
)

# Define reagents
primary_antibody = plate.wells('A1')
secondary_antibody = plate.wells('A2')
dapi = plate.wells('A3')
wash_buff = plate.wells('A4')
permeabilizing_buffer = plate.wells('A5')
blocking_solution = plate.wells('A6')

# Perform experiment
# Move pipette to the position of plate wells, mix and transfer the reagents
p20.pick_up_tip()
p20.mix(3, 20, primary_antibody)
p20.transfer(20, primary_antibody, dapi, new_tip='never')
p20.transfer(5, primary_antibody, plate.wells('B1'), new_tip='never')
p20.drop_tip()

p20.pick_up_tip()
p20.mix(3, 20, secondary_antibody)
p20.transfer(20, secondary_antibody, dapi, new_tip='never')
p20.transfer(5, secondary_antibody, plate.wells('B2'), new_tip='never')
p20.drop_tip()

p20.pick_up_tip()
p20.mix(3, 20, dapi)
p20.transfer(20, dapi, plate.wells('B3'), new_tip='never')
p20.drop_tip()

p20.pick_up_tip()
p20.mix(3, 20, wash_buff)
p20.transfer(20, wash_buff, plate.wells('B4'), new_tip='never')
p20.drop_tip()

p20.pick_up_tip()
p20.mix(3, 20, permeabilizing_buffer)
p20.transfer(20, permeabilizing_buffer, plate.wells('B5'), new_tip='never')
p20.drop_tip()

p20.pick_up_tip()
p20.mix(3, 20, blocking_solution)
p20.transfer(20, blocking_solution, plate.wells('B6'), new_tip='never')
p20.drop_tip()

# Save robot instructions
robot.commands()
