# Import Opentrons modules
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'MSC spheroids',
    'author': 'Your Name',
    'description': 'Culturing hMSC cells (2500 cells/100 µl) with DMEM in 6 well plates, and making hMSC spheroids in 96 well plates with two different conditions',
    'apiLevel': '2.1'
}

# protocol run function, the "protocol" parameter maybe of different type. Check OpenTrons API documentation.
def run(protocol: protocol_api.ProtocolContext):
    
    # Define labware
    plate6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    plate96well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    
    # Define pipettes
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '3')])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_20ul', '4')])
    
    # Define reagents, you should check if these are the correct wells
    dexamethasone = 'A1'
    ascorbic_acid = 'A2'
    beta_glycerophosphate = 'A3'
    
    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for i in plate96well.rows()[0][:6]:
        p1000.pick_up_tip()
        p1000.aspirate(100, plate6well['A1'])
        p1000.dispense(100, i)
        p1000.drop_tip()
    
    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for i in plate96well.rows()[0][6:]:
        p1000.pick_up_tip()
        p1000.aspirate(100, plate6well['A1'])
        p1000.dispense(100, i)
        p1000.drop_tip()
        
    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) 
    #to each well of 96 well plate (OS+)
    for i in plate96well.rows()[0][6:]:
        p20.pick_up_tip()
        p20.aspirate(0.1, plate96well[dexamethasone])
        p20.aspirate(1, plate96well[ascorbic_acid])
        p20.aspirate(1, plate96well[beta_glycerophosphate])
        p20.dispense(2.1, i)
        p20.drop_tip()
        
    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for i in plate96well.rows()[0][:6]:
        p1000.pick_up_tip()
        p1000.aspirate(100, plate6well['A2'])
        p1000.dispense(100, i)
        p1000.drop_tip()
    
    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for i in plate96well.rows()[0][6:]:
        p1000.pick_up_tip()
        p1000.aspirate(100, plate6well['A2'])
        p1000.dispense(100, i)
        p1000.drop_tip()
