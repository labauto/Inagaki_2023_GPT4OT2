from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC cells to visualize lysosomes',
    'author': 'Your Name <youremail@example.com>',
    'description': 'Opentrons protocol for preparing immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware setup
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', '2')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', '3')
    p1000_single = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1, tiprack_2])

    # Reagent setup
    antibody = plate.columns()[0][0]
    mounting_medium = plate.columns()[0][1]
    wash_buffer = plate.columns()[0][2]

    # Add wash buffer and incubate
    p1000_single.pick_up_tip()
    for well in plate.columns()[0][2:]:
        p1000_single.aspirate(900, wash_buffer)
        p1000_single.dispense(900, well)
    p1000_single.drop_tip()
    protocol.delay(minutes=10)

    # Remove wash buffer and add antibody
    p1000_single.pick_up_tip()
    for well in plate.columns()[0][2:]:
        p1000_single.aspirate(1000, well)
        p1000_single.dispense(1000, protocol.trash_container.wells()[0])
    p1000_single.drop_tip()
    p1000_single.pick_up_tip()
    for well in plate.columns()[0][2:]:
        p1000_single.aspirate(500, antibody)
        p1000_single.dispense(500, well)
    p1000_single.drop_tip()
    protocol.delay(minutes=30)

    # Remove antibody and add mounting medium
    p1000_single.pick_up_tip()
    for well in plate.columns()[0][2:]:
        p1000_single.aspirate(1000, well)
        p1000_single.dispense(1000, protocol.trash_container.wells()[0])
    p1000_single.drop_tip()
    p1000_single.pick_up_tip()
    for well in plate.columns()[0][2:]:
        p1000_single.aspirate(250, mounting_medium)
        p1000_single.dispense(250, well)
    p1000_single.drop_tip()
    protocol.comment('Protocol is complete!')
