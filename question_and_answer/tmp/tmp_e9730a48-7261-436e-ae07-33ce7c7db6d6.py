from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul', '6')
    dmem = protocol.load_labware('nest_12_reservoir_15ml', '4').wells()[0]
    dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '4').wells()[1]
    dmso = protocol.load_labware('nest_12_reservoir_15ml', '5')
    cells = protocol.load_labware('nest_12_reservoir_15ml', '5').wells()[0]

    # Reagents
    dex = dmso.wells()[0]
    aa = dmso.wells()[1]
    bgp = dmso.wells()[2]

    # Pipette
    p50_multi = protocol.load_instrument('p50_multi', 'left', tip_racks=[tiprack, tiprack2])

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    p50_multi.transfer(0.1, dex, plate_96_os_plus.wells(), mix_after=(3, 20), new_tip='always')
    p50_multi.transfer(1, aa, plate_96_os_plus.wells(), mix_after=(3, 20), new_tip='always')
    p50_multi.transfer(1, bgp, plate_96_os_plus.wells(), mix_after=(3, 20), new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p50_multi.transfer(100, cells, plate_96_os_minus.wells(), new_tip='always')

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p50_multi.transfer(100, cells, plate_96_os_plus.wells(), new_tip='always')

    # End
