from opentrons import protocol_api

metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):
    # Load the labware and pipettes
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '3')])

    # Add PBS(-) to the 6 well plate and wash 5 times
    for well in plate.wells():
        p1000.pick_up_tip()
        for i in range(5):
            p1000.aspirate(1000, pbs_rack['A1'])
            p1000.dispense(1000, well)
            if i < 4:
                p1000.aspirate(1000, well)
                p1000.dispense(1000, pbs_rack['A1'])
        p1000.drop_tip()

    # Add trypsin solution and wait 5 minutes
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(1000 * 0.25, pbs_rack['A2'])
        p1000.dispense(1000 * 0.25, well)
    protocol.delay(minutes=5)

    # Add cell culture medium to the 6 well plate
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(1000, pbs_rack['A3'])
        p1000.dispense(1000, well)
    p1000.drop_tip()
