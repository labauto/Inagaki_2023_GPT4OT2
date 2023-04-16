# Importing everything we need
from opentrons import protocol_api

# Metadata
metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Immunostaining Protocol',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes'
}

# Defining and running the protocol
def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', 2)

    # Load tiprack and pipette
    pipette = protocol.load_instrument('p10_single', mount='right', tip_racks=[tiprack_10])

    # Mix and transfer cells and reagents
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.mix(5, 10, well)
        pipette.transfer(5, well, tiprack_10['A1'])
        pipette.drop_tip()
