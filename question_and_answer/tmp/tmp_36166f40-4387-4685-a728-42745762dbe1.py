from opentrons import protocol_api

metadata = {
    'protocolName': '6-well plate medium exchange',
    'author': 'Your Name',
    'description': 'Automated exchange of hMSC cell culture medium using PBS(-) and D-MEM in a 6-well plate using Opentrons machine',
    'apiLevel': '2.11'
}

P300_MULTI_MOUNT = 'right'
P300_MULTI_TYPE = 'p300_multi'
P1000_SINGLE_MOUNT = 'left'
P1000_SINGLE_TYPE = 'p1000_single'

def run(protocol: protocol_api.ProtocolContext):

    # Define labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')
    pbs = protocol.load_labware('nest_12_reservoir_15ml', '4')
    medium = protocol.load_labware('nest_12_reservoir_15ml', '5')

    # Define pipettes
    p300_multi = protocol.load_instrument(P300_MULTI_TYPE, P300_MULTI_MOUNT, tip_racks=[tiprack_300])
    p1000_single = protocol.load_instrument(P1000_SINGLE_TYPE, P1000_SINGLE_MOUNT, tip_racks=[tiprack_1000])

    # Protocol

    # Pick up tips
    p300_multi.pick_up_tip()

    # Transfer 300 uL of PBS to each well
    for well in plate.wells():
        p300_multi.aspirate(300, pbs['A1'])
        p300_multi.dispense(300, well)

    # Drop tips
    p300_multi.drop_tip()

    # Pick up tips
    p1000_single.pick_up_tip()

    # Transfer 800 uL of medium to each well
    for well in plate.wells():
        p1000_single.aspirate(800, medium['A1'])
        p1000_single.dispense(800, well)

    # Drop tips
    p1000_single.drop_tip()
