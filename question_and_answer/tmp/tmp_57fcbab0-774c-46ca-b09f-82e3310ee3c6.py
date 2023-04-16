from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'YOUR_NAME',
    'description': 'Automated hMSC spheroids experiment in 96 well plates with Opentrons',
    'apiLevel': '2.9'
}


def transfer_medium(pipette, source, destination_wells, volume):
    for well in destination_wells:
        pipette.transfer(volume, source, well)


def transfer_cells(pipette, source, destination_wells, volume):
    for well in destination_wells:
        pipette.transfer(volume, source, well)


def add_supplements(pipette, supplement_dict, destination_wells):
    for dest_well in destination_wells:
        pipette.transfer(0.1, supplement_dict['dex'], dest_well)
        pipette.transfer(1, supplement_dict['aa'], dest_well)
        pipette.transfer(1, supplement_dict['bgp'], dest_well)


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    hMSC_dmem = protocol.load_labware('nest_1_reservoir_195ml','1')
    hMSC_dmem_high_glucose = protocol.load_labware('nest_1_reservoir_195ml', '2')
    medium_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    supplements = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '8')

    # Pipettes
    p_1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_1000ul', '3')])

    # Transfer medium
    transfer_medium(p_1000, hMSC_dmem['A1'], medium_plate.columns()[0:6], 100)
    transfer_medium(p_1000, hMSC_dmem_high_glucose['A1'], medium_plate.columns()[6:12], 100)

    # Add supplements
    supplement_dict = {'dex': supplements['A1'], 'aa': supplements['A2'], 'bgp': supplements['A3']}
    add_supplements(p_1000, supplement_dict, medium_plate.columns()[6:12])

    # Transfer cells
    cells = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    transfer_cells(p_1000, cells['A1'], medium_plate.columns()[0:6], 100)
    transfer_cells(p_1000, cells['A1'], medium_plate.columns()[6:12], 100)
