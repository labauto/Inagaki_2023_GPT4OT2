from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining hMSC Cells',
    'author': 'Your Name',
    'description': 'Protocol for immunostaining of hMSC cells to visualize lysosomes in a 6-well plate.',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate_6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 3)

    # Load pipettes
    pipette_p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])
    
    # Reagents
    primary_antibody = tube_rack['A1']
    secondary_antibody = tube_rack['A2']
    wash_buffer = tube_rack['A3']

    # Variables
    incubation_time_primary = 60    # in minutes
    incubation_time_secondary = 60  # in minutes
    wash_steps = 3

    # Begin immunostaining process

    # Primary antibody incubation
    for well in plate_6well.wells():
        pipette_p300.pick_up_tip()
        pipette_p300.transfer(100, primary_antibody, well, mix_after=(3, 100), new_tip='never')
        pipette_p300.drop_tip()
    protocol.delay(minutes=incubation_time_primary)

    # Washing steps
    for _ in range(wash_steps):
        for well in plate_6well.wells():
            pipette_p300.pick_up_tip()
            pipette_p300.transfer(200, wash_buffer, well, mix_after=(3, 100), new_tip='never')
            pipette_p300.drop_tip()
    
    # Secondary antibody incubation
    for well in plate_6well.wells():
        pipette_p300.pick_up_tip()
        pipette_p300.transfer(100, secondary_antibody, well, mix_after=(3, 100), new_tip='never')
        pipette_p300.drop_tip()
    protocol.delay(minutes=incubation_time_secondary)

    # Final washing steps
    for _ in range(wash_steps):
        for well in plate_6well.wells():
            pipette_p300.pick_up_tip()
            pipette_p300.transfer(200, wash_buffer, well, mix_after=(3, 100), new_tip='never')
            pipette_p300.drop_tip()

    # Immunostaining process completed
