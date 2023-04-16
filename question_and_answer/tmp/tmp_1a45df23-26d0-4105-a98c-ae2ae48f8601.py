from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'OT',
    'description': 'Automated assay for cell viability and cytotoxicity',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack_1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 6)
    tube_rack_2 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', 4)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    p200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Modules
    model = 'heaterShakerModuleV1'
    if model.lower() == 'heatershakermodulev1':
        heater_shaker = protocol.load_module('heater_shaker', 5)
    else:
        raise ValueError('Invalid module specified.')

    # Samples
    thapsigargin_stock = tube_rack_2.wells('A1')  # 1 mM stock solution of Thapsigargin
    cell_suspension = tube_rack_1.wells('A': 10)
    dilution_tubes = tube_rack_2.wells('C1': 'D7')  # For diluting Thapsigargin
    celltox_green = tube_rack_2.wells('B2')
    celltiter_glo = tube_rack_2.wells('B1')

    # Additional experiment protocol code goes here

