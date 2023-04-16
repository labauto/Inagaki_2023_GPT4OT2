from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'Immunostained hMSC Cell Preparation'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    
    # Pipettes
    pipette_300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Reagents
    cell_culture_medium = plate_6well['A1']
    
    # Wells for the hMSC cells
    wells = ['B1', 'C1', 'A2', 'B2', 'C2', 'A3']

    # Transfer cell culture medium to other wells
    for well in wells:
        pipette_300.pick_up_tip()
        pipette_300.transfer(2000, cell_culture_medium, plate_6well[well], new_tip='never')
        pipette_300.mix(5, 500, plate_6well[well])
        pipette_300.drop_tip()
