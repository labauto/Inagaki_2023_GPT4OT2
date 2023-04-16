from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'Immunostaining iPS Cells',
    'author': 'Your Name',
    'description': 'Preparation of immunostained iPS cells to visualize lysosomes in a 6-well plate'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    trough = protocol.load_labware('agilent_1_reservoir_290ml', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    # Reagent Locations
    wash_buffer = trough['A1']
    primary_antibody = trough['A2']
    secondary_antibody = trough['A3']

    # Protocol Steps
    protocol.comment('Immunostaining iPS cells started')
    
    # Step 1: Rinse cells with wash buffer
    protocol.comment('Transferring wash buffer to 6-well plate')
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, wash_buffer)
        p300.dispense(200, well)
        p300.drop_tip()
        
    protocol.delay(minutes=5)
    protocol.comment('Wash buffer incubation completed. Moving on to primary antibody.')

    # Step 2: Incubate with primary antibody
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, primary_antibody)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.comment('Incubating with primary antibody for 1 hour.')
    protocol.delay(minutes=60)

    # Step 3: Rinse cells with wash buffer
    protocol.comment('Transferring wash buffer to 6-well plate after primary antibody')
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, wash_buffer)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.delay(minutes=5)
    protocol.comment('Wash buffer incubation completed. Moving on to secondary antibody.')

    # Step 4: Incubate with secondary antibody
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, secondary_antibody)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.comment('Incubating with secondary antibody for 1 hour.')
    protocol.delay(minutes=60)

    # Step 5: Rinse cells with wash buffer
    protocol.comment('Transferring wash buffer to 6-well plate after secondary antibody')
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, wash_buffer)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.comment('Immunostaining completed. Cells are ready for visualization.')
