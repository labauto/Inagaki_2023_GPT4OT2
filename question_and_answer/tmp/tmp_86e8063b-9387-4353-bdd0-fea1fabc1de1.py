from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    medium_dmem = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '4')
    medium_dmem_high = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '5')
    tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '6')

    # Pipettes
    p50 = protocol.load_instrument('p50_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '7')])
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '8')])

    # Reagents
    dmem = medium_dmem['A1']                         # DMEM in tube A1
    dmem_high = medium_dmem_high['A1']               # DMEM high glucose in tube A1
    dex = tuberack['A1']                             # Dexamethasone in tube A1
    aa = tuberack['A2']                              # Ascorbic acid in tube A2
    bgp = tuberack['A3']                             # beta-glycerophosphate in tube A3
    hmsc_os_minus = tuberack['A4']                   # hMSC cells for OS(-) in tube A4
    hmsc_os_plus = tuberack['A5']                    # hMSC cells for OS(+) in tube A5

    # Prepare OS(-) wells
    for well in plate_os_minus.wells():
        p300.transfer(100, dmem, well)

    # Prepare OS(+) wells
    for well in plate_os_plus.wells():
        p300.transfer(100, dmem_high, well)
        p50.transfer(0.1, dex, well)
        p50.transfer(1, aa, well)
        p50.transfer(1, bgp, well)

    # Transfer hMSC cells to OS(-) wells
    p50.pick_up_tip()
    for well in plate_os_minus.wells():
        p50.transfer(100, hmsc_os_minus, well, new_tip='never')
    p50.drop_tip()

    # Transfer hMSC cells to OS(+) wells
    p50.pick_up_tip()
    for well in plate_os_plus.wells():
        p50.transfer(100, hmsc_os_plus, well, new_tip='never')
    p50.drop_tip()
