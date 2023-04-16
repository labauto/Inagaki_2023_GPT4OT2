from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Cell Viability and Cytotoxicity',
    'author': 'Opentrons <protocols@opentrons.com>',
    'description': 'Measure viability and cytotoxicity of A549 cells treated with Thapsigargin.',
    'apiLevel': '2.0'  # Add the API Level here
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', 2)
    falcon_50ml_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # Steps

    # Step 1 to 4 is performed manually

    # Step 5 to 8: dilute the drug and add it to 96-well plate
    thapsigargin_stock = [
        ('A1', 60*10**-6),
        ('A2', 6*10**-6),
        ('A3', 600*10**-9),
        ('A4', 60*10**-9)
    ]

    for well, volume in thapsigargin_stock:
        stock_tg_tube_A1 = falcon_50ml_rack.wells_by_name()[well]
        for i in range(3):    # 3 wells per concentration
            p20.pick_up_tip()
            p20.aspirate(volume, stock_tg_tube_A1)
            p20.dispense(volume, plate.wells()[i])
            p20.drop_tip()
