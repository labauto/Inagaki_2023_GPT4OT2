from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    lysosome_stain = protocol.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', '3')
    
    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    # Protocol
    starting_well = lysosome_stain['A1']
    
    wells_to_fill = ['A3', 'A4', 'B3', 'B4', 'C3', 'C4']
    
    for well_key in wells_to_fill:
        destination_well = well_plate[well_key]
        
        pipette.pick_up_tip()
        pipette.aspirate(100, starting_well)
        pipette.dispense(100, destination_well)
        pipette.drop_tip()
