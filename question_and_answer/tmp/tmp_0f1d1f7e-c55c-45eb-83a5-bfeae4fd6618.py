Sure, here's a Python script that runs the Opentrons machine and performs the experiment you described:

```
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your Name',
    'description': 'Spheroid culture of hMSC cells on 96-well plates using Opentrons robot',
}

# define the transfer function
def transfer(volume, source, dest):
    pipette.aspirate(volume, source)
    pipette.dispense(volume, dest)

# define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # labware
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    plate_6_cells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '5')
    
    # pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])
    
    # transfer 100 µl of medium to each well of 96 well plate (OS-)
    for well in plate_96_os_minus.rows()[0]:
        transfer(100, plate_6_cells['A1'], well)
    
    # transfer 100 µl of medium (DMEM high glucose) and supplements to each well of 96 well plate (OS+)
    for well in plate_96_os_plus.rows()[0]:
        transfer(100, plate_6_cells['A1'], well)
        transfer(0.1, plate_6_cells['B1'], well)
        transfer(1, plate_6_cells['C1'], well)
        transfer(1, plate_6_cells['D1'], well)
    
    # transfer 100 µl of hMSC cells to each well of 96 well plate (OS-) and (OS+)
    for well in plate_96_os_minus.rows()[0]:
        transfer(100, plate_6_cells['E1'], well)
    
    for well in plate_96_os_plus.rows()[0]:
        transfer(100, plate_6_cells['E1'], well)
    
    # end
    protocol.comment("Protocol completed!")
```
Note: This script is written for the Opentrons API version 2. You may need to modify it slightly if you're using a newer version of the API.


:*************************


