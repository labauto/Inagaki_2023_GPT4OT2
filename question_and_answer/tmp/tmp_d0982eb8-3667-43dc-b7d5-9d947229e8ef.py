from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay with A549 Cells and Thapsigargin',
    'author': 'Your Name',
    'description': 'Script for automating the viability and cytotoxicity assay using Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
  
    # labware
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)
    falcon_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)

    # pipettes
    p20_single = protocol.load_instrument('p20_single_gen2', 'right')
    p200_single = protocol.load_instrument('p200_single_gen2', 'left')

    # Steps to simulate fixation and staining

    # Add fixative
    p20_single.transfer(20, falcon_rack['B1'], plate_96_well['A1'])

    # Add stain
    p200_single.transfer(75, falcon_rack['C1'], plate_96_well['A1'])

    protocol.pause('Replace the 96-well plate with a new plate and resume to continue.')

    # Steps to simulate washing and imaging steps

    # Wash 1
    p200_single.transfer(190, falcon_rack['D1'], plate_96_well['A1'])

    # Wash 2
    p200_single.transfer(190, falcon_rack['D2'], plate_96_well['A1'])

    # Wash 3
    p200_single.transfer(190, falcon_rack['D3'], plate_96_well['A1'])

    # Image
    protocol.comment('Now, image the plate.')

    protocol.pause('Replace the 96-well plate with a new plate and resume to continue.')

