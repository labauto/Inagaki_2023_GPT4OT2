# Import modules
from opentrons import simulate, protocol_api

# Define protocol
metadata = {
    'protocolName': 'Cell Culture',
    'author': 'Your Name',
    'description': 'Protocol for cell culture',
    'apiLevel': '2.0'
}

# Define protocol
def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    falcon_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    p1000_pipette = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '3')])
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # Mix five times
    p1000_pipette.pick_up_tip()
    for well in plate.wells():
        p1000_pipette.aspirate(1000, falcon_tube_rack['A1'])
        p1000_pipette.dispense(1000, well)
        for i in range(5):
            p1000_pipette.aspirate(1000, well)
            p1000_pipette.dispense(1000, well)
    p1000_pipette.drop_tip()

    # Add trypsin solution
    p1000_pipette.pick_up_tip()
    for well in plate.wells():
        p1000_pipette.aspirate(1000, falcon_tube_rack['A2'])
        p1000_pipette.dispense(1000, well)
    p1000_pipette.drop_tip()

    # Wait for 5 minutes
    protocol.delay(minutes=5)

    # Add cell culture medium
    p1000_pipette.pick_up_tip()
    for well in plate.wells():
        p1000_pipette.aspirate(1000, falcon_tube_rack['A3'])
        p1000_pipette.dispense(1000, well)
    p1000_pipette.drop_tip()

    # Finish
    protocol.comment("Protocol complete!")
