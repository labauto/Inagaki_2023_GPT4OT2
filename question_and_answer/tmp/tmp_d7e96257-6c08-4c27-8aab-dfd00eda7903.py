from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Cells to Visualize Lysosomes',
    'author': 'Your Name',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes in a 6-well plate using the Opentrons robot.',
    'apiLevel': '2.0'
}

# Define the protocol run function
def run(protocol: protocol_api.ProtocolContext):
    
    # Load the deck setup
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack])

    # Define the sample locations and volumes
    sample_locations = [(well, vol) for well, vol in zip(plate.wells(), [800, 800, 800, 800, 800, 800])]
    lysosome_volume = 100
    
    # Perform the immunostaining protocol
    for well, vol in sample_locations:
        p1000.pick_up_tip()
        p1000.transfer(vol, well, tiprack.wells()[0], new_tip='never')
        p1000.mix(2, 400)
        p1000.transfer(lysosome_volume, well, tiprack.wells()[1], new_tip='always')
        p1000.blow_out()
        p1000.drop_tip()
