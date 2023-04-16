from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay',
    'author': 'Firstname Lastname',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter
    # at low fan speed for about an hour before seeding the cells
    # on 96 well plate. Continue to keep the HEPA filter turned on during
    # the duration of setting up the robot with the respective labware,
    # dilutions of the drug (thapsigargin) on the second day and addition
    # of the drug on to the 96 well plate

    # Add your code here to perform cleaning and setup

    # Step 1: Count cells in the T-75 flask
    # Take a 24–48 hours old T-75 flask of A549 cells.
    # Take a cell count using the automated Countess 3 machine (Thermofisher Scientific)
    # after treating the cells with Tryple Express enzyme and dislodging the adherent cells.
    count = count_cells()

    # Step 2: Seed cells
    seed_cells(count, protocol)

    # Step 3-8: Prepare thapsigargin dilutions and add to 96 well plate
    prepare_dilutions(protocol)

    # Step 9-17: Perform CellTox Green assay and Cell Titer Glo 2.0 assay
    perform_assays(protocol)


def count_cells():
    # Add code here to count cells
    count = 10000  # replace with actual cell count
    return count


def seed_cells(cell_count, protocol):
    # Step 2: Seed cells
    # 8000 cells are to be seeded in each well of the 96 well plate.
    # Adjust the cell volume in 10% Ham’s F12K medium in such a way that 60
    # microL of cells contain the cell number mentioned above.
    cell_volume = (cell_count / 8000) * 60
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    for i in range(1, 13):
        plate['A'+str(i)].transfer(cell_volume,
                                    plate['A'+str(i+12)],
                                    mix_after=(3, 5))


def prepare_dilutions(protocol):
    # Step 3-8: Prepare thapsigargin dilutions and add to 96 well plate
    stock_1mM = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '6')
    stock_1mM_tube = stock_1mM['A1']
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_cols = plate.columns()[1:7]
    plate_cols.append(plate.columns()[0])
    negative_ctrl = plate_cols[0][4:7]
    # Add negative control
    for well in negative_ctrl:
        well.transfer(30, protocol.load_labware('nest_1_reservoir_195ml', '2')['A1'], (0, 2), new_tip='always')

    drug_cols = [['A', '1uM'], ['B', '100nM'], ['C', 'no drugs (vehicle)']]
    for i in range(len(drug_cols)):
        dilution_vol = 25
        start_col = plate_cols[i*2]
        drug_vol_per_well = 5
        for tube, col in zip(stock_1mM_tube.get_children_list(), start_col):
            drug_vol = dilute_thapsigargin(tube, dilution_vol, protocol)
            col.transfer(drug_vol_per_well, protocol.load_labware('nest_1_reservoir_195ml', '2')['A2'],
                         (0, 2), new_tip='always')
            col.transfer(drug_vol + drug_vol_per_well, protocol.load_labware('nest_1_reservoir_195ml', '2')['A3'],
                         (0, 2), new_tip='always')

    # Add drug dilutions to 96 well plate
    for col, drug_col in zip(plate_cols, drug_cols):
        col_name, drug_conc = drug_col
        drug_vol = 10
        drug_conc = drug_conc.lower()
        if drug_conc == 'no drugs (vehicle)':
            for well in col:
                well.transfer(drug_vol, protocol.load_labware('nest_1_reservoir_195ml', '2')['A3'],
                              (0, 2), new_tip='always')
        else:
            for i, well in enumerate(col):
                row_name = 'ABCDEFGH'[i // 12]
                well.transfer(drug_vol, protocol.load_labware('nest_1_reservoir_195ml', '2')['A3'],
                              (0, 2), new_tip='always')
                well.transfer(drug_vol, protocol.load_labware('nest_1_reservoir_195ml', '2')[drug_conc],
                              (0, 2), new_tip='always')

                if row_name == 'D' and well.get_name() == drug_conc[0] + '4':
                    # For 2X dilution, first add the respective column of drug free
                    # medium and then dispense the drug at each concentration.
                    col = plate.columns()[1:7]
                    col.append(plate.columns()[0])
                    for dose, col in zip(['1/8', '1/4', '1/2', '1X', '2X'], col):
                        for well in col:
                            well.transfer(drug_vol, protocol.load_labware('nest_1_reservoir_195ml', '2')['A3'],
                                          (0, 2), new_tip='always')
                        if dose == '2X':
                            dose = drug_conc
                        for well in col:
                            if row_name != 'E' or well > col[2]:
                                well.transfer(drug_vol * int(dose[0]), protocol.load_labware('nest_1_reservoir_195ml', '2')[dose[1:]],
                                              (0, 2), new_tip='always')

    # Mix well after adding drug
    for col in plate_cols:
        for well in col:
            well.mix(3, 30)


def dilute_thapsigargin(tube, dilution_vol, protocol):
    dilute_vol = 225 - dilution_vol
    tube_contents_vol = tube.volume - 10  # leave 10 uL at the bottom of the tube
    ratio = dilute_vol / tube_contents_vol
    dilute_vol = round(dilute_vol, 1)
    ratio = round(ratio, 1)
    if ratio > 5:
        dilute_vol = 10
        ratio = round(dilution_vol / tube.volume, 1)

    vol_to_transfer = dilute_vol + 10
    if vol_to_transfer >= tube.volume:
        vol_to_transfer = tube.volume - 10

    diluted_tube = tube.parent.wells_by_name()[tube.get_name()+' Diluted']
    diluted_tube.transfer(dilute_vol, protocol.load_labware('nest_1_reservoir_195ml', '2')['A3'],
                           (0, 2), new_tip='always')
    tube.transfer(vol_to_transfer, diluted_tube, (0, 2), new_tip='always')
    diluted_tube.mix(3, 30)
    while tube.volume > 10:
        tube.transfer(2, protocol.load_labware('trash-box', '12')['A1'], new_tip='always')
    return round(dilution_vol / ratio, 1)


def perform_assays(protocol):
    # Add CellTox Green reagent
    cell_tox_green = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_conical', '10')
    cell_tox_green_tube = cell_tox_green['B2']
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')

    plate_cols = plate.columns()[0:6]
    for col in plate_cols:
        wells_to_add_reagent = col[0:4]
        for well in wells_to_add_reagent:
            well.transfer(15, cell_tox_green_tube, (0, 2), new_tip='always')

    # Process the plate
    shaker = protocol.load_module('shaker', '7')
    plate_w_shaker = shaker.load_labware('corning_96_wellplate_360ul_flat')

    plate_w_shaker.transfer(15, plate, plate_w_shaker.columns()[0][0:8], new_tip='always')

    # Shake for 2 minutes
    shakes = 0
    while shakes < 2:
        plate_w_shaker.set_temperature(ambient_temperature)
        plate_w_shaker.set_shake_position(1)
        plate_w_shaker.set_shake_frequency(500)
        plate_w_shaker.set_shake_amplitude(2)
        plate_w_shaker.start_shaking()
        protocol.delay(minutes=1)
        shakes += 1
        plate_w_shaker.stop_shaking()

    # Incubate the plate for 15 minutes
    protocol.delay(minutes=15)

    # Read fluorescence
    fluorescence_reader = protocol.load_module('fluorescence_reader', '8')
    fluorescence_plate = fluorescence_reader.load_labware('corning_96_wellplate_360ul_flat')

    # Transfer the contents of each well on the shaker to the fluorescence plate
    for well in plate_w_shaker.wells():
        destination_well = fluorescence_plate[wells.get_name()]
        destination_well.transfer(15, wells, (0, 2), new_tip='always')

    # Read the fluorescence
    fluorescence_reader.open


:*************************


