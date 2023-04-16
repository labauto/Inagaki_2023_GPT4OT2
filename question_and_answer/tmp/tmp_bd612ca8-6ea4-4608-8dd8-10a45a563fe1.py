metadata = {
    'apiLevel': '2.0',
    'protocolName': 'My Protocol'
}

def run(ctx):
    # tiprack
    tiprack = ctx.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", 1)

    # pipette
    pipette = ctx.load_instrument('p1000_single', mount='left', tip_racks=[tiprack])

    # plate
    plate = ctx.load_labware("corning_6_wellplate_16.8ml_flat", 2)

    # steps
    washing_volume = 1000
    trypsin_volume = 1000
    dmep_volume=1000

    # wash
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(washing_volume, well)
        pipette.dispense(washing_volume, well)
        for _ in range(5):
            pipette.aspirate(washing_volume, well)
            pipette.dispense(washing_volume, well)
        pipette.drop_tip()

    # add trypsin
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(trypsin_volume, well)
        pipette.dispense(trypsin_volume, well)
        pipette.delay(minutes=5)
        pipette.drop_tip()

    # add DMEM
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(dmep_volume, well)
        pipette.dispense(dmep_volume, well)
        pipette.drop_tip()
