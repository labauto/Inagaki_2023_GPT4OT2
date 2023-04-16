# Import necessary modules
from opentrons import labware, instruments, protocol_api

# metadata
metadata = {
    'protocolName': 'A549 Cell Line Viability and Cytotoxicity Measurement with Thapsigargin',
    'author': 'Your Name Here',
    'description': 'Experiment to measure viability and cytotoxicity of A549 cells treated with Thapsigargin using OpenTrons robot',
    'apiLevel': '2.11'
}

# Define the protocol run function
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    tips = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    well_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_snapcap', '3')

    # Define pipettes
    p10 = protocol.load_instrument('p10_single', 'left', tip_racks=[tips])

    # Define cells seeding
    cells_to_seed = 8000
    cell_volume = 6  # Volume of cells containing cells_to_seed cells
    cell_plate_wells = well_plate.wells()[:4]
    cell_tube = tuberack.wells()[0]

    # Define negative control
    neg_ctrl_wells = well_plate.wells()[:3]
    neg_ctrl_wells_A1_C5 = well_plate.rows('A') + well_plate.columns('5')

    # Define pipetting volumes for drug dilution
    diluent_vol = 225
    drug_vol = 25
    mix_vol = 5

    # Define other volumes
    CellTox_vol = 15
    CellTiter_vol = 80

    # Define tube locations
    dil_stock_tubes = tuberack.rows_by_name()['A'][1:8]
    dil_working_tubes = tuberack.rows_by_name()['C'] + tuberack.rows_by_name()['D']

    # Define drug concentrations
    drug_concentrations = [
        1,
        0.1,
        0.01,
        0.001,
        0.0001,
        0.00005,
        0.00001,
        0.00002,
        0.00004,
        0.00008,
        0.00016,
        0.0002
    ]  # In molar

    # Define drug dilution factors
    dil_factor_4x = 4
    dil_factor_2x = 0.5

    # Define procedures for automating the protocol

    # Pick up cells
    p10.pick_up_tip()
    for well in cell_plate_wells:
        p10.transfer(cell_volume, cell_tube, well, new_tip='never')
    p10.drop_tip()

    # Add negative controls
    for well in neg_ctrl_wells:
        p10.transfer(cell_volume, cell_tube, well)

    for well in neg_ctrl_wells_A1_C5:
        p10.transfer(cell_volume, tuberack.wells()[1], well)

    # Add drug diluent
    for tube in dil_stock_tubes:
        p10.transfer(diluent_vol, tuberack.wells()[1], tube)

    # Add drug
    for source, dest in zip(dil_stock_tubes, dil_working_tubes):
        p10.pick_up_tip()
        p10.mix(mix_vol, dil_source)
        p10.aspirate(drug_vol, source)
        p10.dispense(drug_vol, dest)
        p10.drop_tip()

    # Make 4x drug dilution
    for source, dest in zip(dil_stock_tubes, dil_working_tubes):
        p10.transfer(dil_vol * dil_factor_4x, tuberack.wells()[0], dest)

    # Make 2x drug dilution
    for i, tube in enumerate(dil_working_tubes):
        if i % 2 == 0:
            continue
        p10.pick_up_tip()
        p10.transfer(dil_vol, tube, dil_working_tubes[i - 1], new_tip='never')
        p10.mix(mix_vol, dil_working_tubes[i - 1])
        p10.return_tip()

    # Add drug to plate
    for i, concentration in enumerate(drug_concentrations):
        dest_wells = well_plate.columns()[i]
        if concentration == 1:
            source_tube = dil_working_tubes[0]
        else:
            source_tube = dil_working_tubes[(i * 2) - 1]
        p10.pick_up_tip()
        p10.transfer(drug_vol, source_tube, dest_wells, new_tip='never')
        p10.mix(mix_vol, dest_wells)
        p10.return_tip()

    # Incubate for 72 hours
    protocol.comment('Incubate for 72 hours.')

    # Add CellTox reagent
    for i, well in enumerate(well_plate.rows()):
        if i == 3:
            break
        p10.pick_up_tip()
        p10.transfer(CellTox_vol, tuberack.wells()[1], well, new_tip='never')
        p10.return_tip()

    protocol.comment('Start orbital shaking for 2 minutes at 500 rpm.')

    protocol.delay(minutes=15)

    # Add CellTiter reagent
    for well in well_plate.wells():
        p10.pick_up_tip()
        p10.transfer(CellTiter_vol, tuberack.wells()[0], well, new_tip='never')
        p10.mix(mix_vol, well)
        p10.drop_tip()

    protocol.comment('Start orbital shaking for 2 minutes at 500 rpm.')

    protocol.delay(minutes=10)

