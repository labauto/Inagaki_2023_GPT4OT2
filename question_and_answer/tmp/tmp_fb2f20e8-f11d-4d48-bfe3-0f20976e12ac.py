from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    num_tubes_rack = protocol.load_labware("opentrons_6_tuberack_eppendorf_5ml", '1')
    tc_plate = protocol.load_labware("corning_96_wellplate_360ul_flat", '2')
    slots4_tips = ["4", "5", "6", "7", "8", "9", "10", "11"]  # Load tips to all these slots

    # Modules
    heater_shaker = protocol.load_module('heaterShakerModuleV1', '9')
    
    tip_racks = [protocol.load_labware("opentrons_96_tiprack_300ul", slot) for slot in slots4_tips]

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tips_rack_list)
    
    # Rest of your protocol

