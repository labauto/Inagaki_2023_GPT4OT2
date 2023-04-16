from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Opentrons',
    'description': 'Automated hMSC spheroids experiment with and without osteoinduction supplements.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    hMSC_tube_rack = protocol.load_labware('<your_hMSC_tube_rack_labware>', '2')
    supplements_rack = protocol.load_labware('<your_supplement_tube_rack_labware>', '3')
    dmem_tube_rack = protocol.load_labware('<your_dmem_tube_rack_labware>', '4')

    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200])

    # Reagents
    hMSC_cells = hMSC_tube_rack['A1']
    dmso = dmem_tube_rack['A1']
    dmso_high_glucose = dmem_tube_rack['A2']
    dex = supplements_rack['A1']
    aa = supplements_rack['B1']
    bgp = supplements_rack['C1']

    # Protocol steps
    pipette.pick_up_tip()

    # Transfer 100 µl of medium (DMEM) to 96 well plate (OS-)
    for well in plate_96.rows_by_name()['A'][:6]:
        pipette.transfer(100, dmso, well)

    # Transfer 100 µl of medium (DMEM high glucose) to 96 well plate (OS+)
    for well in plate_96.rows_by_name()['A'][6:]:
        pipette.transfer(100, dmso_high_glucose, well)

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in plate_96.rows_by_name()['A'][6:]:
        pipette.transfer(0.1, dex, well, mix_after=(3, 25))
        pipette.transfer(1, aa, well, mix_after=(3, 25))
        pipette.transfer(1, bgp, well, mix_after=(3, 25))

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in plate_96.rows_by_name()['A'][:6]:
        pipette.transfer(100, hMSC_cells, well, mix_after=(3, 50))

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in plate_96.rows_by_name()['A'][6:]:
        pipette.transfer(100, hMSC_cells, well, mix_after=(3, 50))

    pipette.drop_tip()
