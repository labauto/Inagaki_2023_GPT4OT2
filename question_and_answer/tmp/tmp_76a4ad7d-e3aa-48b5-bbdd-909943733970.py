from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Opentrons',
    'description': 'Automation of hMSC spheroids experiment',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    dmso_tube = protocol.load_labware('<replace_with_correct_labware_name>', location='1')
    os_plus_tube = protocol.load_labware('<replace_with_correct_labware_name>', location='5')
    os_minus_tube = protocol.load_labware('<replace_with_correct_labware_name>', location='2')
    hmsc_cells = protocol.load_labware('<replace_with_correct_labware_name>', location='3')
    dex_aa_bgp = protocol.load_labware('<replace_with_correct_labware_name>', location='4')

    # Load pipettes
    p_20 = protocol.load_instrument('p20_single_gen2', 'left')
    p_100 = protocol.load_instrument('p1000_single_gen2', 'right')

    # Step 1: Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for well in os_minus_tube.wells():
        p_100.transfer(100, dmso_tube.wells()[0], well)

    # Step 2: Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for well in os_plus_tube.wells():
        p_100.transfer(100, dmso_tube.wells()[1], well)

    # Step 3: Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in os_plus_tube.wells():
        p_20.transfer(0.1, dex_aa_bgp.wells()[0], well)
        p_20.transfer(1, dex_aa_bgp.wells()[1], well)
        p_20.transfer(1, dex_aa_bgp.wells()[2], well)

    # Step 4: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in os_minus_tube.wells():
        p_100.transfer(100, hmsc_cells.wells()[0], well)

    # Step 5: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in os_plus_tube.wells():
        p_100.transfer(100, hmsc_cells.wells()[0], well)
