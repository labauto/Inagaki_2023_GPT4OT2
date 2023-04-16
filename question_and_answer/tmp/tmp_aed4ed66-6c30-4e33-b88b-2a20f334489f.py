from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '6')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', '4')

    # Pipettes
    p50 = protocol.load_instrument('p50_single', 'right', tip_racks=[tiprack_200ul])

    # Slots: 1 - 96 well plate, 6 - tube rack, 4 - 200ul tiprack

    # Do the experiment steps here...
    # Example: p50.transfer(20, tube_rack['A1'], plate['A1'])

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.10')
    run(protocol)
