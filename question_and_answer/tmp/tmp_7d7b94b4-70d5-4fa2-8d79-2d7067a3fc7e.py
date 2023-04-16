metadata = {
    'apiLevel': '2.0',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with Thapsigargin',
    'source': 'https://your_source_url.com'
}

from opentrons import protocol_api

# protocol run function. the part after the colon lets your editor know
# how to handle indentation


def run(protocol: protocol_api.ProtocolContext):
    # labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    dilution_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '5')
    tipracks_20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul', str(slot))
                   for slot in range(6, 11)]

    # pipettes
    p20_multi = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=tipracks_20)

    # reagents
    cells = tube_rack['A1']

    # Step 2. Seeding cells
    cell_volume = 60  # ul
    seeding_density = 8000  # cells per well
    initial_wells = {'A{}'.format(col): col for col in 'BCDEFGH'}
    for well, col in initial_wells.items():
        protocol.transfer(cells.bottom(0.5), plate.wells_by_name()[well].bottom(0.5),
                          seeding_density, new_tip='always')

    # Step 3. Dispense cells into tubes
    transfer_volume = 225  # ul
    tube_wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    for source, dest in zip(plate.wells(), [tube_rack.wells_by_name()[well] for well in tube_wells]):
        p20_multi.transfer(cell_volume, source.bottom(0.5), dest.top(), new_tip='always')

    # Step 4. Add medium to the negative control wells
    medium_well = 'A5'
    for well, col in initial_wells.items():
        if well != medium_well:
            protocol.transfer(10, cells.bottom(0.5), plate.wells_by_name()[well].bottom(0.5), new_tip='always')

    # Step 6. Add 1mM thapsigargin
    thap_wells = ['A1']
    thap_concentrations = [1000]
    for well, conc in zip(thap_wells, thap_concentrations):
        protocol.transfer(35, tube_rack.wells_by_name()[well].bottom(0.5), dilution_plate.wells_by_name()[well].bottom(0.5), new_tip='always')

    # Step 7. Prepare dilutions of thapsigargin
    stock_wells = ['A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    dilution_columns = ['C', 'D']
    dilution_rows = [str(i) for i in range(1, 7)]
    dilution_wells = [col + row for col in dilution_columns for row in dilution_rows]
    dilution_volumes = [125, 125, 125, 125, 125, 125, 62.5, 62.5, 62.5, 62.5, 62.5, 62.5, 31.25, 31.25, 31.25,
                        31.25, 31.25, 31.25, 15.62, 15.62, 15.62, 15.62, 15.62, 15.62]
    stock_concentrations = [100, 10, 1, 0.1, 0.01, 0.001]
    for vol, source, dest in zip(dilution_volumes, [tube_rack.wells_by_name()[well] for well in stock_wells], [dilution_plate.wells_by_name()[well].bottom(0.5) for well in dilution_wells]):
        p20_multi.transfer(vol, source.bottom(0.5), dest, new_tip='always')

    # Step 9. Add CellTox reagent and incubate
    plate_wells = ['A1', 'A2', 'A3', 'A4', 'D4', 'E4', 'F4']
    ctxw = dilution_plate.rows_by_name()['A'][:6]
    ctxr = dilution_plate.rows_by_name()['B'][:6]
    ctxwells = list(zip(ctxw, ctxr))
    ctreagent_volume = 15
    protocol.delay(minutes=20, msg='Incubating at room temperature.')
    for (l, r), well in zip(ctxwells, plate_wells):
        protocol.transfer(ctreagent_volume, l.bottom(0.5), plate.wells_by_name()[well].bottom(0.5), new_tip='always')
        protocol.transfer(ctreagent_volume, r.bottom(0.5), plate.wells_by_name()[well].bottom(0.5), new_tip='always')
        protocol.delay(minutes=15, msg='Incubating at room temperature.')
        p20_multi.transfer(25, plate.wells_by_name()[well].bottom(0.5), dilution_plate.wells_by_name()[well].bottom(0.5), new_tip='always')

    # Step 10. Read CellTox fluorescence
    protocol.delay(minutes=1, msg='Reading CellTox fluorescence.')
    protocol.set_plate_temperature(37)
    # Set the excitation and emission wavelengths for the Biotek reader
    # https://www.biotek.com/products/microplate-detectors/filter-based-microplate-readers/cytation-c5-cytation-3/cytation-3/
    p20_multi.home()
    p20_multi.absorbance_plate(plate, '485:20', 'excitation')
    p20_multi.absorbance_plate(plate, '520:20', 'emission')
    protocol.set_plate_temperature(ambient_temp)

    # Step 11. Add CellTiter Glo reagent and incubate
    ctg_wells = ['A1', 'A2', 'A3', 'A4', 'D4', 'E4', 'F4']
    ctg_volume = 80
    for well in ctg_wells:
        protocol.transfer(ctg_volume, tube_rack.wells_by_name()['A1'].bottom(0.5), plate.wells_by_name()[well].bottom(0.5), new_tip='always')
        protocol.delay(minutes=10, msg='Incubating at room temperature.')

    # Step 12. Read CellTiter Glo luminescence
    protocol.delay(minutes=5, msg='Reading CellTiter Glo luminescence.')
    protocol.set_plate_temperature(37)
    p20_multi.home()
    p20_multi luminescence_plate(plate)

    protocol.comment('Protocol complete.')


