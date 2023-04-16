from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):

    # Load the 6 well and 96 well plates
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8_ml_flat', '1')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    
    # Load the pipettes and set their volume limits
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '4')])
    p200 = protocol.load_instrument('p10_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_20ul', '3')])

    # Transfer 100 µl medium (DMEM) to each well of 96 well plate (OS-)
    p1000.pick_up_tip()
    for well in plate_96_well.rows()[0]:
        p1000.transfer(100, plate_6_well['A1'], well, new_tip='never')
    p1000.drop_tip()

    # Transfer 100 µl medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p1000.pick_up_tip()
    for well in plate_96_well.rows()[1]:
        p1000.transfer(100, plate_6_well['A1'], well, new_tip='never')
    p1000.drop_tip()

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in plate_96_well.rows()[1]:
        p200.pick_up_tip()
        p200.transfer(0.1, plate_6_well['B1'], well, new_tip='never')
        p200.transfer(1, plate_6_well['C1'], well, new_tip='never')
        p200.transfer(1, plate_6_well['D1'], well, new_tip='never')
        p200.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p1000.pick_up_tip()
    for well in plate_96_well.rows()[0]:
        p1000.transfer(100, plate_6_well['A2'], well, new_tip='never')
    p1000.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p1000.pick_up_tip()
    for well in plate_96_well.rows()[1]:
        p1000.transfer(100, plate_6_well['A2'], well, new_tip='never')
    p1000.drop_tip()
