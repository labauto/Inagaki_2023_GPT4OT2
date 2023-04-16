from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Cells Preparation',
    'author': 'Assistant',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    lysosome_staining_solution = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right')
    
    # Protocol
    for well in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']:
        p300.pick_up_tip()
        p300.aspirate(100, lysosome_staining_solution['A1'])
        p300.dispense(100, six_well_plate[well])
        p300.mix(5, 100, six_well_plate[well])
        p300.drop_tip()

    protocol.comment('The hMSC cells are now prepared with the lysosome staining solution.')
