from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Formation',
    'author': 'Your Name',
    'description': 'Automated preparation of hMSC spheroids with/without osteoinduction supplements',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    reagents = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    well_plate_os_neg = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    well_plate_os_pos = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')

    # Pipettes
    p50 = protocol.load_instrument('p50_single', 'right', tip_racks=[tips_200])
    
    # Reagent wells
    medium_dmem = reagents.wells_by_name()['A1']
    medium_dmem_high = reagents.wells_by_name()['A2']
    hmsc_cells = reagents.wells_by_name()['A3']
    dex = reagents.wells_by_name()['A4']       # Dexamethasone
    aa = reagents.wells_by_name()['A5']        # Ascorbic Acid
    bgp = reagents.wells_by_name()['A6']       # beta-glycerophosphate

    # Protocol
    for well in well_plate_os_neg.wells():
        # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
        p50.transfer(100, medium_dmem, well)
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
        p50.transfer(100, hmsc_cells, well)

    for well in well_plate_os_pos.wells():
        # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
        p50.transfer(100, medium_dmem_high, well)
        # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
        p50.transfer(0.1, dex, well, mix_after=(3, 50))
        p50.transfer(1, aa, well, mix_after=(3, 50))
        p50.transfer(1, bgp, well, mix_after=(3, 50))
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
        p50.transfer(100, hmsc_cells, well)
