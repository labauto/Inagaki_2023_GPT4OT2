from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Cytotoxicity Assay with Thapsigargin',
    'author': 'Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tip_rack20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tip_rack200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack20])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack200])

    # Reagents
    cell_suspension = tube_rack.wells_by_name()['A6']
    initial_stock = [tube_rack.wells_by_name()[well] for well in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']]
    working_stock_4x = [tube_rack.wells_by_name()[well] for well in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']]
    F12K_medium = protocol.load_labware('nest_12_reservoir_15ml', 5)
    celltox_green_reagent = tube_rack.wells_by_name()['B2']
    celltiter_glo_reagent = tube_rack.wells_by_name()['B1']

    # Steps
    ## Step 1 (manual): Cell counting

    ## Step 2 (manual): Adjust cell volume

    ## Step 3: Dispense cell suspension
    for well in plate.wells()[:60]:
        p300.transfer(60, cell_suspension, well)

    ## Steps 4-8 (manual): Drug preparation

    ## Step 9: Add 2X thapsigargin to wells
    for stock_well, target_wells in zip(working_stock_4x, plate.columns()[3:13]):
        for target_well in target_wells:
            p300.transfer(100, stock_well, target_well.top())

    ## Steps 10-16 (manual): Assay execution

    # Step 17: Read luminescence
    # This step should be performed with the Biotek microplate reader, which is not controlled by the Opentrons script.
