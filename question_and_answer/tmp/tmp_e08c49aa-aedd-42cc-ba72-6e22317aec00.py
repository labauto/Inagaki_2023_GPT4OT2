from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Cell Preparation',
    'author': 'Opentrons',
    'description': 'Preparation of immunostained hMSC cells for lysosome visualization.',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', '2')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])

    # Protocol
    for i in range(1, 7):
        well = plate_6_well.wells_by_name()[f"A{i}"]
        p20.pick_up_tip()
        p20.aspirate(10, well)
        p20.dispense(10, well)
        p20.drop_tip()

