Certainly! Here's a Python script that should work for your experiment:

```
# Import necessary modules
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Medium Exchange',
    'author': 'Your Name',
    'description': 'Exchanging iPS cell culture medium using PBS(-) and SCM130.'
}

# Define protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load the 6 well plate
    plate = protocol.load_labware('corning_6_wellplate_16.4ml_flat', 2)
    
    # Load the pipettes
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 1)])
    
    # Define which wells to aspirate and dispense from
    wells_to_exchange = [well for row in plate.rows() for well in row[1:5]]
    
    # Define PBS(-) and SCM130
    pbs = protocol.load_labware('usascientific_12_reservoir_22ml', 6)['A1']
    scm130 = protocol.load_labware('usascientific_12_reservoir_22ml', 6)['A2']
    
    # Exchanging medium
    for well in wells_to_exchange:
        # Aspirate PBS(-)
        p300.pick_up_tip()
        p300.aspirate(150, pbs)
        # Dispense PBS(-)
        p300.dispense(150, well)
        # Aspirate and dispense air to remove remaining liquid
        p300.aspirate(20, well)
        p300.dispense(20, pbs)
        # Aspirate SCM130
        p300.aspirate(150, scm130)
        # Dispense SCM130
        p300.dispense(150, well)
        # Aspirate and dispense air to remove remaining liquid
        p300.aspirate(20, well)
        p300.dispense(20, scm130)
        # Drop tip
        p300.drop_tip()   
```

Before trying to run this script, make sure that you have downloaded the "corning_6_wellplate_16.4ml_flat" and "usascientific_12_reservoir_22ml" labware definition files in the OT-2 app from the Opentrons Library under the "Labware" tab.


:*************************


