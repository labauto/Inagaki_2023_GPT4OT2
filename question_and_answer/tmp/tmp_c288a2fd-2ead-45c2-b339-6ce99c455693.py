# Protocol Steps:
# 1. Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
# 2. After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
# 3. Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
# 4. Finish the experiment.

from opentrons import protocol_api

metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name Here',
    'description': 'My protocol description',
    'apiLevel': '2.9'
}


def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    falcon_tube = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[tiprack])

    # Protocol
    for well in plate.wells():
        p1000.transfer(1000, falcon_tube.wells('A1'), well, new_tip='always')
        p1000.transfer(1000, well, falcon_tube.wells('A1'), new_tip='always')
        p1000.transfer(1000, falcon_tube.wells('A2'), well, new_tip='always')
        p1000.transfer(1000, well, falcon_tube.wells('A2'), new_tip='always')
        p1000.transfer(1000, falcon_tube.wells('A3'), well, new_tip='always')
        p1000.transfer(1000, well, falcon_tube.wells('A3'), new_tip='always')
        p1000.transfer(1000, falcon_tube.wells('A4'), well, new_tip='always')
        p1000.transfer(1000, well, falcon_tube.wells('A4'), new_tip='always')

    protocol.comment("Protocol finished!")
