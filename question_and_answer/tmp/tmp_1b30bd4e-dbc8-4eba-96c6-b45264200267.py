from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    
    dmem = protocol.load_labware('nest_12_reservoir_15ml', 3)['A1']
    dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', 4)['A1']
    dex = protocol.load_labware('nest_12_reservoir_15ml', 5)['A1']
    aa = protocol.load_labware('nest_12_reservoir_15ml', 6)['A1']
    bgp = protocol.load_labware('nest_12_reservoir_15ml', 7)['A1']
    hmsc = protocol.load_labware('nest_12_reservoir_15ml', 8)['A1']
    
    tiprack_1 = protocol.load_labware("opentrons_96_tiprack_300ul", 9)
    tiprack_2 = protocol.load_labware("opentrons_96_tiprack_300ul", 10)

    # Pipettes
    p50_multi = protocol.load_instrument('p50_multi', 'left', tip_racks=[tiprack_1, tiprack_2])

    # Transfer DMEM to OS- plate wells
    p50_multi.transfer(100, dmem, plate_96_os_minus.wells(), new_tip='always')

    # Transfer DMEM high glucose to OS+ plate wells
    p50_multi.transfer(100, dmem_high_glucose, plate_96_os_plus.wells(), new_tip='always')

    # Add supplements (Dex, AA, BGP) to OS+ plate wells
    for well in plate_96_os_plus.wells():
        p50_multi.transfer(0.1, dex, well, mix_after=(3, 50), new_tip='always')
        p50_multi.transfer(1, aa, well, mix_after=(3, 50), new_tip='always')
        p50_multi.transfer(1, bgp, well, mix_after=(3, 50), new_tip='always')

    # Transfer hMSC cells to OS- and OS+ plate wells
    hmsc_to_os_minus = p50_multi.transfer(100, hmsc, plate_96_os_minus.wells(), mix_after=(3, 50), new_tip='always')
    hmsc_to_os_plus = p50_multi.transfer(100, hmsc, plate_96_os_plus.wells(), mix_after=(3, 50), new_tip='always')
