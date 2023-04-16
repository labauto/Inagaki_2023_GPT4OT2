# Import necessary modules from Opentrons SDK
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Immunostaining of hMSC cells',
    'author': 'Your Name <your.name@example.com>',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.11'
}

# Define protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.76ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')

    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single', mount='left', tip_racks=[tiprack])
    
    # Well locations
    wells = {
        0: 'A1',
        1: 'A2',
        2: 'A3',
        3: 'B1',
        4: 'B2',
        5: 'B3',
    }

    # Perform experiment
    for index, well_name in wells.items():
        
        # Add fixative to well
        well = plate[well_name]
        p1000.pick_up_tip()
        p1000.aspirate(800, well.bottom().move(protocol.Point(0, 0, -4)))
        p1000.dispense(800, well.top())
        p1000.blow_out()
        p1000.drop_tip()
        
        # ... continue with remaining steps of experiment
