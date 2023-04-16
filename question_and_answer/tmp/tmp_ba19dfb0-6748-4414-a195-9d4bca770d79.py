from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tuberack_50ml = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Wells
    cell_culture_wells = ['A1', 'A2', 'A3']
    lysosome_stain_well = tuberack_50ml.wells_by_name()['A1']
    hmsc_stain_well = tuberack_50ml.wells_by_name()['A2']
    
    # Protocol
    for well in cell_culture_wells:
        # Aspirate lysosome solution
        p300.pick_up_tip()
        p300.aspirate(100, lysosome_stain_well)
        p300.dispense(100, six_well_plate.wells_by_name()[well])
        p300.blow_out()
        p300.drop_tip()
        
        # Aspirate hMSC solution
        p300.pick_up_tip()
        p300.aspirate(100, hmsc_stain_well)
        p300.dispense(100, six_well_plate.wells_by_name()[well])
        p300.blow_out()
        p300.drop_tip()
