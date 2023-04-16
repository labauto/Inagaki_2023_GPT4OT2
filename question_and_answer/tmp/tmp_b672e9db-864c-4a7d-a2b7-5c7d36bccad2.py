from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'hMSC Spheroid Experiment'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    src_plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    src_plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    dest_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    
    # Pipettes
    p10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_10])
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_200])

    # Reagent Positions
    dmem_medium = src_plate_os_minus['A1']
    dmem_high_glucose_medium = src_plate_os_plus['A1']
    dex = src_plate_os_plus['B1']
    aa = src_plate_os_plus['C1']
    bgp = src_plate_os_plus['D1']
    hmsc = src_plate_os_minus['H1']

    # Transfer DMEM medium for OS(-)
    for well in dest_plate.wells():
        p300.transfer(100, dmem_medium, well, new_tip='always')
        
    # Transfer DMEM high glucose medium for OS(+)
    for well in dest_plate.wells():
        p300.transfer(100, dmem_high_glucose_medium, well, new_tip='always')

    # Add osteoinduction supplements for OS(+)
    for well in dest_plate.wells():
        p10.transfer(0.1, dex, well, mix_after=(3, 10), new_tip='always')
        p10.transfer(1, aa, well, mix_after=(3, 10), new_tip='always')
        p10.transfer(1, bgp, well, mix_after=(3, 10), new_tip='always')

    # Transfer hMSC cells for OS(-) and OS(+)
    for well in dest_plate.wells():
        p300.transfer(100, hmsc, well, mix_after=(3, 100), new_tip='always')
