Yes, it seems like the Python protocol you uploaded has the Python API Version 1.0 which is not supported by the current robot server version. 

Here's a Python script that uses the Opentrons API Version 2.0 that you can use to perform your experiment:

```
from opentrons import simulate, protocol_api

metadata = {
    'protocolName': 'Immunostaining of hMSC cells',
    'author': 'Your Name',
    'description': 'Protocol to immunostain hMSC cells for lysosomes',
    'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 2)

    # Load pipette
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack])

    # Define reagents and samples
    primary_antibody = 'A1234'
    secondary_antibody = 'S5678'
    hmsc_cells = plate.wells_by_name()['A1']

    # Add primary antibody to cells
    p20.pick_up_tip()
    p20.aspirate(2, primary_antibody)
    p20.dispense(2, hmsc_cells)
    p20.mix(3, 10)
    p20.drop_tip()

    # Add secondary antibody to cells
    p20.pick_up_tip()
    p20.aspirate(2, secondary_antibody)
    p20.dispense(2, hmsc_cells)
    p20.mix(3, 10)
    p20.drop_tip()

    # Finish
    protocol.comment('Protocol complete!')
```

This script uses the Opentrons API to load the necessary labware and pipette, define the reagents and samples, and carry out the immunostaining protocol. 

You may need to adjust the volumes, plate type, or pipette types based on your specific experiment requirements.

After making any necessary changes, you can run this script using the Opentrons hardware or in simulation mode using the Opentrons app.


:*************************


