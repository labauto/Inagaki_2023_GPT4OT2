from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Your Name',
    'description': 'Creating hMSC spheroids in 96 well plates with and without osteoinduction supplements',
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '5')

    # Pipettes
    p10_multi = protocol.load_instrument('p10_multi', 'left', tip_racks=[tiprack_10])
    p50_multi = protocol.load_instrument('p50_multi', 'right', tip_racks=[tiprack_200])

    # Reagents
    dmem = reagent_reservoir.wells_by_name()['A1']
    dmem_high_glucose = reagent_reservoir.wells_by_name()['A2']
    dexamethasone = reagent_reservoir.wells_by_name()['A3']
    ascorbic_acid = reagent_reservoir.wells_by_name()['A4']
    beta_glycerophosphate = reagent_reservoir.wells_by_name()['A5']
    hmsc_cells = reagent_reservoir.wells_by_name()['A6']

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    p10_multi.transfer(0.1, dexamethasone, plate_96_os_plus.wells(), new_tip='always', mix_after=(3, 10))
    p10_multi.transfer(1, ascorbic_acid, plate_96_os_plus.wells(), new_tip='always', mix_after=(3, 10))
    p10_multi.transfer(1, beta_glycerophosphate, plate_96_os_plus.wells(), new_tip='always', mix_after=(3, 10))

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, hmsc_cells, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, hmsc_cells, plate_96_os_plus.wells(), new_tip='always')

    # End
