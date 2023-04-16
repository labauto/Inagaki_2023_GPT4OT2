# Import necessary modules
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name Here',
    'description': 'Automated protocol for washing a 6 well plate and adding trypsin and cell culture medium',
    'apiLevel': '2.11'
}

# Protocol run function
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    wellplate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    
    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '4')])
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '5')])

    # Define volumes and tips
    wash_vol = 1000  # µL
    trypsin_vol = 1000  # µL
    medium_vol = 1000  # µL

    # Wash wellplate with PBS
    p1000.pick_up_tip()
    for well in wellplate.rows()[0][:6]:
        p1000.aspirate(wash_vol, tuberack['A1'])
        for _ in range(5):
            p1000.dispense(wash_vol, well)
            p1000.aspirate(wash_vol, well)
    p1000.drop_tip()

    # Add trypsin
    p300.pick_up_tip()
    for well in wellplate.rows()[0][:6]:
        p300.aspirate(trypsin_vol, tuberack['A2'])
        p300.dispense(trypsin_vol, well)
    protocol.delay(minutes=5)
    p300.drop_tip()

    # Add cell culture medium
    p1000.pick_up_tip()
    for well in wellplate.rows()[0][:6]:
        p1000.aspirate(medium_vol, tuberack['A3'])
        p1000.dispense(medium_vol, well)
    p1000.drop_tip()
    
    # Protocol complete
    protocol.comment('Protocol complete.')
