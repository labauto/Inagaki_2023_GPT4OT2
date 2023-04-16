from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Your Name',
    'description': 'Opentrons script for automating a biology experiment',
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    six_well_plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', 2)
    tip_rack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
    
    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tip_rack_1000])

    # Reagents
    PBS = tube_rack.wells_by_name()['A1']
    trypsin = tube_rack.wells_by_name()['A2']
    DMEM = tube_rack.wells_by_name()['A3']

    # Protocol Steps
    # Step 1: Wash with PBS(-)
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, PBS)
        for i in range(5):
            if i != 0:
                p1000.aspirate(800, well)
            p1000.dispense(800, well)
        p1000.drop_tip()
    
    # Step 2: Add trypsin solution and wait 5 minutes
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, trypsin, well, new_tip='never')
        p1000.drop_tip()

    protocol.delay(minutes=5)

    # Step 3: Add cell culture medium (DMEM)
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, DMEM, well, new_tip='never')
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment('Experiment complete.')
