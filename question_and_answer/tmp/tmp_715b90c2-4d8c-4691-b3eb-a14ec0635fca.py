from opentrons import simulate
protocol = simulate.get_protocol_api()

def run(protocol):
    # Labware
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)
    opentrons_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', 4)
        
    # Pipettes
    pipette_20ul = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    pipette_200ul = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])
    
    # Complete the rest of the experiment


run(protocol)
