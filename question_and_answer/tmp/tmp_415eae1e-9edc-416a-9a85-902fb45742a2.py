from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):

    # labware setup
    pbs = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    trypsin = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    medium = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # pipette setup
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '5')])
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '6')])

    # wash plate with PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(500, pbs['A1'])
        p1000.dispense(500, well)
        p1000.mix(5, 1000, well)
        p1000.blow_out()
        p1000.drop_tip()

    # add trypsin solution and wait for 5 minutes
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(200, trypsin['A1'])
        p1000.dispense(200, well)
        p1000.mix(5, 1000, well)
        p1000.blow_out()
        p1000.drop_tip()

    protocol.delay(minutes=5)

    # add cell culture medium to the plate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(300, medium['A1'])
        p300.dispense(300, well)
        p300.mix(5, 200, well)
        p300.blow_out()
        p300.drop_tip()
