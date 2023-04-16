from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Viability and Cytotoxicity Assay',
    'author': 'Your name here',
    'description': 'Protocol for measuring viability and cytotoxicity of A549 cells treated with thapsigargin',
    'apiLevel': '2.10.1'
}

# Define plate and well coordinates
plate = "96-flat"
negative_control_wells = ["A5", "B5", "C5"]
drug_treated_wells = ["A1", "B1", "C1", "D1", "E1", "F1", "D4", "E4", "F4"]
medium_control_wells = ["A5", "B5", "C5"]
celltox_reagent_wells = ["B2", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4"]
celltiter_reagent_wells = ["B1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "A5", "B5", "C5"]

# Define tip racks
tip_racks_10ul = [protocol.load_labware('tiprack-10ul', slot) for slot in ['4', '7', '8']]
tip_racks_200ul = [protocol.load_labware('tiprack-200ul', slot) for slot in ['5', '9']]

# Define pipettes
p10 = protocol.load_instrument('p10_single', mount='left', tip_racks=tip_racks_10ul)
p200 = protocol.load_instrument('p200_single', mount='right', tip_racks=tip_racks_200ul)

# Define reagents
celltox_reagent = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conicalrack', slot='11').wells_by_name()['B2']
celltiter_reagent = protocol.load_labware('96-flat', slot='10').wells_by_name()['A5']

def clean_robot():
    """
    Cleans the inside of the robot with 70% ethanol and turns on the HEPA filter. The HEPA filter is left on during the experiment.
    """
    robot.home()
    protocol.pause("Please clean the inside of the robot with 70% ethanol and press resume when done.")
    protocol.set_rail_lights(True)
    protocol.delay(minutes=60)
    protocol.set_rail_lights(False)

def seed_cells():
    """
    Seeding A549 cells and adding media to negative control wells.
    """
    # Take cell count
    countess = protocol.load_module('countess', '3')
    countess.robot.turn_on_lights()
    protocol.pause('Insert cell counting slides and switch on the countess instrument. Dilute cells in TrypLE Express buffer, then add 25ul of cells to each counting slide. Mix well and check that cells are dispersed evenly across the slide. Place the slide into the Countess instrument and acquire cell count before proceeding. Press resume if ready to proceed.')
    countess.reset()
    cells = countess.acquire_cell_count()

    # Seed cells
    cell_volume = 6e-5  # vol of cells to add in each well (uL)
    cells_to_seed = 8000  # cells to seed in each well
    cells_needed = cells_to_seed / cells * 1e6
    cells_volume = cells_needed / cells * cell_volume
    cells_volume = cells_volume * 1.1  # add 10% extra cells

    # Calculate cell suspension volume
    wells = protocol.load_labware(plate, '1')
    cell_susp = wells.rows()[0][:len(drug_treated_wells)]
    p200.pick_up_tip()
    for s in cell_susp:
        p200.transfer(cells_volume, countess.buffer_well, s.top(-5), new_tip='never')
        p200.blow_out(s.top(-5))
    p200.drop_tip()

    # Add media to negative control wells
    neg_ctrl_wells = wells.wells_by_name()[
        ":".join([plate.split("-")[0], negative_control_wells[0]]) :
        ":".join([plate.split("-")[0], negative_control_wells[-1]])
    p200.distribute(60, countess.buffer_well, neg_ctrl_wells, new_tip='always')

def dilute_drugs():
    """
    Prepare dilutions of Thapsigargin in Ham's F12K medium.
    """
    # Prepare initial drug stocks
    drug_wells = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conicalrack', slot='11').rows()[0][:len(drug_treated_wells)]
    thapsigargin_1mM = drug_wells[0]
    thapsigargin_100uM = drug_wells[1]
    thapsigargin_10uM = drug_wells[2]
    thapsigargin_1uM = drug_wells[3]
    thapsigargin_100nM = drug_wells[4]
    thapsigargin_50nM = drug_wells[5]
    thapsigargin_10nM = drug_wells[6]

    # Prepare dilutions of Thapsigargin
    for i, dilution in enumerate(['4X', '2X', '1X']):
        if dilution == '4X':
            drug_vol = 15
            diluent_vol = 45
            source_plates = drug_wells
        elif dilution == '2X':
            drug_vol = 50
            diluent_vol = 50
            source_plates = [d.top(-2) for d in drug_wells]
        elif dilution == '1X':
            drug_vol = 100
            diluent_vol = 100
            source_plates = [d.top(-2) for d in drug_wells]
            dilution_wells = protocol.load_labware(plate, '2').wells_by_name()[drug_treated_wells[i * 3] : drug_treated_wells[(i + 1) * 3 - 1]]
        for j, (source_plate, dilution_well) in enumerate(zip(source_plates, dilution_wells)):
            if dilution == '4X':
                vol_to_dispense = diluent_vol
                p10.pick_up_tip()
                p10.aspirate(vol_to_dispense, protocol.load_labware(plate, '1').wells_by_name()['A1'].bottom(1))
                p10.move_to(protocol.load_labware(plate, '1').wells_by_name()[drug_treated_wells[j]].bottom(1))
                p10.dispense(vol_to_dispense, protocol.load_labware(plate, '1').wells_by_name()[drug_treated_wells[j]].bottom(1))
                p10.mix(repetitions=3, volume=20, location=protocol.load_labware(plate, '1').wells_by_name()[drug_treated_wells[j]].bottom(1))
                p10.blow_out()
                p10.drop_tip()
                vol_to_dispense = drug_vol
                p10.pick_up_tip()
                p10.aspirate(vol_to_dispense, source_plate)
                if j != len(source_plates) - 1:
                    p10.dispense(vol_to_dispense, source_plates[j + 1])
                    p10.mix(repetitions=3, volume=20, location=source_plates[j + 1])
                p10.dispense(vol_to_dispense, dilution_well)
                p10.mix(repetitions=3, volume=20, location=dilution_well)
                p10.blow_out()
                p10.drop_tip()
            elif dilution == '2X':
                vol_to_dispense = diluent_vol
                p200.pick_up_tip()
                p200.aspirate(vol_to_dispense, celltiter_reagent.bottom(1))
                p200.move_to(dilution_well.top(-2))
                p200.dispense(vol_to_dispense, dilution_well.top(-2))
                p200.blow_out(dilution_well.top(-2))
                p200.drop_tip()
                vol_to_dispense = drug_vol
                p10.pick_up_tip()
                p10.aspirate(vol_to_dispense, source_plate)
                p10.dispense(vol_to_dispense, dilution_well)
                p10.mix(repetitions=3, volume=20, location=dilution_well)
                p10.blow_out()
                p10.drop_tip()
            elif dilution == '1X':
                vol_to_dispense = diluent_vol
                p200.pick_up_tip()
                p200.aspir


:*************************


