from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Cells Preparation',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.0'
}

# Function to run protocol
def run(protocol: protocol_api.ProtocolContext):
    # Define Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')

    # Define Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tiprack])
    
    # Define Well Positions
    lysis_buffer = plate['A1']
    cells = plate['B1']
    lysosome_stain = plate['C1']
    wash = plate['D1']
    fixative = plate['E1']
    blocking_buffer = plate['F1']

    # Define Volume Amounts
    buffer_volume = 1000
    cell_volume = 500
    lysosome_volume = 25

    # Add lysis buffer to cells
    p1000.pick_up_tip()
    p1000.transfer(buffer_volume, lysis_buffer, cells, new_tip='never')
    p1000.mix(10, buffer_volume, cells)
    p1000.drop_tip()

    # Add cells to lysosome stain
    p1000.pick_up_tip()
    p1000.transfer(cell_volume, cells, lysosome_stain, new_tip='never')
    p1000.mix(10, cell_volume, lysosome_stain)
    p1000.drop_tip()

    # Wash cells with PBS buffer
    p1000.pick_up_tip()
    p1000.transfer(buffer_volume, wash, cells, new_tip='never')
    p1000.mix(10, buffer_volume, cells)
    p1000.drop_tip()

    # Add fixative
    p1000.pick_up_tip()
    p1000.transfer(buffer_volume, fixative, cells, new_tip='never')
    p1000.mix(10, buffer_volume, cells)
    p1000.drop_tip()

    # Block cells with blocking buffer
    p1000.pick_up_tip()
    p1000.transfer(buffer_volume, blocking_buffer, cells, new_tip='never')
    p1000.mix(10, buffer_volume, cells)
    p1000.drop_tip()

    protocol.comment('Done preparing cells!')

