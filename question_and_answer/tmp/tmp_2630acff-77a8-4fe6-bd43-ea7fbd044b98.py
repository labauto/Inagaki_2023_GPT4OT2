from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.11'
}

# Protocol
def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    p1000_rack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    source_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3') # Cell culture plate
    buffer_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '4') # reservoir for PBS(-) and D-MEM
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[p1000_rack])

    # Reagents
    pbs_minus = buffer_reservoir.wells_by_name()['A1'] # PBS(-)
    d_mem = buffer_reservoir.wells_by_name()['A2'] # D-MEM

    # Protocol steps
    # Step 1: Remove cell culture medium
    for well in source_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, well, p1000.trash_container.top(), air_gap=100, new_tip='never')
        p1000.drop_tip()

    # Step 2: Washing the cells with PBS(-)
    for well in source_plate.wells():
        p300.pick_up_tip()
        p300.transfer(200, pbs_minus, well, new_tip='never', mix_before=(3, 200))
        p300.drop_tip()

    # Step 3: Repeat washing with PBS(-)
    for well in source_plate.wells():
        p300.pick_up_tip()
        p300.transfer(200, pbs_minus, well, new_tip='never', mix_before=(3, 200))
        p300.drop_tip()

    # Step 4: Add D-MEM
    for well in source_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, d_mem, well, new_tip='never', mix_before=(3, 1000))
        p1000.drop_tip()

