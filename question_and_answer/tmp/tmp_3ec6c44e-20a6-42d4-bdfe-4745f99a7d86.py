from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Experiment',
    'author': 'Assistant',
    'description': 'A script to transfer hMSC cells and prepare well plates with and without osteoinduction supplements',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Define labware
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', 3)
    tiprack_300 = [protocol.load_labware('opentrons_96_tiprack_300ul', slot) for slot in [4, 5]]
    
    # Define pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tiprack_300)
    
    # Define reagents
    medium_dmem = reagent_reservoir.wells_by_name()['A1']
    medium_dmem_high_glucose = reagent_reservoir.wells_by_name()['A2']
    dexamethasone = reagent_reservoir.wells_by_name()['A3']
    ascorbic_acid = reagent_reservoir.wells_by_name()['A4']
    beta_glycerophosphate = reagent_reservoir.wells_by_name()['A5']
    hmsc_cells = reagent_reservoir.wells_by_name()['A6']
    
    def transfer_dmem_medium():
        for well in plate_os_minus.wells():
            p300.pick_up_tip()
            p300.aspirate(100, medium_dmem)
            p300.dispense(100, well)
            p300.drop_tip()
    
    def transfer_high_glucose_medium():
        for well in plate_os_plus.wells():
            p300.pick_up_tip()
            p300.aspirate(100, medium_dmem_high_glucose)
            p300.dispense(100, well)
            p300.drop_tip()
    
    def add_supplements():
        for well in plate_os_plus.wells():
            p300.pick_up_tip()
            p300.aspirate(0.1, dexamethasone)
            p300.aspirate(1, ascorbic_acid)
            p300.aspirate(1, beta_glycerophosphate)
            p300.dispense(2.1, well)
            p300.drop_tip()
    
    def transfer_hmsc_cells():
        for plate in [plate_os_minus, plate_os_plus]:
            for well in plate.wells():
                p300.pick_up_tip()
                p300.aspirate(100, hmsc_cells)
                p300.dispense(100, well)
                p300.drop_tip()
    
    # Perform the steps
    transfer_dmem_medium() # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    transfer_high_glucose_medium() # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    add_supplements() # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    transfer_hmsc_cells() # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS- and OS+)

