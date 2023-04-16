from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    pipette = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tips_1000])
    
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '11')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '12')
    supplements = protocol.load_labware('nest_12_reservoir_15ml', '9')
    hmsc_cells = protocol.load_labware('nest_12_reservoir_15ml', '10')

    # Step 1: Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    pipette.pick_up_tip()
    wells_os_minus = os_minus_plate.wells()
    for well in wells_os_minus:
        pipette.aspirate(100, medium_dmem.wells()[0])
        pipette.dispense(100, well)
    pipette.drop_tip()

    # Step 2: Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    pipette.pick_up_tip()
    wells_os_plus = os_plus_plate.wells()
    for well in wells_os_plus:
        pipette.aspirate(100, medium_dmem_high_glucose.wells()[0])
        pipette.dispense(100, well)
    pipette.drop_tip()

    # Step 3: Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    supplements_wells = supplements.wells()
    for well in wells_os_plus:
        pipette.pick_up_tip()
        
        pipette.aspirate(0.1, supplements_wells[0])  # Dex
        pipette.dispense(0.1, well)

        pipette.aspirate(1, supplements_wells[1])  # AA
        pipette.dispense(1, well)

        pipette.aspirate(1, supplements_wells[2])  # BGP
        pipette.dispense(1, well)
        
        pipette.drop_tip()

    # Step 4: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    pipette.pick_up_tip()
    for well in wells_os_minus:
        pipette.aspirate(100, hmsc_cells.wells()[0])
        pipette.dispense(100, well)
    pipette.drop_tip()

    # Step 5: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    pipette.pick_up_tip()
    for well in wells_os_plus:
        pipette.aspirate(100, hmsc_cells.wells()[0])
        pipette.dispense(100, well)
    pipette.drop_tip()

    # End
