from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'hMSC Culture Medium Exchange Protocol',
    'author': 'Your Name <youremail@example.com>',
    'description': 'Protocol for exchanging hMSC cell culture medium using PBS(-) and D-MEM in a 6-well plate'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
   
    # Load the plate
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    
    # Load reagents
    pbs = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    dmem = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # Load tips
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])
    
    ### Start experimental procedures
    
    # Step 1: Exchange the culture medium with PBS(-)
    
    p300.pick_up_tip()
    
    # Aspirate PBS(-) from reservoir
    p300.aspirate(150, pbs['A1'])

    # Dispense PBS(-) into all 6 wells of the plate
    p300.dispense(150, plate.columns_by_name()['1'])
    p300.dispense(150, plate.columns_by_name()['2'])
    p300.dispense(150, plate.columns_by_name()['3'])
    p300.dispense(150, plate.columns_by_name()['4'])
    p300.dispense(150, plate.columns_by_name()['5'])
    p300.dispense(150, plate.columns_by_name()['6'])

    p300.drop_tip()

    # Step 2: Exchange PBS(-) with D-MEM.
    
    p300.pick_up_tip()
    
    # Aspirate D-MEM from reservoir
    p300.aspirate(150, dmem['A1'])

    # Dispense D-MEM into all 6 wells of the plate
    p300.dispense(150, plate.columns_by_name()['1'])
    p300.dispense(150, plate.columns_by_name()['2'])
    p300.dispense(150, plate.columns_by_name()['3'])
    p300.dispense(150, plate.columns_by_name()['4'])
    p300.dispense(150, plate.columns_by_name()['5'])
    p300.dispense(150, plate.columns_by_name()['6'])

    p300.drop_tip()

    protocol.comment("Protocol complete!")
