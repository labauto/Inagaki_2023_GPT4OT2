from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'A549 Cell Viability and Cytotoxicity Experiment',
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    tiprack_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')
    tiprack_200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '9')
    num_tubes_rack = protocol.load_labware("opentrons_15_tuberack_falcon_15ml_conical", '1')
    falcon_rack = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", '7')

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # Load heater shaker module
    heater_shaker = protocol.load_module('heaterShakerModuleV1', '9')
    # ... rest of the protocol

