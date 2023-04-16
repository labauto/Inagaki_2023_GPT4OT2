from opentrons import labware, instruments, robot

# Define labware and pipettes
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
p200 = instruments.P300_Single(mount='left', tip_racks=[labware.load('tiprack-200ul', '2')])

# Define reagents
pbs = labware.load('usascientific_12_reservoir_22ml', '3')['A1']
dmem = labware.load('usascientific_12_reservoir_22ml', '3')['A2']

# Define transfer volumes and positions
pbs_vol = 200
dmem_vol = 500
source_well = pbs
dest_wells = [well for well in plate.rows(0)]

# Exchange medium
for dest_well in dest_wells:
    # Aspirate old medium with PBS(-)
    p200.pick_up_tip()
    p200.transfer(pbs_vol, dest_well, p200.trash_container.top(), new_tip='never')
    p200.drop_tip()
    
    # Wash well with PBS(-)
    for _ in range(3):
        p200.pick_up_tip()
        p200.transfer(pbs_vol, source_well, dest_well, new_tip='never')
        p200.drop_tip()

    # Aspirate PBS(-) and add D-MEM
    p200.pick_up_tip()
    p200.transfer(pbs_vol, dest_well, p200.trash_container.top(), new_tip='never')
    p200.transfer(dmem_vol, dmem, dest_well, new_tip='always')
    p200.drop_tip()

# Park robot at home position
robot.home()
