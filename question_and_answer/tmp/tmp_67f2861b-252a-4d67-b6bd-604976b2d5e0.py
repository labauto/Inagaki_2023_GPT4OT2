Here is a simple Python script for running your Opentrons robot experiment:

```
from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Lab Experiment Protocol',
    'author': 'Assistant',
    'description': 'Automated experiment using Opentrons robot'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labwares
    trypsin_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    pbs_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    culture_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)
    tip_rack1 = protocol.load_labware('opentrons_96_tiprack_1000ul', 4)

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tip_rack1])

    # Step 1: Wash the 6 well plate with PBS(-)
    pbs_tube = pbs_tube_rack['A1']
    for well in culture_plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, pbs_tube)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution and wait for 5 minutes
    trypsin_tube = trypsin_tube_rack['A1']
    for well in culture_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin_tube)
        p1000.dispense(1000, well)
        p1000.drop_tip()
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM)
    dmem_tube = trypsin_tube_rack['A2']
    for well in culture_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem_tube)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment - no action required
```


:*************************


