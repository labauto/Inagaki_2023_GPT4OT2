metadata = {
    'protocolName': 'Immunostaining hMSC Cells',
    'author': 'Your Name',
    'description': 'Protocol to prepare immunostained hMSC cells for lysosome visualization',
    'apiLevel': '2.0'
}


def run(ctx):

    # Load labware
    plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    tiprack_1000 = ctx.load_labware('opentrons_96_tiprack_1000ul', '2')

    # Load pipettes
    p1000 = ctx.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Mixing reagents
    p1000.pick_up_tip()
    for i in range(5):
        p1000.aspirate(800, plate['A1'])
        p1000.dispense(800, plate['A1'])
    p1000.mix(5, 800, plate['A1'])
    p1000.blow_out(plate['A1'].top())
    p1000.drop_tip()

    # Add primary antibody
    for well in plate:
        p1000.pick_up_tip()
        p1000.aspirate(800, well)
        p1000.dispense(800, well)
        p1000.mix(5, 800, well)
        p1000.blow_out(well.top())
        p1000.drop_tip()

    # Incubate primary antibody
    ctx.delay(minutes=15)

    # Washing steps
    for i in range(3):
        for well in plate:
            p1000.pick_up_tip()
            p1000.aspirate(1200, well)
            p1000.dispense(1200, well)
            p1000.blow_out(well.top())
            p1000.drop_tip()
        ctx.delay(minutes=2)

    # Add secondary antibody
    for well in plate:
        p1000.pick_up_tip()
        p1000.aspirate(800, well)
        p1000.dispense(800, well)
        p1000.mix(5, 800, well)
        p1000.blow_out(well.top())
        p1000.drop_tip()

    # Incubate secondary antibody
    ctx.delay(minutes=15)

    # Add DAPI
    for well in plate:
        p1000.pick_up_tip()
        p1000.aspirate(800, well)
        p1000.dispense(800, well)
        p1000.mix(5, 800, well)
        p1000.blow_out(well.top())
        p1000.drop_tip()

    # Incubate DAPI
    ctx.delay(minutes=15)

    ctx.comment('Protocol complete.')
