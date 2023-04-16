# Importing the required modules
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'hMSC spheroids',
    'author': 'Your Name Here',
    'description': 'Protocol to culture hMSC cells with DMEM in 6 well plates, and to make hMSC spheroids in 96 well plates with or without the osteoinduction supplements',
    'apiLevel': '2.8'
}

# Protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # Declare labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')

    # Declare pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '4')])

    # Scale up each transfer step for demonstration purposes
    scale_factor = 10

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p300.pick_up_tip()
    for i in range(96):
        p300.transfer(100/scale_factor, reservoir.wells()[0], plate_96_well.wells()[i])
    p300.drop_tip()

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    p300.pick_up_tip()
    for i in range(96):
        p300.transfer(100/scale_factor, reservoir.wells()[1], plate_96_well.wells()[i])
    p300.drop_tip()

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    p10 = protocol.load_instrument('p10_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_10ul', '5')])

    p10.pick_up_tip()
    for i in range(96):
        p10.transfer(0.1/scale_factor, reservoir.wells()[2], plate_96_well.wells()[i], new_tip='never')
        p10.transfer(1/scale_factor, reservoir.wells()[3], plate_96_well.wells()[i], new_tip='never')
        p10.transfer(1/scale_factor, reservoir.wells()[4], plate_96_well.wells()[i], new_tip='never')
    p10.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    p300.pick_up_tip()
    for i in range(96):
        p300.transfer(2.5/scale_factor, plate_6_well.wells()[0], plate_96_well.wells()[i])
    p300.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p300.pick_up_tip()
    for i in range(96):
        p300.transfer(2.5/scale_factor, plate_6_well.wells()[0], plate_96_well.wells()[i+96])
    p300.drop_tip()

    # End
