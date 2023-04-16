from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Opentrons',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    liquid_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '4')
    
    # Liquids
    dmem = liquid_reservoir.wells()[0]
    dmem_high_glucose = liquid_reservoir.wells()[1]
    dex = liquid_reservoir.wells()[2]
    aa = liquid_reservoir.wells()[3]
    bgp = liquid_reservoir.wells()[4]
    hmsc_cells = liquid_reservoir.wells()[5]

    # Pipettes
    p50_multi = protocol.load_instrument('p50_multi', 'left', tip_racks=[tiprack])
    
    # Experiment
    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add osteoinduction supplements to 96 well plate (OS+)
    p50_multi.transfer(0.1, dex, plate_96_os_plus.wells(), new_tip='always')
    p50_multi.transfer(1, aa, plate_96_os_plus.wells(), new_tip='always')
    p50_multi.transfer(1, bgp, plate_96_os_plus.wells(), new_tip='always')

    # Transfer hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, hmsc_cells, plate_96_os_minus.wells(), new_tip='always')

    # Transfer hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, hmsc_cells, plate_96_os_plus.wells(), new_tip='always')
