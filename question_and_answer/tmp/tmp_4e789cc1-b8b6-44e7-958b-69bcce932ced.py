import opentrons.protocol_api as protocol_api

metadata = {
    'protocolName': 'Cell Culture and Spheroid Generation',
    'author': 'Your Name <youremail@yourinstitution.edu>',
    'description': 'A protocol to culture hMSC cells and create spheroids with two different conditions, 1) Without osteoinduction supplements (OS-) and 2) With osteoinduction supplements (OS+)',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '5')
    plate_96_wells = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    tiprack_1000ul = protocol.load_labware('opentrons_96_tiprack_1000ul', '4')
    
    # Load instruments
    p1000 = protocol.load_instrument('p1000_single_gen2', mount='left', tip_racks=[tiprack_1000ul])
    
    # Define transfer volumes and locations
    medium_volume = 100  # µl
    cell_volume = 100    # µl
    num_cells = 2500
    
    # Define sources and destinations
    medium_os_neg = plate_96_wells.rows_by_name()['A']
    medium_os_pos = plate_96_wells.rows_by_name()['B']
    cells_os_neg = plate_96_wells.rows_by_name()['C']
    cells_os_pos = plate_96_wells.rows_by_name()['D']
    medium_reservoir = plate_6_wells['A1']
    
    # Distribute medium to each well of 96-well plate (OS-)
    p1000.pick_up_tip()
    for well in medium_os_neg:
        p1000.aspirate(medium_volume, medium_reservoir)
        p1000.dispense(medium_volume, well)
    p1000.drop_tip()
    
    # Distribute medium to each well of 96-well plate (OS+)
    p1000.pick_up_tip()
    for well in medium_os_pos:
        p1000.aspirate(medium_volume, medium_reservoir)
        p1000.dispense(medium_volume, well)
    p1000.drop_tip()
    
    # Add supplements to each well of 96-well plate (OS+)
    p1000.pick_up_tip()
    for well in medium_os_pos:
        p1000.aspirate(0.1, plate_6_wells['A2'])
        p1000.aspirate(1, plate_6_wells['A3'])
        p1000.aspirate(1, plate_6_wells['A4'])
        p1000.dispense(1.1, well)
    p1000.drop_tip()
    
    # Distribute cells to each well of 96-well plate (OS-)
    p1000.pick_up_tip()
    for well in cells_os_neg:
        p1000.aspirate(cell_volume, medium_reservoir)
        p1000.dispense(cell_volume, well)
    p1000.drop_tip()
    
    # Distribute cells to each well of 96-well plate (OS+)
    p1000.pick_up_tip()
    for well in cells_os_pos:
        p1000.aspirate(cell_volume, medium_reservoir)
        p1000.dispense(cell_volume, well)
    p1000.drop_tip()
