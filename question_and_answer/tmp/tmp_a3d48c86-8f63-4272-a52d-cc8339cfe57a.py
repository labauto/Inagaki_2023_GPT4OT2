# Import the Opentrons SDK
import opentrons.protocol_api as protocol_api

# Define the protocol
metadata = {
    'protocolName': 'My protocol',
    'author': 'Your Name',
    'description': 'A simple protocol to wash cells',
}
def run(protocol: protocol_api.ProtocolContext):
    # Load the labware you will use
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')

    # Load the pipette you will use
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Define the volumes to use
    pbs_vol = 1000  # uL
    trypsin_vol = 1000  # uL
    medium_vol = 1000  # uL

    # Wash the wells with PBS(-)
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(pbs_vol, well)
        pipette.dispense(pbs_vol, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Add trypsin to the wells and wait
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(trypsin_vol, well)
        pipette.dispense(trypsin_vol, well)
        pipette.blow_out()
        pipette.delay(minutes=5)
        pipette.drop_tip()

    # Add the medium to the wells
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(medium_vol, well)
        pipette.dispense(medium_vol, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Finish the protocol
    protocol.comment("Protocol complete")
