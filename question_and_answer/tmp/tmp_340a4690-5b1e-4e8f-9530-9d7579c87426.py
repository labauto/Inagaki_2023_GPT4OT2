from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Opentrons Helper',
    'description': 'Automating hMSC spheroids experiment with Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_200 = [protocol.load_labware('opentrons_96_filtertiprack_200ul', slot) for slot in [2, 3]]
    hMSC_well_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 4)
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)
    reagent_tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tips_200)

    # Reagents
    DMEM_medium = reagent_tube_rack.wells_by_name()['A1']
    DMEM_high_glucose_medium = reagent_tube_rack.wells_by_name()['B1']
    hMSC_cells = reagent_tube_rack.wells_by_name()['C1']
    Dex = reagent_tube_rack.wells_by_name()['D1']
    AA = reagent_tube_rack.wells_by_name()['A2']
    BGP = reagent_tube_rack.wells_by_name()['B2']

    # Functions for transferring
    def transfer_medium(source, dest_plate):
        for well in dest_plate.wells():
            p300.pick_up_tip()
            p300.aspirate(100, source)
            p300.dispense(100, well)
            p300.drop_tip()

    def transfer_cells():
        for well in hMSC_well_plate.wells():
            p300.pick_up_tip()
            p300.aspirate(100, hMSC_cells)
            p300.dispense(100, well)
            p300.drop_tip()

    def add_supplements():
        for well in os_plus_plate.wells():
            p300.pick_up_tip()
            p300.aspirate(0.1, Dex)
            p300.aspirate(1, AA)
            p300.aspirate(1, BGP)
            p300.dispense(2.1, well)
            p300.drop_tip()

    # Step by step execution
    transfer_medium(DMEM_medium, os_minus_plate)  # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    transfer_medium(DMEM_high_glucose_medium, os_plus_plate)  # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    add_supplements()  # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    transfer_cells()  # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    transfer_cells()  # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)

