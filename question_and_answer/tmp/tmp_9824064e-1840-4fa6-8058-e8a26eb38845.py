from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Immunostaining of hMSC cells - Lysosomes'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])

    # Wells
    hMSC_cells = plate_6_well.wells_by_name()['A1']
    primary_antibody = plate_6_well.wells_by_name()['B1']
    secondary_antibody = plate_6_well.wells_by_name()['C1']
    DAPI_stain = plate_6_well.wells_by_name()['D1']

    # Experiment steps
    # 1. Aspirate primary antibody
    p300.pick_up_tip()
    p300.aspirate(50, primary_antibody)
    
    # 2. Dispense primary antibody to hMSC cells
    p300.dispense(50, hMSC_cells)

    # 3. Incubate with primary antibody (1 hour)
    p300.drop_tip()
    protocol.delay(minutes=60)

    # 4. Aspirate secondary antibody
    p300.pick_up_tip()
    p300.aspirate(50, secondary_antibody)
    
    # 5. Dispense secondary antibody to hMSC cells
    p300.dispense(50, hMSC_cells)

    # 6. Incubate with secondary antibody (1 hour)
    p300.drop_tip()
    protocol.delay(minutes=60)

    # 7. Aspirate DAPI stain
    p300.pick_up_tip()
    p300.aspirate(50, DAPI_stain)
    
    # 8. Dispense DAPI stain to hMSC cells
    p300.dispense(50, hMSC_cells)

    # 9. Incubate with DAPI stain (30 minutes)
    p300.drop_tip()
    protocol.delay(minutes=30)

    # End of the experiment
