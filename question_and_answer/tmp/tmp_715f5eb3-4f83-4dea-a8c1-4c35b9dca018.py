from opentrons import protocol_api

metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    hMSC_spheroids_osm = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    hMSC_spheroids_os = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    reagent_reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    
    # Pipette
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])

    # Reagents
    dmem = reagent_reservoir['A1']
    dmem_high_glucose = reagent_reservoir['A2']
    dex = reagent_reservoir['A3']
    aa = reagent_reservoir['A4']
    bgp = reagent_reservoir['A5']
    hMSC_cells = reagent_reservoir['A6']

    # Protocol steps
    for well in hMSC_spheroids_osm.wells():
        p300.transfer(100, dmem, well, new_tip='always')

    for well in hMSC_spheroids_os.wells():
        p300.transfer(100, dmem_high_glucose, well, new_tip='always')
        p300.transfer(0.1, dex, well, new_tip='always')
        p300.transfer(1, aa, well, new_tip='always')
        p300.transfer(1, bgp, well, new_tip='always')

    for well in hMSC_spheroids_osm.wells():
        p300.transfer(100, hMSC_cells, well, new_tip='always')

    for well in hMSC_spheroids_os.wells():
        p300.transfer(100, hMSC_cells, well, new_tip='always')
