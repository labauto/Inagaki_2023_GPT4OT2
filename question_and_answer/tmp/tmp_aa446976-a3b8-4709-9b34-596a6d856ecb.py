from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'A549 Thapsigargin Viability and Cytotoxicity Assay',
    'author': 'Your Name <yourname@yourinstitute.edu>',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin'
}

# Define custom labware
tip_racks_20ul = [
    labware.load('opentrons_96_tiprack_20ul', str(slot))
    for slot in range(1, 4)
]

tube_rack_15ml = labware.load('tube-rack-15_50ml', '6')

# Define custom pipettes
p20 = instruments.P20_Single(
    mount='right',
    tip_racks=tip_racks_20ul
)

# Define custom reagents
cell_tox_green = tube_rack_15ml.wells()[1]
cell_titer_glo = tube_rack_15ml.wells()[0]

# Define locations of negative control wells in the plate
negative_control_wells = ['A5', 'B5', 'C5']

# Define dilution scheme for thapsigargin concentrations
initial_concentrations = [100_000, 10_000, 1_000, 100, 10, 1]  # nM
dilution_factors = [1, 2, 4, 8, 16, 32]

# Define main function that runs the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Set up the robot
    robot.home()
    plate = labware.load('corning_96_wellplate_360ul_flat', '5')
    incubator = modules.load('tempdeck', '7')
    incubator.set_temperature(37)
    incubator.wait_for_temp()
    plate_on_deck = incubator.load_labware('corning_96_wellplate_360ul_flat')
    p20.flow_rate.aspirate = 10
    p20.flow_rate.dispense = 10

    # Step 1: Cell seeding and initial drug additions
    cell_to_seed = 8000
    cells_needed = (cell_to_seed / 60) * 1000
    p20.pick_up_tip()
    p20.transfer(cells_needed,
                 cell_dilution_mix,
                 [well.top() for well in plate.columns()],
                 new_tip='never')
    p20.drop_tip()

    # Prepare negative control wells
    for well in negative_control_wells:
        p20.transfer(60, media, plate[well].top())

    # Prepare drug solutions
    all_concentrations = initial_concentrations + [x * y for x in initial_concentrations for y in dilution_factors]
    all_tubes = tube_rack_15ml.rows()[0][:7]
    initial_stock = all_tubes[0]
    desired_volumes = [12500, 1250, 125, 12.5, 1.25, 0.125]
    p20.transfer(35, initial_stock, all_tubes[1], mix_after=(3, 20))
    for concentration, tube, volume in zip(all_concentrations, all_tubes[1:], desired_volumes):
        p20.transfer(volume, media, tube)
        p20.transfer(12500, tube, all_tubes[1+all_concentrations.index(concentration) // 6], mix_after=(3, 20))
    
    # Prepare 2x drug dilutions
    concentrate_wells = plate.rows_by_name()['C'] + plate.rows_by_name()['D']
    for conc_well, drug_tube in zip(concentrate_wells, all_tubes[1:]):
        p20.transfer(100, media, conc_well)
        p20.transfer(100, drug_tube, conc_well, mix_after=(3, 20))
    
    # Add drugs to cells
    cols_to_fill = [plate.columns_by_name()[col_name] for col_name in ['A', 'B', 'C', 'D', 'E', 'F']]
    drug_wells = all_tubes[1:]
    drug_concentrations = [concentration for concentration in all_concentrations if concentration < 2000]
    for drug_concentration, drug_row, col_to_fill in zip(drug_concentrations, drug_wells, cols_to_fill):
        for col in col_to_fill:
            p20.transfer(60, conc_well, col)

    # Step 2: Cell viability measurements
    p20.pick_up_tip()
    for well in plate.wells():
        if well not in negative_control_wells:
            p20.transfer(15, cell_tox_green, well, new_tip='never')
    p20.drop_tip()
    protocol.delay(minutes=2)
    incubator.start_orbital_shaking(500)
    protocol.delay(minutes=15)
    incubator.stop_shaking()
    for well in plate.wells():
        if well not in negative_control_wells:
            protocol.light_absorbance(
                cell_tox_green,
                well,
                wavelength=485,
                incubate_secs=0,
                read_secs=3
            )

    # Step 3: Cell viability measurements
    p20.pick_up_tip()
    for well in plate.wells():
        if well not in negative_control_wells:
            p20.transfer(80, cell_titer_glo, well, new_tip='never')
    p20.drop_tip()
    protocol.delay(minutes=10)
    incubator.start_orbital_shaking(500)
    protocol.delay(minutes=2)
    incubator.stop_shaking()
    for well in plate.wells():
        if well not in negative_control_wells:
            protocol.measure_luminescence(cell_titer_glo, well)

