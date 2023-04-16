from opentrons import simulate, protocol_api

# Set up the Opentrons API and robot simulation
protocol = protocol_api.ProtocolContext()
robot = simulate.SimulatingContext()

# Define labware
plate_96_well = robot.load_labware('corning_96_wellplate_360ul_flat', '1')
rack_15_mL = robot.load_labware('opentrons_15_tuberack_nest_15ml_conical', '6')
rack_1_5_mL = robot.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '7')

# Define pipettes
pipette_10ul = protocol.load_instrument('p10_single', 'left', tip_racks=[robot.get_tip_rack('opentrons_96_tiprack_10ul')], aspirate_flow_rate=10, dispense_flow_rate=10)
pipette_100ul = protocol.load_instrument('p100_single', 'right', tip_racks=[robot.get_tip_rack('tiprack-1000ul')], aspirate_flow_rate=100, dispense_flow_rate=100)

# Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter
protocol.comment('Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter')
robot.pause('Clean the robot and press Resume')

# Take a cell count using the automated Countess 3 machine
protocol.comment('Take a cell count using the automated Countess 3 machine')
robot.pause('Count the cells and press Resume')

# Seed cells in the 96 well plate
protocol.comment('Seed cells in the 96 well plate')
cells_per_well = 8000
cell_vol_per_well = 60
num_wells = plate_96_well.well_count
cell_suspension = rack_1_5_mL.wells()[0]
neg_control_wells = plate_96_well.rows()[4][:3]
for well_num in range(num_wells):
    well = plate_96_well.wells()[well_num]
    if well not in neg_control_wells:
        pipette_100ul.transfer(cell_vol_per_well, cell_suspension, well)
        protocol.comment(f"Seeded {cells_per_well} cells in well {well_num}.")
    else:
        pipette_100ul.transfer(cell_vol_per_well, None, well)
        protocol.comment(f"Added medium in negative control well {well_num}.")
robot.pause('Check the plate before continuing')

# Prepare dilutions of thapsigargin for drug treatment
protocol.comment('Prepare dilutions of thapsigargin for drug treatment')
thapsigargin_concs = {
    'A1': 1e-3,
    'A2': 1e-4,
    'A3': 1e-5,
    'A4': 1e-6,
    'A5': 1e-7,
    'A6': 5e-8,
    'B1': 1e-8,
}
diluent_vol = 75
drug_vol = 25
working_concs = {
    'C1': 1.56e-9,
    'C2': 3.12e-9,
    'C3': 6.24e-9,
    'C4': 12.52e-9,
    'C5': 2.5e-8,
    'C6': 5e-8,
    'D1': 1e-8,
    'D2': 2e-8,
    'D3': 4e-8,
    'D4': 8e-8,
    'D5': 1.6e-7,
    'D6': 2e-7,
}
drug_tubes = rack_1_5_mL.wells()[:7]
diluent_tubes = rack_1_5_mL.wells()[12:18]
for tube, conc in thapsigargin_concs.items():
    pipette_10ul.transfer(drug_vol, drug_tubes[0], rack_1_5_mL[tube])
    for i, diluent_tube in enumerate(diluent_tubes):
        dilution_conc = conc * 4**(i+1)
        pipette_10ul.transfer(diluent_vol, diluent_tube, rack_1_5_mL[tube])
        pipette_10ul.mix(4, 10, rack_1_5_mL[tube])
        pipette_10ul.transfer(drug_vol, rack_1_5_mL[tube], rack_1_5_mL[tube.next()])
        pipette_10ul.mix(4, 10, rack_1_5_mL[tube.next()])
robot.comment('Thapsigargin dilutions prepared. Check the tubes before continuing.')

# Prepare 2X working concentrations of the drug and add to plate
protocol.comment('Prepare 2X working concentrations of the drug and add to plate')
neg_control_wells = plate_96_well.rows()[4][:3]
drug_wells = plate_96_well.rows()[3]
for row_num, conc_tube in enumerate(diluent_tubes[::2]):
    for col_num, conc_well in enumerate(drug_wells[::2]):
        if conc_well not in neg_control_wells:
            source_tube = rack_1_5_mL['C' + str(row_num+1)]
            source_well = source_tube.wells()[col_num]
            drug_vol = 50
            diluent_vol = 50
            pipette_100ul.transfer(diluent_vol, None, conc_well)
            pipette_100ul.transfer(drug_vol, source_well, conc_well)
            pipette_100ul.mix(7, 50, conc_well)
            pipette_100ul.transfer(drug_vol, conc_well, conc_well.next())
            pipette_100ul.mix(7, 50, conc_well.next())
robot.pause('Check the plate before continuing')

# Add CellTox Green reagent to plate for cytotoxicity assay
protocol.comment('Add CellTox Green reagent to plate for cytotoxicity assay')
ctg_reagent = rack_15_mL['B2']
ctg_vol = 15
for row in plate_96_well.rows()[:4]:
    for well in row:
        if well not in neg_control_wells:
            pipette_10ul.transfer(ctg_vol, ctg_reagent, well)
robot.pause('Shake the plate for 2 minutes on the heater-shaker at 500 rpm, then incubate at RT for 15 min. Press Resume when ready to continue.')

# Read the fluorescence from the plate for the cytotoxicity assay
protocol.comment('Read the fluorescence from the plate for the cytotoxicity assay')
robot.pause('Read the fluorescence from the plate for the cytotoxicity assay and press Resume when ready to continue.')

# Add CellTiter-Glo 2.0 reagent to plate for viability assay
protocol.comment('Add CellTiter-Glo 2.0 reagent to plate for viability assay')
ctg_reagent = rack_15_mL['B1']
ctg_vol = 80
for row in plate_96_well.rows()[:4]:
    for well in row:
        if well not in neg_control_wells:
            pipette_100ul.transfer(ctg_vol, ctg_reagent, well)
robot.pause('Shake the plate for 2 minutes on the heater-shaker at 500 rpm, then incubate at RT for 10 min. Press Resume when ready to continue.')

# Read the luminescence from the plate for the viability assay
protocol.comment('Read the luminescence from the plate for the viability assay')
robot.pause('Read the luminescence from the plate for the viability assay and press Resume when done.')

protocol.comment('Experiment complete!')
