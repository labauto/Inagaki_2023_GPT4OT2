from opentrons import protocol_api

metadata = {
    'apiLevel': '2.8',
    'protocolName': 'Prepare Immunostained iPS Cells',
    'description': 'Automate immunostaining processes for E-Cadherin visualization'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    reagent_tuberack = protocol.load_labware('opentrons_24_tuberack_nest_2ml_snapcap', '3')
    
    # Tip and waste containers
    tips = [tiprack.rows()[0][x] for x in range(3)]
    
    # Pipettes
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])
    
    # Reagents
    primary_antibody = reagent_tuberack['A1']
    secondary_antibody = reagent_tuberack['A2']    
    wash_buffer = reagent_tuberack['A3']

    # Staining protocol
    pipette.pick_up_tip(tips[0])

    for well in plate.wells():
        # Add primary antibody
        pipette.transfer(2000, primary_antibody, well, new_tip='never')
        
    pipette.drop_tip()
    protocol.delay(minutes=30)

    for well in plate.wells():
        # Wash 3 times
        for _ in range(3):
            pipette.pick_up_tip(tips[1])
            pipette.transfer(2000, wash_buffer, well, new_tip='never')
            pipette.drop_tip()
    
        # Add secondary antibody
        pipette.pick_up_tip(tips[2])
        pipette.transfer(2000, secondary_antibody, well, new_tip='never')
        
    pipette.drop_tip()
