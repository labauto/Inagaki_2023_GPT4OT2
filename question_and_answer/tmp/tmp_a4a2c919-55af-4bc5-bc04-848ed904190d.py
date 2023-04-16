from opentrons import protocol_api

metadata = {
    'apiLevel': '2.12',  # Specific apiLevel you are using. Please check the latest version if necessary.
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'Your_Name',
    'description': 'Automated cell viabiliy and cytotoxicity using Opentrons'
}

# Other functions for each step of the protocol will be defined here (e.g., def step_1():, def step_2():, and so on)

def run(protocol: protocol_api.ProtocolContext):

    # Initializing labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '4')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '6')
    reagent_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '7')

    # Initializing pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p200_single_gen2', 'left', tip_racks=[tiprack_200ul])

    # Call the other functions for each step here (e.g., step_1(), step_2(), and so on)

