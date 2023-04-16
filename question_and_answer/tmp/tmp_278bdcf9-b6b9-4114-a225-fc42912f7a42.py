# Import Opentrons modules
from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1') # 6-well plate
tip_rack_1 = labware.load('opentrons-tiprack-300ul', '2')

# Define instruments
p300 = instruments.P300_Single(mount='left', tip_racks=[tip_rack_1])

# Define reagents
buffer = ...

# Define locations on the plate
cell_locations = [well for well in plate.wells()[:6]]

# Define steps for the protocol
def prepare_cells():
    # 1. Add buffer to each well to wash cells
    p300.pick_up_tip()
    for well in cell_locations:
        p300.transfer(200, buffer, well.top(-5), new_tip='never')
    p300.drop_tip()

    # 2. Fix cells with paraformaldehyde
    p300.pick_up_tip()
    for well in cell_locations:
        p300.transfer(100, paraformaldehyde, well.top(-10), new_tip='never')
    p300.drop_tip()

    # 3. Permeabilize cells with Triton X-100
    p300.pick_up_tip()
    for well in cell_locations:
        p300.transfer(100, triton_x_100, well.top(-10), new_tip='never')
    p300.drop_tip()

    # 4. Block cells with BSA
    p300.pick_up_tip()
    for well in cell_locations:
        p300.transfer(100, bsa, well.top(-10), new_tip='never')
    p300.drop_tip()

    # 5. Stain cells with Lysotracker
    p300.pick_up_tip()
    for well in cell_locations:
        p300.transfer(100, lysotracker, well.top(-10), new_tip='never')
    p300.drop_tip()

prepare_cells() # run the protocol
