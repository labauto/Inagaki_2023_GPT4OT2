# Import necessary modules and methods.
from opentrons import labware, instruments

metadata = {'apiLevel': '2.2'}

def run(ctx):

    # Load labware.
    plate = ctx.load_labware('greinerbioone_96_wellplate_2000ul', '1')
    lysotracker = ctx.load_labware('greinerbioone_96_wellplate_2000ul', '2')

    # Load pipette.
    p300 = ctx.load_instrument('p300_single_gen2', 'left')

    # Transfer lysotracker, fixative, and wash buffer to plate and agitate.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, lysotracker.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(3, 100, well)
        p300.drop_tip()

    # Add permeabilization buffer and block.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, buffer.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(2, 100, well)
        p300.drop_tip()

    # Add primary antibody and incubate.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, antibody.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(2, 100, well)
        p300.drop_tip()

    ctx.delay(minutes=30)
    
    # Add secondary antibody and incubate.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, secondary_antibody.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(2, 100, well)
        p300.drop_tip()

    ctx.delay(minutes=30)
    
    # Add DAPI stain and incubate.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, dapi_stain.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(2, 100, well)
        p300.drop_tip()

    ctx.delay(minutes=15)

    # Remove DAPI and wash cells in buffer.
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, buffer.wells()[0], well, air_gap=10, new_tip='never')
        p300.mix(2, 100, well)
        p300.drop_tip()
