from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # Loading labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tubes_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 3)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    # Defining pipettes
    pipette_20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    pipette_200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # Instructions
    # (Other functions for each experimental step should be defined here)
    
    # Main function
    # (Call the functions defined above to execute the protocol)

