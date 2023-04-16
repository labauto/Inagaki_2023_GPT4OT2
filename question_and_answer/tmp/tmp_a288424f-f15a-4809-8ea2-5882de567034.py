from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS Cell Immunostaining',
    'author': 'Your Name',
    'description': 'Automated immunostaining of E-Cadherin in iPS cells',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')

    # Pipette
    pipette = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack])

    # Reagents
    reagent_1 = reagent_reservoir.wells_by_name()['A1']
    reagent_2 = reagent_reservoir.wells_by_name()['A2']
    
    # iPS Cell Staining Procedure
    for i in range(1, 7):
        well = plate.wells_by_name()[f'A{i}']
        
        # Step 1: Aspirate reagent 1
        pipette.pick_up_tip()
        pipette.aspirate(1000, reagent_1)
        
        # Step 2: Dispense reagent 1 into well
        pipette.dispense(1000, well)
        pipette.blow_out() # Added blow_out step to help clear droplets from the tip

        # Step 3: Aspirate cells and remaining reagent 1 from well
        pipette.aspirate(2000, well)
        
        # Step 4: Dispense waste
        pipette.dispense(2000, reagent_reservoir['A12'].bottom()) # Replace "pipette.waste_container" with the designated waste well
        pipette.blow_out() # Added blow_out step to help clear droplets from the tip
        pipette.drop_tip()

        # Step 5: Aspirate reagent 2
        pipette.pick_up_tip()
        pipette.aspirate(1000, reagent_2)
        
        # Step 6: Dispense reagent 2 into well
        pipette.dispense(1000, well)
        pipette.blow_out() # Added blow_out step to help clear droplets from the tip
        
        # Step 7: Aspirate cells and remaining reagent 2 from well
        pipette.aspirate(2000, well)
        
        # Step 8: Dispense waste
        pipette.dispense(2000, reagent_reservoir['A12'].bottom()) # Replace "pipette.waste_container" with the designated waste well
        pipette.blow_out() # Added blow_out step to help clear droplets from the tip
        pipette.drop_tip()
