from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Immunostaining and lysosome visualization',
    'author': 'Your Name Here <your.name@example.com>',
    'description': 'Protocol to prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.8'
}

# protocol run function. the argument to this function can be either
# an ProtocolContext or a SessionContext
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # reagents
    media = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '2').wells()[0]
    fixative = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3').wells()[0]
    primary_antibody = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '4').wells()[0]
    secondary_antibody = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '5').wells()[0]
    dye = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '6').wells()[0]

    # pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '7')])
    p200 = protocol.load_instrument('p300_multi', 'left')

    # step 1 - replace media
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(800, media)
        p1000.dispense(800, well.top().move(protocol.Point(0,0,-1)), blow_out=True)
    p1000.drop_tip()

    # step 2 - wash cells with PBS
    for _ in range(2):
        p1000.pick_up_tip()
        for well in plate.wells():
            p1000.aspirate(1000, well)
            p1000.dispense(1000, well.top().move(protocol.Point(0,0,-1)), new_tip='never')
        p1000.drop_tip()

    # step 3 - fix cells
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(800, fixative)
        p1000.dispense(800, well.top().move(protocol.Point(0,0,-1)), blow_out=True)
    p1000.drop_tip()

    # step 4 - wash cells with PBS
    for _ in range(2):
        p1000.pick_up_tip()
        for well in plate.wells():
            p1000.aspirate(1000, well)
            p1000.dispense(1000, well.top().move(protocol.Point(0,0,-1)), new_tip='never')
        p1000.drop_tip()

    # step 5 - permeabilize cells
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(800, primary_antibody)
        p1000.dispense(800, well.top().move(protocol.Point(0,0,-1)), blow_out=True)
    p1000.drop_tip()
    protocol.delay(minutes=30)

    # step 6 - wash cells with PBS
    for _ in range(2):
        p1000.pick_up_tip()
        for well in plate.wells():
            p1000.aspirate(1000, well)
            p1000.dispense(1000, well.top().move(protocol.Point(0,0,-1)), new_tip='never')
        p1000.drop_tip()

    # step 7 - add secondary antibody
    p200.set_flow_rate(aspirate=150, dispense=300)
    p200.pick_up_tip()
    for well in plate.wells():
        p200.aspirate(100, secondary_antibody)
        p200.dispense(100, well, new_tip='never')
        p200.mix(5, 30, well)
    p200.drop_tip()

    # step 8 - wash cells with PBS
    for _ in range(2):
        p1000.pick_up_tip()
        for well in plate.wells():
            p1000.aspirate(1000, well)
            p1000.dispense(1000, well.top().move(protocol.Point(0,0,-1)), new_tip='never')
        p1000.drop_tip()

    # step 9 - add dye
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(800, dye)
        p1000.dispense(800, well.top().move(protocol.Point(0,0,-1)), blow_out=True)
    p1000.drop_tip()

    # step 10 - incubate cells
    protocol.delay(minutes=30)

    # step 11 - wash cells with PBS
    for _ in range(2):
        p1000.pick_up_tip()
        for well in plate.wells():
            p1000.aspirate(1000, well)
            p1000.dispense(1000, well.top().move(protocol.Point(0,0,-1)), new_tip='never')
        p1000.drop_tip()

    # step 12 - scan plates
    protocol.comment('Plate can be scanned now to visualize lysosomes')
