from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'author': 'Your Name',
    'description': 'Automated preparation of immunostained hMSC cells to visualize lysosomes',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])
    
    # Protocol
    for i in range(1, 7):
        well = plate_6_well.wells_by_name()[f"A{i}"]
        p300.pick_up_tip()
        # Add your reagents and other steps here as needed
        p300.return_tip()
