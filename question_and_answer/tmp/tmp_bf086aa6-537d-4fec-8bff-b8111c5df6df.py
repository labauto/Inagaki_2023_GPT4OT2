from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'apiLevel': '2.10'
}

# Define the robot
robot = protocol_api.ProtocolContext()  

def clean_robot():
    # Clean the inside of the robot with 70% ethanol
    # and turn on the HEPA filter at low fan speed
    robot.comment('Cleaning the robot...')
    robot.pause('Add 70% ethanol to the cleaning cassette, put it in Slot 12, and click "Resume"')
    robot._hw_manager.hardware.set_lights(rails=False, lights=True)
    robot.pause('Turn on the HEPA filter at low fan speed and wait for 1 hour, then click "Resume"')
    robot._hw_manager.hardware.set_lights(rails=True, lights=False)
    robot.comment('Robot cleaning complete.')

def seed_cells():
    # Seed A549 cells in a 96 well plate
    robot.comment('Seeding cells...')
    # Calculate the cell volume needed to seed 8000 cells in each well
    cell_count = robot.countess.count_cells()
    cell_volume = 60 / cell_count * 8000
    # Prepare the cell suspension
    cells = robot.load_labware('opentrons_24_tuberack_1500ul', '6')
    medium = robot.load_labware('tcplate_96_wellplate_100ul', '9')
    pipette = robot.load_instrument('p300_single', 'left')
    pipette.pick_up_tip()
    for tube, well in zip(cells.wells()[:10], medium.rows()[0][:10]):
        pipette.transfer(cell_volume, tube, well, blow_out=True)
    # Add the medium control
    for well in medium.columns()[4][:3]:
        pipette.transfer(60, medium.columns()[0][4], well, blow_out=True)
    robot.comment('Cell seeding complete.')

def prepare_drug_dilutions():
    # Prepare dilutions of thapsigargin
    robot.comment('Preparing drug dilutions...')
    # Load the drug stocks
    stocks = robot.load_labware('opentrons_24_tuberack_1500ul', '7')
    dilutions = robot.load_labware('opentrons_24_tuberack_1500ul', '8')
    medium = robot.load_labware('opentrons_24_tuberack_1500ul', '6')
    # Prepare the 4X drug concentrations
    pipette = robot.load_instrument('p300_single', 'left')
    pipette.pick_up_tip()
    for i in range(7):
        pipette.transfer(200, medium.columns()[0][0], dilutions.columns()[0][i], blow_out=True)
        pipette.transfer(50, stocks.columns()[0][i], dilutions.columns()[0][i], mix_after=(3, 50))
    # Prepare the 2X drug concentrations
    for i, col in enumerate(medium.columns()[0][::2]):
        for j in range(1, 7):
            pipette.transfer(100, dilutions.columns()[0][j], col, mix_after=(3, 100))
            pipette.transfer(100, col, col.parent.columns()[i + 4].bottom(3), blow_out=True)
    robot.comment('Drug dilutions prepared.')

def treat_cells():
    # Treat the cells with thapsigargin
    robot.comment('Treating cells...')
    plate = robot.load_labware('tcplate_96_wellplate_100ul', '1')
    medium = robot.load_labware('opentrons_24_tuberack_1500ul', '6')
    for i, col in enumerate(plate.columns()[1:]):
        for j, well in enumerate(col):
            if j == 2:
                pipette.transfer(60, medium.columns()[0][4], well, blow_out=True)
                continue
            drug_conc = (j - 3) * 0.39
            drug_vol = 100 * drug_conc / (2000 - drug_conc)
            pipette.transfer(drug_vol, medium.columns()[0][i * 2 + 1], col[j], blow_out=True)
    robot.comment('Drug treatment complete.')

def add_celltox_reagent():
    # Add CellTox Green reagent to measure cytotoxicity
    robot.comment('Adding CellTox Green reagent...')
    plate = robot.load_labware('tcplate_96_wellplate_100ul', '1')
    reagent_tube = robot.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '10').wells()[1]
    pipette = robot.load_instrument('p20_multi_gen2', 'right')
    pipette.pick_up_tip()
    for row in plate.rows()[:4]:
        pipette.aspirate(15, reagent_tube)
        for well in row:
            pipette.dispense(15, well.top(-3))
        pipette.blow_out(reagent_tube.top())
    robot.comment('CellTox Green reagent added.')

def shake_plate():
    # Shake the plate to distribute the reagent evenly
    robot.comment('Shaking the plate...')
    plate = robot.load_labware('tcplate_96_wellplate_100ul', '1')
    robot._hw_manager.hardware.set_temperature(25)
    robot._hw_manager.hardware.set_temperature(37)
    plate.place(robot._hw_manager.hardware._deck)
    robot.pause('Start orbital shaking for 2 minutes at 500 rpm on the Heater/Shaker, then click "Resume"')
    robot.comment('Plate shaking complete.')

def read_cytotoxicity():
    # Read the fluorescence to measure cytotoxicity
    robot.comment('Reading cytotoxicity...')
    plate = robot.load_labware('tcplate_96_wellplate_100ul', '1')
    reader = robot.load_instrument('c1000_touch', 'right')
    reader.start_lid_close_detection()
    reader.open_lid()
    reader.close_lid()
    reader.set_lid_temperature(37)
    reader.set_excitation(485)
    reader.set_emission(520)
    reader.set_gain(50)
    measurement = reader.take_measurement(1)
    robot.comment('Cytotoxicity measurement complete.')

def add_celltiter_reagent():
    # Add CellTiter Glo 2.0 reagent to measure viability
    robot.comment('Adding CellTiter Glo 2.0 reagent...')
    plate = robot.load_labware('clear_96_wellplate_200ul', '2')
    reagent_tube = robot.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '10').wells()[0]
    pipette = robot.load_instrument('p300_single', 'left')
    pipette.pick_up_tip()
    for row in plate.rows()[:4]:
        pipette.aspirate(80, reagent_tube)
        for well in row[:8]:
            pipette.dispense(80, well.top())
        pipette.blow_out(reagent_tube.top())
    robot.comment('CellTiter Glo 2.0 reagent added.')

def shake_plate_again():
    # Shake the plate to distribute the reagent evenly
    robot.comment('Shaking the plate again...')
    robot.pause('Start orbital shaking for 2 minutes at 500 rpm on the Heater/Shaker, then click "Resume"')
    robot.comment('Plate shaking complete.')

def read_viabililty():
    # Read the luminescence to measure viability
    robot.comment('Reading viability...')
    plate = robot.load_labware('clear_96_wellplate_200ul', '2')
    reader = robot.load_instrument('c1000_touch', 'right')
    reader.start_lid_close_detection()
    reader.open_lid()
    reader.close_lid()
    reader.set_lid_temperature(37)
    reader.set_luminescence(excitation=0, emission=0)
    reader.set_gain(50)
    measurement = reader.take_measurement(1)
    robot.comment('Viability measurement complete.')

def main():
    robot.home()
    clean_robot()
    seed_cells()
    prepare_drug_dilutions()
    treat_cells()
    add_celltox_reagent()
    shake_plate()
    read_cytotoxicity()
    add_celltiter_reagent()
    shake_plate_again()
    read_viabililty()

if __name__ == '__main__':
    main()
