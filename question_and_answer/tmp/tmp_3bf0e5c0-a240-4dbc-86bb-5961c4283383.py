from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.11'}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')

    # pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right')

    # reagents
    pbs = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3').wells()[0]
    trypsin = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3').wells()[1]

    # wash wells with PBS
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs)
        for _ in range(5):
            p1000.aspirate(200, well.bottom(1))
            p1000.dispense(200, well.bottom(1))
        p1000.drop_tip()

    # add trypsin and wait
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well.bottom(1))
        protocol.delay(minutes=5)
        p1000.drop_tip()

    # add DMEM
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, 'A1')
        p1000.dispense(1000, well.bottom(1))
        p1000.drop_tip()

