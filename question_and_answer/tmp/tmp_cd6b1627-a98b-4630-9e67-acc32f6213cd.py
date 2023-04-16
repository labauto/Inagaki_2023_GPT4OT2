from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Your Name <youremail@example.com>',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    p300_single = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '5')
    
    # Assign reagents
    pbs_minus = reservoir.wells_by_name()['A1']
    scm130 = reservoir.wells_by_name()['A2']
    
    # Protocol
    wells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
    
    for well in wells:
        # Remove medium from well
        p300_single.pick_up_tip()
        p300_single.transfer(1000, plate_6_wells.wells_by_name()[well].bottom(2), pbs_minus.top(), new_tip='never')
        p300_single.drop_tip()

        # Wash cells with PBS(-)
        p300_single.pick_up_tip()
        p300_single.transfer(1000, pbs_minus, plate_6_wells.wells_by_name()[well].bottom(2), new_tip='never')
        p300_single.transfer(1000, plate_6_wells.wells_by_name()[well].bottom(2), pbs_minus.top(), new_tip='never')
        p300_single.drop_tip()
        
        # Add SCM130
        p300_single.pick_up_tip()
        p300_single.transfer(1000, scm130, plate_6_wells.wells_by_name()[well].bottom(1), new_tip='never')
        p300_single.drop_tip()
