from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining of iPS cells to visualize lysosomes',
    'author': 'Your Name',
    'description': 'Prepare immunostained iPS cells to visualize lysosomes.',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)

    # Load tips
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    p200 = protocol.load_instrument('p200_single', 'right', tip_racks=[tiprack_200ul])

    # Add reagents to wells
    p200.pick_up_tip()
    p200.transfer(10, plate.wells('A1'), plate.wells('A2'), new_tip='never')
    p200.transfer(10, plate.wells('C1'), plate.wells('C2'), new_tip='never')
    p200.transfer(10, plate.wells('E1'), plate.wells('E2'), new_tip='never')
    p200.drop_tip()

    # Wash cells
    for well in plate.rows('A', to='F'):
        p200.pick_up_tip()
        p200.transfer(200, well, p200.trash_container.top(), new_tip='never')
        p200.transfer(200, protocol.load_labware('reservoir_300ml', 3).wells('A1'), well, new_tip='never')
        p200.drop_tip()

    # Add antibodies
    p200.pick_up_tip()
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A1'), plate.wells('B1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A2'), plate.wells('D1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A3'), plate.wells('F1'), new_tip='never')
    p200.drop_tip()

    # Incubate
    protocol.delay(minutes=30)

    # Wash cells
    for well in plate.rows('A', to='F'):
        p200.pick_up_tip()
        p200.transfer(200, well, p200.trash_container.top(), new_tip='never')
        p200.transfer(200, protocol.load_labware('reservoir_300ml', 3).wells('A1'), well, new_tip='never')
        p200.drop_tip()

    # Add secondary antibody
    p200.pick_up_tip()
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A1'), plate.wells('B1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A2'), plate.wells('D1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A3'), plate.wells('F1'), new_tip='never')
    p200.drop_tip()

    # Incubate again
    protocol.delay(minutes=30)

    # Wash cells
    for well in plate.rows('A', to='F'):
        p200.pick_up_tip()
        p200.transfer(200, well, p200.trash_container.top(), new_tip='never')
        p200.transfer(200, protocol.load_labware('reservoir_300ml', 3).wells('A1'), well, new_tip='never')
        p200.drop_tip()

    # Add DAPI stain
    p200.pick_up_tip()
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A1'), plate.wells('B1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A2'), plate.wells('D1'), new_tip='never')
    p200.transfer(10, protocol.load_labware('reservoir_300ml', 3).wells('A3'), plate.wells('F1'), new_tip='never')
    p200.drop_tip()

    # Incubate again
    protocol.delay(minutes=10)

    # Wash cells again
    for well in plate.rows('A', to='F'):
        p200.pick_up_tip()
        p200.transfer(200, well, p200.trash_container.top(), new_tip='never')
        p200.transfer(200, protocol.load_labware('reservoir_300ml', 3).wells('A1'), well, new_tip='never')
        p200.drop_tip() 

    protocol.comment('Protocol complete.')
