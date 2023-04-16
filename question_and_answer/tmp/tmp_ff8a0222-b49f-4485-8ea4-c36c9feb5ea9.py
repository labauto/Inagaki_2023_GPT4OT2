from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 cells drug test',
    'author': 'Assistant',
    'description': 'Drug testing protocol for A549 cells using Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    dilution_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 7)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Reagents
    celltox_green_reagent = tube_rack['B2']
    celltiter_glo_reagent = tube_rack['B1']
    
    # Dilution tubes
    dilution_tubes = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']

    # Add medium as negative control
    p300.distribute(100, tube_rack['A5'], plate_96.columns[4][:3], new_tip='once')

    # Drug dilutions
    for i in range(1, len(dilution_tubes)):
        source = dilution_tubes[i - 1]
        dest = dilution_tubes[i]
        p20.pick_up_tip()
        p20.mix(3, 25, dilution_rack[source])  # Mix before transferring
        p20.aspirate(25, dilution_rack[source])
        p20.dispense(25, dilution_rack[dest])
        p20.mix(3, 25, dilution_rack[dest])  # Mix after transferring
        p20.drop_tip()
    
    # Proceed with the rest of the protocol steps

