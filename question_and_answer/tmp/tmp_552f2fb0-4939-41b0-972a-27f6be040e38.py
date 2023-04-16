from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Your Name',
    'description': 'Automation of hMSC spheroids experiment using Opentrons'
}

def run(protocol: protocol_api.ProtocolContext):

    # labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '4')
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '5')
    
    # reagents
    medium_dmem = reservoir.wells_by_name()['A1']
    medium_dmem_high_glucose = reservoir.wells_by_name()['A2']
    hmsc_cells = reservoir.wells_by_name()['A3']
    dex = reservoir.wells_by_name()['A4']
    aa = reservoir.wells_by_name()['A5']
    bgp = reservoir.wells_by_name()['A6']
    
    # pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Transfer medium to OS- wells
    p300.transfer(100, medium_dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer medium to OS+ wells
    p300.transfer(100, medium_dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add supplements to OS+ wells
    for well in plate_96_os_plus.wells():
        p20.transfer(0.1, dex, well, mix_after=(2, 10), new_tip='always')
        p20.transfer(1, aa, well, mix_after=(2, 10), new_tip='always')
        p20.transfer(1, bgp, well, mix_after=(2, 10), new_tip='always')

    # Transfer hMSC cells to OS- wells
    p300.transfer(100, hmsc_cells, plate_96_os_minus.wells(), mix_before=(2, 100), new_tip='always')

    # Transfer hMSC cells to OS+ wells
    p300.transfer(100, hmsc_cells, plate_96_os_plus.wells(), mix_before=(2, 100), new_tip='always')
