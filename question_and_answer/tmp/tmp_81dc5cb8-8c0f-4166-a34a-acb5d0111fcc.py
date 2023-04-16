# Opentrons script for exchanging hMSC cell culture medium using PBS(-) and SCM130

# Importing modules
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'hMSC medium exchange',
    'author': 'Your Name',
    'description': 'An Opentrons protocol for exchanging hMSC cell culture medium using PBS(-) and SCM130 in a 6-well plate',
    'apiLevel': '2.0'
}

# Definining protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    
    # Load instruments
    pipette = protocol.load_instrument('p300_multi', 'left')
    
    # Define locations for reagents
    pbs_col = 1  # A1
    medium_col = 2  # A2
    
    # Define function for transferring medium
    def medium_transfer(volume, source, destination):
        nonlocal tip_count
        if tip_count == 0:
            pipette.pick_up_tip()
        pipette.transfer(volume, source, destination, new_tip='never')
        tip_count += 1
        if tip_count == 8:
            pipette.drop_tip()
            tip_count = 0
    
    # Exchange medium in wells
    wells = plate.rows()[0][:6]
    tip_count = 0
    for well in wells:
        medium_transfer(900, well.bottom(1), reservoir.cols[0][medium_col], tiprack.cols[0][tip_count])
        protocol.delay(minutes=1)
        medium_transfer(900, well.bottom(1), reservoir.cols[0][pbs_col], tiprack.cols[0][tip_count])
        protocol.delay(minutes=1)
        medium_transfer(1800, reservoir.cols[0][medium_col], well.bottom(1), tiprack.cols[0][tip_count])
        protocol.delay(minutes=1)
        pipette.blow_out(well.bottom(1))    
    if tip_count > 0:
        pipette.drop_tip()
        
    protocol.comment('Protocol complete')
