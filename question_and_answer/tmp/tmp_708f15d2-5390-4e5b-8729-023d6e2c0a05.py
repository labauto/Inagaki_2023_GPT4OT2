from opentrons import protocol_api
import time

metadata = {
    'protocolName': 'Immunostaining hMSC Cells Protocol',
    'author': 'Assistant',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    tips_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '2')
    plate_6W = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    reagent_tube_rack = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', '4')
    waste_rack = protocol.load_labware('agilent_1_reservoir_290ml', '5')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips_20ul])
    p200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips_200ul])

    # Reagents
    lysosome_stain = reagent_tube_rack.wells_by_name()['A1']
    pbs = reagent_tube_rack.wells_by_name()['A2']

    # Protocol
    # Adding lysosome stain
    for well in plate_6W.wells():
        p20.transfer(1, lysosome_stain, well, mix_before=(3, 10), new_tip='always')

    # Incubate for 30 minutes
    protocol.delay(minutes=30)

    # Washing with PBS (3x)
    for _ in range(3):
        for well in plate_6W.wells():
            p200.transfer(150, pbs, well, new_tip='always')
            p200.transfer(150, well, waste_rack.wells_by_name()['A1'], new_tip='always')

    # Add mounting medium with DAPI (nuclear stain)
    for well in plate_6W.wells():
        p20.transfer(2, reagent_tube_rack.wells_by_name()['A3'], well, mix_before=(3, 10), new_tip='always')

    # Incubate for 10 minutes
    protocol.delay(minutes=10)
