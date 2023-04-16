from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware Definition
    num_tubes_rack = protocol.load_labware("opentrons_6_tuberack_nest_50ml_conical", '1')
    drug_tubes_rack = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", '2')
    tips_20 = protocol.load_labware("opentrons_96_filtertiprack_20ul", '10')
    tips_200 = protocol.load_labware("opentrons_96_filtertiprack_200ul", '4')
    wellplate_96 = protocol.load_labware("corning_96_wellplate_360ul_flat", '8')

    # Load modules
    heater_shaker = protocol.load_module('temperature module gen2', '7')
    wellplate_96_heater_shaker = heater_shaker.load_labware("corning_96_wellplate_360ul_flat")

    # Pipettes
    pipette_20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    pipette_200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips_200])

    # Protocol steps
    # ... rest of the protocol steps (use wellplate_96_heater_shaker for operations on heater shaker)

