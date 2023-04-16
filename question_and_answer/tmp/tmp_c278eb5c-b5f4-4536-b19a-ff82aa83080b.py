# Importing required libraries
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Immunostained hMSC Cells Preparation',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.0'
}

# Create protocol object
def run(protocol: protocol_api.ProtocolContext):
    
    # Plate and tip rack information
    tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Reagents information
    pbs = protocol.load_labware('nest_1_reservoir_195ml', '4').wells()[0]
    fixative = protocol.load_labware('nest_1_reservoir_195ml', '5').wells()[0]

    # Transfer PBS to cell plate
    protocol.transfer(200, pbs, cell_plate.wells()[0], new_tip='always')
    
    # Fixation process
    for well in cell_plate.wells()[0:6]:
        protocol.transfer(200, well, tip_rack.wells()[0], new_tip='always')
        protocol.transfer(200, fixative, well, new_tip='always')
        protocol.delay(minutes=10)

    # Wash process
    for well in cell_plate.wells()[0:6]:
        for i in range(3):
            protocol.transfer(200, pbs, well, new_tip='always')

    # Add primary antibody
    for well in cell_plate.wells()[0:6]:
        protocol.transfer(200, well, tip_rack.wells()[0], new_tip='always')
        protocol.transfer(200, fixative, well, new_tip='always')
        protocol.delay(minutes=60)

    # Wash process
    for well in cell_plate.wells()[0:6]:
        for i in range(3):
            protocol.transfer(200, pbs, well, new_tip='always')

    # Add secondary antibody
    for well in cell_plate.wells()[0:6]:
        protocol.transfer(200, well, tip_rack.wells()[0], new_tip='always')
        protocol.transfer(200, fixative, well, new_tip='always')
        protocol.delay(minutes=60)

    # Wash process
    for well in cell_plate.wells()[0:6]:
        for i in range(3):
            protocol.transfer(200, pbs, well, new_tip='always')
