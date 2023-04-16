from opentrons import protocol_api

metadata = {
    'protocolName': 'Lysosome Immunostaining',
    'author': 'Your Name <your.name@example.com>',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.0'
}


def run(protocol):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)

    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 3)

    p200 = protocol.load_instrument('p200_single_gen2', 'right', tip_racks=[tiprack_200])
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])

    # Add reagents
    p200.pick_up_tip()
    p200.transfer(100, protocol.load_labware('vwr_1.5ml_microtube', 4).wells()[0], plate.rows()[0][0])
    p200.mix(5, 100, plate.rows()[0][0])
    p200.drop_tip()

    # Wash cells
    for well in plate.wells():
        p20.pick_up_tip()
        p20.transfer(10, well, protocol.load_labware('vwr_1.5ml_microtube', 5).wells()[0])
        p20.drop_tip()

    protocol.pause('Remove plate from robot to perform paraformaldehyde fixation')


run(protocol_api.ProtocolContext())  
