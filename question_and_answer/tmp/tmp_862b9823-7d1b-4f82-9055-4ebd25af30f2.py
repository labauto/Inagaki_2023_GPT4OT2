from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.4',
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'FirstName LastName <email@example.com>',
    'description': 'A protocol to measure cell viability and cytotoxicity of A549 cells treated with thapsigargin.',
}

# protocol run function. The part after the colon lets your editor know
# what type of variable is `protocol`.
def run(protocol: protocol_api.ProtocolContext):
    
    # labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', '2')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '4')

    # pipettes
    p10 = protocol.load_instrument('p10_single', mount='right', tip_racks=[tiprack_10])
    p200 = protocol.load_instrument('p300_single', mount='left', tip_racks=[tiprack_200])

    # reagents and cells
    cell_count = 8000
    cell_volume = 60
    countess = tube_rack.wells_by_name()['A1']
    neg_ctrl_wells = plate.rows_by_name()['A'][4:7]

    # Step 1 - Take a cell count
    countess.on_block = True
    p200.pick_up_tip()
    p200.transfer(100, countess, countess.buffer_well, new_tip='never')
    p200.drop_tip()
    countess.on_block = False

    # Step 2 - Seed cells in the plate
    p10.pick_up_tip()
    p10.transfer(cell_count, countess.buffer_well, plate.columns_by_name()['1'], new_tip='never')
    p10.drop_tip()

    # Step 3 - Dispense cell suspension into tubes and negative controls on the plate
    p200.pick_up_tip()
    for tube in tube_rack.wells()[:10]:
        p200.aspirate(cell_volume, plate.columns_by_name()['1'])
        p200.dispense(cell_volume, tube)
    p200.drop_tip()

    # Step 4 - Add media to the negative control wells
    p200.pick_up_tip()
    p200.distribute(60, countess.buffer_well, neg_ctrl_wells, new_tip='always')
    p200.drop_tip()

    # Step 5 - Wait for 12-16 hours

    # Step 6 - Add the initial concentration of thapsigargin
    thapsigargin_stock = tube_rack.wells_by_name()['A1']
    p10.pick_up_tip()
    p10.aspirate(35, thapsigargin_stock)
    p10.touch_tip()
    p10.dispense(35, tube_rack.wells_by_name()['C1'])
    p10.mix(5, 10)
    p10.blow_out(tube_rack.wells_by_name()['C1'].top())
    p10.drop_tip()

    # Step 7 - Prepare dilutions of thapsigargin
    thapsigargin_stocks = tube_rack.wells_by_name()
    thapsigargin_concentrations = [
        '100µM', '10µM', '1µM', '100nM', '50nM', '10nM',
        '1.56nM', '3.12nM', '6.24nM', '12.52nM', '25nM', '50nM',
    ]
    for conc, source, dests in zip(thapsigargin_concentrations, thapsigargin_stocks['A2':'D6'], tube_rack.rows()[1:]):
        p10.pick_up_tip()
        p10.transfer(35, source, dests, new_tip='never')
        p10.mix(5, 10)
        p10.blow_out(dests.top())
        p10.drop_tip()

    # Step 8 - Create 2X and 1X dilutions of thapsigargin and add to the plate
    thapsigargin_concentrations = thapsigargin_stocks.values()
    diluent = countess.buffer_well
    for conc, source, dests in zip(thapsigargin_concentrations, tube_rack.columns()[2:], plate.columns()[3:]):
        p200.pick_up_tip()
        p200.aspirate(100, diluent)
        p200.dispense(100, dests[0])
        p200.aspirate(100, source)
        p200.dispense(100, dests)
        p200.mix(5, 50)
        for well in dests:
            p200.aspirate(100, well.top())
            p200.dispense(100, well)
        p200.drop_tip()

    # Step 9 - Wait for 72 hours

    # Step 10 - Add CellTox Green reagent
    cell_tox = tube_rack.wells_by_name()['B2']
    p10.pick_up_tip()
    for col in plate.columns():
        p10.transfer(15, cell_tox, col, new_tip='never')
    p10.drop_tip()

    # Step 11 - Shake plate
    protocol.set_plate_temperature(25)
    protocol.set_plate_shaker('slow', 500)
    protocol.delay(minutes=2)
    protocol.set_plate_shaker(None)
    
    # Step 12 - Incubate plate
    protocol.delay(minutes=15)

    # Step 13 - Read fluorescence signal
    reader = protocol.embedded_instrument('biotek_elx808', mount='3')
    reader.set_excitation(485)
    reader.set_emission(520)
    for col in plate.columns():
        reader.pick_up_tip()
        reader.aspirate(100, col)
        reader.dispense(100, col)
        reader.drop_tip()

    # Step 14 - Shake plate
    protocol.set_plate_shaker('slow', 500)
    protocol.delay(minutes=2)

    # Step 15 - Add CellTiter-Glo 2.0 reagent
    cell_titer_glo = tube_rack.wells_by_name()['B1']
    p200.pick_up_tip()
    for col in plate.columns():
        p200.transfer(80, cell_titer_glo, col, new_tip='never')
    p200.drop_tip()

    # Step 16 - Shake plate
    protocol.set_plate_shaker(None)
    protocol.set_plate_temperature(25)
    protocol.set_plate_shaker('slow', 500)
    protocol.delay(minutes=2)

    # Step 17 - Read luminescence signal
    for col in plate.columns():
        reader.pick_up_tip()
        reader.aspirate(100, col)
        reader.dispense(100, col)
        reader.drop_tip()
