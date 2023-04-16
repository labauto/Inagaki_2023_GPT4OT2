from opentrons import protocol_api, simulate

def run(protocol: protocol_api.ProtocolContext):

    # Defining labwares
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack_15 = protocol.load_labware('opentrons_6_tuberack_falcon_15ml_conical', 2)
    tube_rack_1_5 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', 4)
    tip_rack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 5)

    # Defining pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tip_rack])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tip_rack_200])

    # Aliquoting the 1mM Thapsigargin to other tubes to create stock dilutions
    stock_tg_tube_A1 = tube_rack_1_5.wells_by_name()['A1']
    stock_dilution_tubes = ['A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    for well in stock_dilution_tubes:
        if p20.has_tip:
            p20.drop_tip()
        p20.pick_up_tip(tip_rack[well])
        p20.transfer(35 * 10**-6, stock_tg_tube_A1, tube_rack_1_5.wells_by_name()[well])
        p20.drop_tip()

    # Your following steps go here...
    # ...
