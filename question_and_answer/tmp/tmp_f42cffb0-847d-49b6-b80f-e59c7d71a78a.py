from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Cells Experiment',
    'author': 'Opentrons',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tube_rack_slots_6_7 = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', '6')
    tube_rack_slot_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '7')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '4')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', '5')

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200ul])

    # Rest of the protocol logic
    # ...
