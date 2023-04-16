from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Cell Viability and Cytotoxicity',
    'author': 'Opentrons',
    'description': 'Measure viability and cytotoxicity of A549 cells treated with Thapsigargin',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tip_rack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    tip_rack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)
    tube_rack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)
    tube_rack2 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 3)
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack_200])

    # Heater shaker module
    heater_shaker = protocol.load_module('HeaterShakerModuleV1', 5)

    # Adjust locations and slot numbers according to the labware setup and the instructions given in the description.


# Run the protocol with the desired modifications
if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.11')
    run(protocol)
