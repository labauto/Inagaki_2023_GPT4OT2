from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay with A549 cells using Opentrons',
    'author': 'Your Name',
    'description': 'Measuring viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'apiLevel': '2.11'
}

# defining constants
CELL_COUNT = 8000
CELL_VOLUME = 60
DRUG_VOLUMES = [35, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100]
DILUENT_VOLUMES = [215, 200, 200, 200, 200, 200, 100, 100, 100, 100, 100, 100]
THAP_CONCENTRATIONS = ['1mM', '100uM', '10uM', '1uM', '100nM', '50nM', '10nM']
THAP_DILUTIONS = [
    [1.56, 0.78, 0.39],
    [3.12, 1.56, 0.78],
    [6.24, 3.12, 1.56],
    [12.52, 6.24, 3.12],
    [25, 12.52, 6.24],
    [50, 25, 12.52],
    [100, 50, 25],
    [200, 100, 50],
    [400, 200, 100],
    [800, 400, 200],
    [1600, 800, 400],
    [2000, 1000, 500]
]

def pick_up_tip():
    pipette.pick_up_tip(tiprack.wells()[tip_count])
    if tip_count == len(tiprack.wells()) - 1:
        robot.pause("Replace tip rack")
    tip_count += 1

def seed_cells():
    for i in range(8):
        pipette.transfer(CELL_VOLUME, cell_suspension[i], plate.rows()[0][i+2])
    pipette.transfer(CELL_VOLUME, media, plate.rows()[0][:3])

def add_drug_concentrations():
    for i in range(7):
        pipette.transfer(DRUG_VOLUMES[i], thap_stocks[i], tube_rack.wells()[i])
    for i in range(12):
        thap_conc = THAP_CONCENTRATIONS[i // 3]
        dilution_factor = THAP_DILUTIONS[i][i % 3]
        pipette.transfer(DILUENT_VOLUMES[i], media, tube_rack.wells()[i])
        pipette.mix(3, 50, tube_rack.wells()[i])
        if dilution_factor != 1:
            pipette.transfer((DRUG_VOLUMES[i] * dilution_factor)/4, thap_stocks[THAP_CONCENTRATIONS.index(thap_conc)], tube_rack.wells()[i], mix_after=(3, 50))
            pipette.transfer((DRUG_VOLUMES[i] * dilution_factor)/4, tube_rack.wells()[i], tube_rack.wells()[i+1], mix_after=(3, 50))
            pipette.transfer((DRUG_VOLUMES[i] * dilution_factor)/2, tube_rack.wells()[i+1], tube_rack.wells()[i], mix_after=(3, 50))
        else:
            pipette.transfer(DRUG_VOLUMES[i]/4, thap_stocks[THAP_CONCENTRATIONS.index(thap_conc)], tube_rack.wells()[i], mix_after=(3, 50))
            pipette.transfer(DRUG_VOLUMES[i]/4, tube_rack.wells()[i], tube_rack.wells()[i+1], mix_after=(3, 50))
            pipette.transfer(DRUG_VOLUMES[i]/2, tube_rack.wells()[i+1], tube_rack.wells()[i], mix_after=(3, 50))

def add_thapsigargin_to_plate():
    col = 0
    for conc in THAP_CONCENTRATIONS:
        pipette.transfer(100, tube_rack.wells()[THAP_CONCENTRATIONS.index(conc) * 3], plate.rows()[0][col + 3:col + 6])
        col += 3

def add_celltox_green():
    for i in range(2, 9):
        pipette.transfer(15, celltox_green, plate.rows()[0][i])
    for i in range(1, 5):
        pipette.transfer(15, celltox_green, plate.rows()[i][1:9])

def add_cell_titer_glo():
    for i in range(9):
        pipette.transfer(80, cell_titer_glo, white_plate.rows()[0][i])
    for i in range(3):
        pipette.transfer(80, cell_titer_glo, white_plate.rows()[i+1][3:6])

def pause_experiment():
    robot.pause("Resume protocol after moving plate to room temperature for CellTox Green")

def measure_fluorescence():
    robot.comment("Measure fluorescence: Excitation 485nm, Emission 520nm")
    pause_experiment()

def measure_luminescence():
    robot.comment("Measure luminescence")
    robot.home()

def run(protocol: protocol_api.ProtocolContext):
    # load labware
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    plate = protocol.load_labware('greiner_96_wellplate_200ul', '3')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '4')
    cell_counter = protocol.load_labware('invitrogen_countess', '5')
    media_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '6')

    # load instruments
    pipette = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_10])

    # define reagents and samples
    thap_stocks = tube_rack.columns()[0]
    media = media_reservoir.wells()[0]
    cell_suspension = [cell_counter.wells()[i] for i in range(8)]
    cell_tox_green = tube_rack.wells()[11]
    cell_titer_glo = tube_rack.wells()[0]

    # starting tip count
    tip_count = 0

    # Step 1: Count cells and make cell suspension
    pick_up_tip()
    pipette.aspirate(20, cell_counter.wells()[0])
    pipette.dispense(20, cell_counter.wells()[0])
    pick_up_tip()
    pipette.transfer(20, cell_counter.wells()[1], cell_counter.wells()[2])
    robot.comment("Follow manufacturer instructions to count cells, dislodge and centrifuge the cells, and resuspend cells in Ham's F12K medium")
    robot.pause("Replace Countess 3 slide with tube rack containing cell suspension")
    pick_up_tip()
    seed_cells()
    robot.comment("Seeding cells to 96-well plate completed")

    # Step 2: Add thapsigargin
    robot.comment("Adding Thapsigargin")
    add_drug_concentrations()
    robot.comment("Dilutions preparation completed")
    add_thapsigargin_to_plate()
    robot.comment("Thapsigargin additions completed")

    # Step 3: CellTox Green Assay
    robot.comment("CellTox Green Assay")
    add_celltox_green()
    robot.comment("Incubating plate for 15 minutes at room temperature")
    protocol.delay(minutes=15)
    measure_fluorescence()

    # Step 4: Cell Titer Glo 2.0 Assay
    robot.comment("Cell Titer Glo 2.0 Assay")
    add_cell_titer_glo()
    robot.comment("Incubating plate for 10 minutes at room temperature")
    protocol.delay(minutes=10)
    measure_luminescence()
