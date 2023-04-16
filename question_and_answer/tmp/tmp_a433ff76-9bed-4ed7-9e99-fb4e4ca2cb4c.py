from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(ctx: protocol_api.ProtocolContext):
    # Labware
    plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    pbs_tube = ctx.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 2)
    dmem_tube = ctx.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 3)
    
    # Pipettes
    pipette = ctx.load_instrument('p300_single_gen2', 'right', tip_racks=[ctx.load_labware('opentrons_96_tiprack_300ul', 4)])
    
    # Procedure
    pbs_source = pbs_tube.wells_by_name()['A1']
    dmem_source = dmem_tube.wells_by_name()['A1']
    
    for well_name in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']:
        pipette.pick_up_tip()
        
        well = plate.wells_by_name()[well_name]
        # Aspirate the medium in the well
        pipette.aspirate(200, well)
        pipette.dispense(200, well)
        
        # Wash with PBS
        pipette.aspirate(200, pbs_source)
        pipette.dispense(200, well)
        
        # Aspirate PBS in the well
        pipette.aspirate(200, well)
        pipette.dispense(200, well)
        
        # Add fresh D-MEM
        pipette.aspirate(200, dmem_source)
        pipette.dispense(200, well)
        
        pipette.drop_tip()
