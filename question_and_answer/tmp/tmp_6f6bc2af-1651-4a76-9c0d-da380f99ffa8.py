Sure, here's a Python script that should do what you described:

```
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Cell Culture Experiment',
    'author': 'Your Name Here',
    'description': 'A protocol to automate washing of 6 well plates, adding trypsin, then adding DMEM medium',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # load labware and pipettes
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '10')
    falcon_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '11')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    pipette = protocol.load_instrument('p1000_single', 'left', tip_racks=[tiprack])

    # commands
    pipette.pick_up_tip()  # pick up tip from the tiprack

    for well in plate.wells():
        pipette.aspirate(1000, falcon_tuberack['A1'])  # wash well with PBS(-) by pipetting up and down
        pipette.dispense(1000, well)
        for i in range(5):
            pipette.mix(5, 600, well)  # 5 times up and down mixing
        pipette.aspirate(1000, well)  # aspirate the PBS(-)
        pipette.dispense(1000, well)  # dispense the PBS(-)
        pipette.aspirate(1000, falcon_tuberack['A2'])  # add trypsin solution (0.25%) to the well
        pipette.dispense(1000, well)  # dispense the trypsin solution
        protocol.delay(minutes=5)  # wait for 5 minutes
        pipette.aspirate(1000, falcon_tuberack['A3'])  # add DMEM medium to the well
        pipette.dispense(1000, well)  # dispense the DMEM medium

    pipette.drop_tip()  # drop tip to the waste container
```

To run the script, copy and paste it into the Opentrons protocol editor and hit the "run" button. Also, make sure that you have connected your Opentrons machine and loaded the labware and pipettes described in the script. Finally, double-check the labware slots and the pipette types.


:*************************


