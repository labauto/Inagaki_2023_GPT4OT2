Yes, you are trying to load a tube rack labware that has not been defined in the protocol. You can add these two lines of code before loading the labware to specify the version of the labware definition you want to use:

```
from opentrons import types

metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name',
    'description': 'Description of my protocol',
    'apiLevel': '2.0'
}

def setup_robot_and_labware(protocol):
    # load labware
    tube_rack_15 = protocol.load_labware("opentrons_15_tube_rack_falcon_15ml_conical",         6, label="tubes_rack_15")
    tube_rack_50 = protocol.load_labware("opentrons_10_tube_rack_falcon_50ml_conical",         5, label="tubes_rack_50")
    tip_rack_10 = protocol.load_labware('opentrons_96_filtertiprack_10ul', 1, label='tiprack_10')
    tip_rack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', 2, label='tiprack_200')
    
    ... # rest of the code
```

You can adjust the versions of the labware definitions to match the ones you have defined in your Custom Labware Definitions Folder in the Opentrons App.


:*************************


