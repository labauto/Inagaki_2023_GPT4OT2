from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Experiment',
    'author': 'Your Name <youremail@example.com>',
    'description': 'Creating hMSC spheroids with and without osteoinduction supplements',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    hmsc_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    dm_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    dmhg_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '7')
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '8')
    reagents = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '2')

    # Pipettes
    pipette20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # Reagents
    dm = reagents.wells_by_name()['A1']  # DMEM
    dmhg = reagents.wells_by_name()['A2']  # DMEM High Glucose
    dex = reagents.wells_by_name()['A3']  # Dexamethasone
    aa = reagents.wells_by_name()['A4']  # Ascorbic Acid
    bgp = reagents.wells_by_name()['A5']  # Beta-Glycerophosphate
    hmsc = reagents.wells_by_name()['A6']  # hMSC cells

    # Perform steps for experiment
    for well in range(96):
        # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
        pipette20.transfer(100, dm, dm_plate.wells()[well], new_tip='always')
        
        # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
        pipette20.transfer(100, dmhg, dmhg_plate.wells()[well], new_tip='always')

        # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
        pipette20.transfer(0.1, dex, dmhg_plate.wells()[well], new_tip='always')
        pipette20.transfer(1, aa, dmhg_plate.wells()[well], new_tip='always')
        pipette20.transfer(1, bgp, dmhg_plate.wells()[well], new_tip='always')

    for well in range(96):
        #Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
        pipette20.transfer(100, hmsc, dm_plate.wells()[well], new_tip='always')

        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
        pipette20.transfer(100, hmsc, dmhg_plate.wells()[well], new_tip='always')

