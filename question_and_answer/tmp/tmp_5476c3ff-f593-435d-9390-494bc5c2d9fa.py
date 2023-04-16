from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    waste_container = protocol.load_labware('nest_1_reservoir_90ml', '3')
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '4')
    
    # Pipette
    pipette = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack])
    
    # Antibody and cells
    antibody_well = eppendorf_rack['A1']
    cell_wells = plate.wells()

    # Immunostaining procedure
    pipette.pick_up_tip()
    for cell_well in cell_wells:
        # Aspirate antibody
        pipette.aspirate(1000, antibody_well)
        
        # Dispense antibody into cell well
        pipette.dispense(1000, cell_well)

        # Mix the antibody and cells
        pipette.mix(3, 1000, cell_well)
        
    # Dispose remaining liquid in waste
    pipette.dispense(1000, waste_container['A1'])
    pipette.drop_tip()
