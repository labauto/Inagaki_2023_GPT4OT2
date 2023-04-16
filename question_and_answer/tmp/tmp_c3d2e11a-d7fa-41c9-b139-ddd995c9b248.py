from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) 
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 6)
    tube_rack_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    tip_rack1 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tip_rack2 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tip_rack1])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tip_rack2])

    # Initial stocks and concentrations
    stock_tg_tube_A1 = tube_rack_10.wells_by_name()['A1']
    stock_concs = [100 * 10**-6, 10 * 10**-6, 1 * 10**-6, 100 * 10**-9, 50 * 10**-9, 10 * 10**-9]

    for i, conc in enumerate(stock_concs, start=2):
        well = tube_rack_10.wells_by_name()[f'A{i}']
        p20.pick_up_tip()
        p20.transfer(35 * 10**-6, stock_tg_tube_A1, well)
        p20.aspirate(35 * 10**-6, well)
        p20.dispense(35 * 10**-6, well)
        p20.blow_out()
        p20.drop_tip()

    ################################################################################
    # Steps 3 to 9: preparation and addition of drug dilutions
    ################################################################################
    # Add cells to 1.5ml snap-capped tubes
    # NOTE: Manually perform this step for now, assumption is cells are in the tubes when the script starts

    # Code for steps 5 to 10 (skipping step 6)
    # Add 10nM to A6, then create a 2X working concentration by mixing 100uL of medium and 100uL of stock concentration
    stock_10nm_tube_A6 = tube_rack_10.wells_by_name()['A6']
    p200.pick_up_tip()
    p200.transfer(100 * 10**-6, stock_10nm_tube_A6, plate_96.wells_by_name()['A'])
    p200.mix(1, 200 * 10**-6, plate_96.wells_by_name()['A'])
    p200.blow_out()
    p200.drop_tip()

    ################################################################################
    # Steps 10 to 11: CellTox Green reagent addition
    ################################################################################
    celltox_green_reagent = tube_rack_10.wells_by_name()['B2']
    p20.pick_up_tip()
    for row in 'ABCDEFGH':
        for col in range(1, 5):
            well = plate_96.wells_by_name()[f'{row}{col}']
            p20.transfer(15 * 10**-6, celltox_green_reagent, well)
            p20.blow_out()
    p20.drop_tip()

    ################################################################################
    # Step 11: Heater Shaker orbital shaking at 500rpm for 2 minutes
    ################################################################################
    protocol.delay(minutes=2)

    ################################################################################
    # Step 14: Cell Titer Glo 2.0 reagent addition
    ################################################################################
    cell_titer_glo_reagent = tube_rack_10.wells_by_name()['B1']
    for col in range(1, 6):
        for row in 'ABCDEFGH':
            p200.pick_up_tip()
            p200.transfer(80 * 10**-6, cell_titer_glo_reagent, plate_96.wells_by_name()[f'{row}{col}'])
            p200.blow_out()
            p200.drop_tip()

    ################################################################################
    # Step 16: Heater Shaker orbital shaking at 500rpm for 2 minutes, incubate at RT for 10 minutes
    ################################################################################
    protocol.delay(minutes=2)
    protocol.delay(minutes=10)
