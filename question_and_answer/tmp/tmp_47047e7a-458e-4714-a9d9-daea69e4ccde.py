
from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS Cell Preparation Protocol',
    'author': 'Your Name Here <your.email@example.com>',
    'description': 'Prepare immunostained iPS cells for lysosome visualization.',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Load the plate
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    
    # Load reagents and samples
    lysotracker = protocol.load_labware('greinerbioone_96_wellplate_2000ul', '2')
    fixative = protocol.load_labware('agilent_24_tuberack_2ml_snapcap', '3').wells()[0]
    media = protocol.load_labware('agilent_50ml_vented').wells()[0]
    
    # Define pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '4')])
    p200 = protocol.load_instrument('p200_multi_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_20ul', '5')])
    
    # Define volumes and transfer reagents
    lysotracker_vol = 25 # uL
    media_vol = 4900 # uL
    cell_vol = 1000 # uL
    fixative_vol = 1000 # uL
    
    p1000.transfer(fixative_vol, fixative, [well.top() for well in plate.wells()], new_tip='always')
    p1000.wait_for_volume()
    
    p200.set_flow_rate(aspirate=4, dispense=4)
    for well in plate.wells():
        p200.transfer(lysotracker_vol, lysotracker.wells()[0], well, new_tip='once')
        p200.transfer(media_vol, media, well, new_tip='once')
        p1000.transfer(cell_vol, well.bottom(2), p1000.tip_racks[0].wells()[0], new_tip='always')
        
    p1000.transfer(media_vol, media, [well.bottom() for well in plate.wells()], new_tip='always')
    
    protocol.comment('Protocol complete.')
 
