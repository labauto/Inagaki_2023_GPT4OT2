from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def main(ctx: protocol_api.ProtocolContext):

    # Load labware
    tiprack_20ul = ctx.load_labware('opentrons_96_tiprack_20ul', '10')
    tiprack_200ul = ctx.load_labware('opentrons_96_tiprack_300ul', '4')
    tube_rack_15ml = ctx.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '7')
    tube_rack_snapcap = ctx.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '6')
    tc_plate = ctx.load_labware('corning_96_wellplate_360ul_flat', '1')

    # Load pipettes
    p20 = ctx.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p200 = ctx.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # Tube positions
    tubes_stock = tube_rack_15ml.rows()[0][:7]
    tubes_4x_concentration = tube_rack_15ml.rows()[2][:6] + tube_rack_15ml.rows()[3][:6]

    # Perform dilutions and additions
    for i in range(len(tubes_4x_concentration)):
        p200.pick_up_tip()
        p200.transfer(100, tubes_stock[i], tubes_4x_concentration[i], touch_tip=True, new_tip='never')
        p200.mix(4, 100, tubes_4x_concentration[i])
        p200.drop_tip()

    # Add cells to wells
    cells_to_add = ['A', 'B', 'C', 'D', 'E', 'F']
    cells_trough = tube_rack_snapcap.wells()[:10]
    control_positions = cells_to_add[:3]
    for row in cells_to_add:
        for i, conc_tube in enumerate(tubes_4x_concentration):
            for well in tc_plate.rows()[cells_to_add.index(row)][i * 3: (i + 1) * 3]:
                p200.pick_up_tip()
                p200.transfer(100, conc_tube, well, touch_tip=True, new_tip='never')
                p200.mix(4, 100, well)
                p200.blow_out(well)
                p200.drop_tip()

    # Add cell suspension
    for tube, row in zip(cells_trough, cells_to_add):
        for well in tc_plate.rows()[cells_to_add.index(row)][:3]:
            p200.pick_up_tip()
            p200.transfer(60, tube, well, touch_tip=True, new_tip='never')
            p200.mix(4, 100, well)
            p200.blow_out(well)
            p200.drop_tip()

    # Add negative control
    medium = tube_rack_15ml['A4']
    negative_control_positions = control_positions + ['A4', 'B4', 'C4']
    for well in tc_plate.rows()[0][:3] + tc_plate.rows()[3][:3]:
        p200.pick_up_tip()
        p200.transfer(60, medium, well, touch_tip=True, new_tip='never')
        p200.mix(4, 100, well)
        p200.blow_out(well)
        p200.drop_tip()
