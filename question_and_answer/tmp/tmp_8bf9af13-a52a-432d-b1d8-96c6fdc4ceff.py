from opentrons import protocol_api

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '11')
    tube_rack = protocol.load_labware('opentrons_15_tuberack_falcon_15_50ml_conical', '6')
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '7')
    tips_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tips_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    
    # Pipettes
    pipette_20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    pipette_200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips_200])
    
    # Module
    heater_shaker = protocol.load_module('heaterShakerModuleV1', '8')
    heated_plate = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')

    # Your protocol steps...
