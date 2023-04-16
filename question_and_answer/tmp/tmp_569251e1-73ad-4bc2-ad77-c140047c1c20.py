from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '4')
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')

    # Reagents
    dmem = reservoir.wells()[0]
    dmem_high_glucose = reservoir.wells()[1]
    dex = reservoir.wells()[2]
    aa = reservoir.wells()[3]
    bgp = reservoir.wells()[4]
    hmsc = reservoir.wells()[5]

    # Pipette
    p50_multi = protocol.load_instrument('p50_multi', 'left', tip_racks=[tiprack_1, tiprack_2])

    # Steps
    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    p50_multi.transfer(0.1, dex, plate_96_os_plus.wells(), mix_after=(1, 5), new_tip='always')
    p50_multi.transfer(1, aa, plate_96_os_plus.wells(), mix_after=(1, 5), new_tip='always')
    p50_multi.transfer(1, bgp, plate_96_os_plus.wells(), mix_after=(1, 5), new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, hmsc, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, hmsc, plate_96_os_plus.wells(), new_tip='always')
