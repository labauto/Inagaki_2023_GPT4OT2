from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 cells thapsigargin treatment',
    'author': 'Assistant',
    'description': 'A549 cells treatment with thapsigargin and cytotoxicity assay',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    
    # Since 'A6' is not a valid well, change the well position to 'A1' or any valid well name present in the tube rack
    cell_suspension = tube_rack.wells_by_name()['A1']

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_20ul', 3)])
    p200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 2)])

    # Distribute cell suspension to the 96 well plate
    p20.distribute(60, cell_suspension, plate_96.wells(), new_tip='always')

    # Steps 5 through 17 would be similar, loading labwares, pipetting the reagents, and handling the samples.

