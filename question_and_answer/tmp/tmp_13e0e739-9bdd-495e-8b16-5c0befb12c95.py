"""
Sure, here's a sample Python script that uses Opentrons machine to exchange hMSC cell culture medium using PBS(-) and D-MEM.
"""

import json
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name <your.name@example.com>',
    'description': 'A protocol to exchange cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.11'
}


# initialize protocol
def run(protocol: protocol_api.ProtocolContext):
    # labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # reagents
    pbs_minus = protocol.load_labware('nest_12_reservoir_15ml', '4')
    dmem = protocol.load_labware('nest_12_reservoir_15ml', '5')

    # transfer 600 uL PBS(-) to all wells of the 6-well plate
    p300.pick_up_tip()
    for well in plate_6_well.wells():
        p300.aspirate(600, pbs_minus['A1'])
        p300.dispense(600, well)
    p300.drop_tip()

    # wait for 5 minutes
    protocol.delay(minutes=5)

    # transfer the spent medium to waste
    p300.pick_up_tip()
    for well in plate_6_well.wells():
        p300.aspirate(600, well)
        p300.dispense(600, protocol.fixed_labware['trash'])
    p300.drop_tip()

    # transfer 600 uL D-MEM to all wells of the 6-well plate
    p300.pick_up_tip()
    for well in plate_6_well.wells():
        p300.aspirate(600, dmem['A1'])
        p300.dispense(600, well)
    p300.drop_tip()
