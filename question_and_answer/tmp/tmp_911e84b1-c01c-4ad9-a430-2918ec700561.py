from opentrons import simulate, protocol_api

metadata = {
    'protocolName': 'hMSC Culture with Osteoinduction supplements',
    'author': 'Your Name',
    'description': 'Automated process to culture hMSC cells with or without osteoinduction supplements',
    'apiLevel': '2.8'
}

# Define the location of labware
plate_96_OSM = simulate.get_protocol_api('2.8').load_labware('corning_96_wellplate_360ul_flat', '1')
plate_6_TC = simulate.get_protocol_api('2.8').load_labware('corning_6_wellplate_16.8ml_flat', '2')
tiprack_20 = simulate.get_protocol_api('2.8').load_labware('opentrons_96_filtertiprack_20ul', '3')

# Define pipettes
pipette_20 = simulate.get_protocol_api('2.8').load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])


def run(protocol: protocol_api.ProtocolContext):
    
    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    source_location = plate_6_TC['A1']
    dest_location_start = plate_96_OSM['A1']
    dest_location_end = plate_96_OSM['H12']
    pipette_20.transfer(100, source_location, [dest_location_start.bottom(1), dest_location_end.bottom(1)], new_tip='always')
    
    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    source_location = plate_6_TC['B1']
    dest_location_start = plate_96_OSM['A1']
    dest_location_end = plate_96_OSM['H12']
    pipette_20.transfer(100, source_location, [dest_location_start.bottom(1), dest_location_end.bottom(1)], new_tip='always')
    
    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    source_location_dex = plate_6_TC['C1']
    source_location_aa = plate_6_TC['D1']
    source_location_bgp = plate_6_TC['E1']
    dest_location_start = plate_96_OSM['A1']
    dest_location_end = plate_96_OSM['H12']
    pipette_20.distribute([0.1, 1, 1], [source_location_dex, source_location_aa, source_location_bgp], [dest_location_start.bottom(1), dest_location_end.bottom(1)], new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    source_location = plate_6_TC['F1']
    dest_location_start = plate_96_OSM['A1']
    dest_location_end = plate_96_OSM['H12']
    pipette_20.transfer(100, source_location, [dest_location_start.bottom(1), dest_location_end.bottom(1)], new_tip='always')
    
    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    source_location = plate_6_TC['G1']
    dest_location_start = plate_96_OSM['A1']
    dest_location_end = plate_96_OSM['H12']
    pipette_20.transfer(100, source_location, [dest_location_start.bottom(1), dest_location_end.bottom(1)], new_tip='always')
    
    # End
