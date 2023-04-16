from opentrons import protocol_api

metadata = {'protocolName': 'Example Protocol', 'author': 'Your Name', 'description': 'An example protocol'}

# Define which labwares are being used
def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    trypsin = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')

    # Define which pipette is being used
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[tiprack])

    # Wash plate with PBS
    for i in range(6):
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin['A1'])
        p1000.dispense(plate['A1'])
        p1000.mix(5, 1000)
        p1000.drop_tip()

    # Add trypsin solution and wait
    p1000.pick_up_tip()
    for well in plate:
        p1000.aspirate(1000, trypsin['A1'])
        p1000.dispense(well)
        p1000.mix(5, 1000)
    p1000.wait_for(300)
    p1000.drop_tip()

    # Add cell culture medium
    for well in plate:
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin['A1'])
        p1000.dispense(well)
        p1000.mix(5, 1000)
        p1000.drop_tip()

    # Finish experiment
    protocol.comment('Protocol complete!')
