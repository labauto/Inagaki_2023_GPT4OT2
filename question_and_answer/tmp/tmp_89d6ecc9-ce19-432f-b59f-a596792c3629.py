from opentrons import protocol_api
from opentrons import labware, instruments

# Protocol constants
NUM_WELLS = 96
NUM_TUBES = 10

# Define labware
plate = labware.load('96-flat', '1')
tubes_rack = labware.load('opentrons-tuberack-2ml-screwcap', '6')
medium_tube_rack = labware.load('opentrons-tuberack-15_50ml', '9')
tip_rack_20ul = labware.load('opentrons-tiprack-20ul', '10')
tip_rack_200ul = labware.load('opentrons-tiprack-200ul', '11')

# Define instruments
m20 = instruments.P20_Multi(mount='right', tip_racks=[tip_rack_20ul])
m200 = instruments.P300_Multi(mount='left', tip_racks=[tip_rack_200ul])

# Define functions for each step

def seed_cells():
    # Step 2 - Seed 8000 cells in each well of the 96 well plate 
    cell_count = 8000
    cell_volume = 60  # microliters
    medium_volume = 140  # microliters
    for well in plate.wells():
        m20.pick_up_tip()
        m20.transfer(cell_volume, tubes_rack.wells('A1'), well, new_tip='never')
        m20.drop_tip()
        m200.transfer(medium_volume, medium_tube_rack.wells('A5'), well.top())

def add_drug():
    # Step 9 - Add drug to the wells 
    drug_volumes = [
        [31.5, 8.5], [31.5, 8.5], [31.5, 8.5], [31.5, 8.5], [31.5, 8.5], [31.5, 8.5], [31.5, 8.5],
        [8.5, 31.5], [8.5, 31.5], [8.5, 31.5], [8.5, 31.5], [8.5, 31.5], [8.5, 31.5], [8.5, 31.5],
        [0, 40], [40, 0], [0, 80], [80, 0], [0, 160], [160, 0], 
        [40, 40], [20, 80], [40, 80], [80, 80], [160, 80], [200, 80], 
        [80, 20], [80, 40], [80, 80], [80, 160], [80, 320], [80, 400]
    ]
    drug_concentrations = [
        '1mM', '100uM', '10uM', '1uM', '100nM', '50nM',
        '10nM', '1.56nM', '3.12nM', '6.24nM', '12.52nM', '25nM', '50nM',
        '0.39nM', '500nM']
    wells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
             'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
             'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
             'D4', 'E4', 'F4', 'D5', 'E5', 'F5', 'D6', 'E6', 'F6']
    for i, conc in enumerate(drug_concentrations):
        volumes = drug_volumes[i]
        for j, well in enumerate(wells):
            m20.pick_up_tip()
            m20.transfer(volumes[j], tubes_rack.wells(conc), plate.wells(well), new_tip='never')
            m20.drop_tip()

def add_CellToxGreen_reagent():
    # Step 10 - Add CellTox Green reagent to the wells
    celltoxgreen_volume = 15  # microliters
    for row in plate.rows():
        m20.pick_up_tip()
        for well in row:
            m20.transfer(celltoxgreen_volume, tubes_rack.wells('B2'),
                         well.bottom(), new_tip='never')
        m20.drop_tip()
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    m200.set_flow_rate(100)
    m200.delay(minutes=15)

def read_CellToxGreen():
    # Step 13 - Read the fluorescence at 485 nm excitation and 520 nm emission
    m200.set_flow_rate(50)
    m200.transfer(25, plate.rows()[0][:3], plate.rows()[1][:3])
    m200.set_flow_rate(100)
    for well in plate.rows()[1]:
        m200.pick_up_tip()
        m200.mix(3, 100, well)
        m200.touch_tip()
        m200.air_gap(10)
        m200.drop_tip()

def add_CellTiterGlo_reagent():
    # Step 15 - Add CellTiter Glo 2.0 reagent to the wells
    celtiterglo_volume = 80  # microliters
    for row in plate.rows():
        m200.pick_up_tip()
        for well in row:
            m200.transfer(celtiterglo_volume, tubes_rack.wells('B1'), well.bottom(), new_tip='never')
        m200.drop_tip()
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    m200.set_flow_rate(100)
    m200.delay(minutes=10)

def read_CellTiterGlo():
    # Step 17 - Read the luminescence measurement of cells using a microplate reader
    for well in plate:
        m200.pick_up_tip()
        m200.transfer(100, well, well.top(), new_tip='never')
        m200.drop_tip()

# Define the main function that runs the experiment - this will call each step function in turn

def run(protocol: protocol_api.ProtocolContext):
    # Step 1 - Take a count of cells
    cell_count = count_cells(m200)

    # Step 2 - Seed cells
    seed_cells()

    # Step 4 - Add medium to negative control wells
    negative_ctrl_wells = plate.rows_by_name()['A'][4:6]
    for well in negative_ctrl_wells:
        m200.transfer(140, medium_tube_rack.wells('A5'), well.top())

    # Step 9 - Add drug to the wells
    add_drug()

    # Step 10 - Add CellTox Green reagent to the wells
    add_CellToxGreen_reagent()

    # Step 11-12 - Shake and incubate the reagent
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    m200.set_flow_rate(100)
    m200.delay(minutes=2)
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    
    # Step 13 - Read the fluorescence at 485 nm excitation and 520 nm emission
    read_CellToxGreen()

    # Step 14 - Put plate back on shaker and prepare for CellTiterGlo
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    m200.set_flow_rate(100)

    # Step 15 - Add CellTiter Glo 2.0 reagent to the wells
    add_CellTiterGlo_reagent()

    # Step 16 - Shake and incubate the reagent
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)
    m200.set_flow_rate(100)
    m200.delay(minutes=2)
    m200.set_flow_rate(50)
    m200.mix(3, 200, plate)

    # Step 17 - Read the luminescence measurement of cells using a microplate reader
    read_CellTiterGlo()

