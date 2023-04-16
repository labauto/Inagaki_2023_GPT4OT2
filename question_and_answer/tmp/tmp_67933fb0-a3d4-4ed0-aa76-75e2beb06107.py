from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining iPS Cells',
    'author': 'Your Name',
    'description': 'Automated immunostaining of iPS cells using Opentrons',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    trough = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', '3')
    
    # Pipettes
    pipette_200 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack_200])

    # Reagent Positions
    primary_antibody = trough['A1']
    secondary_antibody = trough['A2']
    wash_buffer = trough['A3']


    # Protocol steps
    # Step 1: Primary antibody
    for well in plate_6_well.wells():
        pipette_200.pick_up_tip()
        pipette_200.transfer(100, primary_antibody, well, new_tip='never')
        pipette_200.drop_tip()

    protocol.delay(minutes=60)

    # Step 2: Washing
    for _ in range(3):
        for well in plate_6_well.wells():
            pipette_200.pick_up_tip()
            pipette_200.transfer(200, wash_buffer, well, new_tip='never')
            pipette_200.drop_tip()

    # Step 3: Secondary antibody
    for well in plate_6_well.wells():
        pipette_200.pick_up_tip()
        pipette_200.transfer(100, secondary_antibody, well, new_tip='never')
        pipette_200.drop_tip()

    protocol.delay(minutes=60)

    # Step 4: Final wash
    for _ in range(3):
        for well in plate_6_well.wells():
            pipette_200.pick_up_tip()
            pipette_200.transfer(200, wash_buffer, well, new_tip='never')
            pipette_200.drop_tip()

