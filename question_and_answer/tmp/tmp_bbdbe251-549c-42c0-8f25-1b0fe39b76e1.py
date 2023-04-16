from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining of hMSC Cells for Lysosomal Visualization',
    'author': 'Your Name',
    'description': 'Protocol to immunostain hMSC cells for lysosomal visualization in a 6 well plate using an Opentrons robot'
}

# Set up a protocol
def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # Load pipette
    pipette = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack])

    # Set up reagents - volumes depend on specific immunostaining protocol
    primary_antibody = plate.wells_by_name()['A1']  
    secondary_antibody = plate.wells_by_name()['B1']  
    DAPI = plate.wells_by_name()['C1']  
    fixative = plate.wells_by_name()['D1'] 
    wash_buffer = plate.wells_by_name()['E1']  
    blocking_buffer = plate.wells_by_name()['F1'] 

    # Perform immunostaining
    # Note: specific timing and order of reagent addition will depend on specific protocol - this is only a rough example
    pipette.pick_up_tip()
    pipette.transfer(100, primary_antibody.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='never')
    pipette.transfer(100, secondary_antibody.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='never')
    pipette.transfer(100, DAPI.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='never')

    # Fix and wash cells
    pipette.transfer(200, fixative.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='always')
    pipette.transfer(200, wash_buffer.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='always')
    pipette.transfer(200, blocking_buffer.bottom(2), plate.rows_by_name()['A'].bottom(2), new_tip='always')

    pipette.drop_tip()
