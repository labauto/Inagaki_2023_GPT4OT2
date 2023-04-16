metadata
    author: "Your name"
    description: "Your protocol description"
    apiLevel: 2
    OT2version: "some_version"

def run(ctx):

    # Load labware
    tuberack = ctx.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Load pipette
    p1000 = ctx.load_instrument('p1000_single', 'right')

    # Define volumes
    pbs_vol = 1000
    trypsin_vol = 1000
    media_vol = 1000

    # Perform protocol
    p1000.pick_up_tip()

    for well in plate.wells():
        p1000.aspirate(pbs_vol, tuberack['A1'])
        for _ in range(5):
            p1000.aspirate(200, well)
            p1000.dispense(200, well)
        p1000.dispense(pbs_vol, well)

    p1000.drop_tip()

    p1000.pick_up_tip()

    for well in plate.wells():
        p1000.aspirate(trypsin_vol, tuberack['B1'])
        p1000.dispense(trypsin_vol, well)

    p1000.drop_tip()

    p1000.pick_up_tip()

    for well in plate.wells():
        p1000.aspirate(media_vol, tuberack['C1'])
        p1000.dispense(media_vol, well)

    p1000.drop_tip()
