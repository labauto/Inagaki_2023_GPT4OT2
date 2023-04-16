metadata = {
    'protocolName': 'Cell culture medium exchange',
    'author': 'Your Name',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM. The cells are cultured in a 6-well plate.',
    'apiLevel': '2.11'
}

def run(ctx):

    # Load labware
    plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs = ctx.load_labware('nest_12_reservoir_15ml', '2')
    dmem = ctx.load_labware('nest_12_reservoir_15ml', '3')

    # Load Pipettes
    p1000 = ctx.load_instrument('p1000_single_gen2', 'left', tip_racks=ctx.load_labware('opentrons_96_tiprack_1000ul', '4'))

    # Pick up and transfer 500uL of PBS to each well
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.transfer(500, pbs.wells()[0], well, new_tip='never')
    p1000.drop_tip()

    # Pick up and transfer 1mL of D-MEM to each well
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.transfer(1000, dmem.wells()[0], well, new_tip='never')
    p1000.drop_tip()

    ctx.comment('Protocol complete.')
