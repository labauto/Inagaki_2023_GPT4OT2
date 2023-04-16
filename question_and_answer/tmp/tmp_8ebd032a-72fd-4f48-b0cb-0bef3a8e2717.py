from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    slot_2_tube_rack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '2')
    slot_3_tube_rack = protocol.load_labware('opentrons_6_tuberack_falcon_15ml_conical', '3')
    slot_4_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    slot_5_tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', '5')
    slot_6_tubes = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '6')
    slot_7_tubes = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '7')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[slot_5_tip_rack])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[slot_4_tip_rack])

    # protocol commands here

if __name__ == '__main__':
    from opentrons import simulate
    simulate.run_protocol(run)
