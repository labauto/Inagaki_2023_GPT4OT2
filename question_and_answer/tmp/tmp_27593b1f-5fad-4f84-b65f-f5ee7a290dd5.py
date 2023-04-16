# Importing required Opentrons modules
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name',
    'description': 'A lab protocol using the Opentrons OT-2',
    'apiLevel': '2.0'
}

# protocol run function. the part after the colon lets your editor know
# to offer autocompletion suggestions
def run(protocol: protocol_api.ProtocolContext):
    # load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')

    # check if tiprack is identified as a tip rack
    assert tiprack.is_tiprack

    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    pipette = protocol.load_instrument('p1000_single', mount='left', tip_racks=[tiprack])

    # protocol steps
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, well)
        pipette.dispense(1000, well)
        pipette.drop_tip()
