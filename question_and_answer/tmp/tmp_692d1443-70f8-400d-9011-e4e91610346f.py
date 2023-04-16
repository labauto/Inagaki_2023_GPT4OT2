# Import necessary libraries and modules
from opentrons import labware, instruments, robot

# Define the labware
plate = labware.load('96-flat', '2')
cell_count_tube = labware.load('opentrons-tuberack-2ml-eppendorf', '5')
thapsigargin_tube = labware.load('opentrons-tuberack-15ml', '7')
medium_mix_tube = labware.load('opentrons-tuberack-15ml', '6')
diluent_tube = labware.load('opentrons-tuberack-15ml', '4')
celltox_reagent_tube = labware.load('opentrons-tuberack-50ml', '10')
celltiter_glo_reagent_tube = labware.load('opentrons-tuberack-15ml', '1')
celltox_well = plate.rows()[0][:6]
celltiter_glo_well = plate.rows()[0][1:7]
medium_control_well = plate.cols()[0][4:7]
thapsigargin_control_well = plate.cols()[0][:3]
thapsigargin_treated_well = plate.cols()[1:7]
medium_mix_well = plate.cols()['7']


# Define the functions for each step

# Step 1- Take cell count
def take_cell_count():
    # Define the instrument
    pipette = instruments.P300_Single(mount='right', tip_racks=[labware.load('opentrons-tiprack-300ul', '8')])

    # Take cell count
    pipette.pick_up_tip()
    pipette.aspirate(100, cell_count_tube[0])
    pipette.dispense(100, cell_count_tube[1])
    pipette.mix(3, 50)
    pipette.drop_tip()

# Step 2- Seed the cells
def seed_cells():
    # Define the instrument
    pipette = instruments.P50_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-300ul', '9')])

    # Seed the cells
    pipette.pick_up_tip()
    for well in plate.rows()[0]:
        pipette.aspirate(48, medium_mix_tube[0])
        pipette.dispense(48, well)
        pipette.aspirate(8, cell_count_tube[1])
        pipette.dispense(8, well)
    pipette.drop_tip()

# Step 3- Dispense cell suspension in tubes
def dispense_cell_suspension_in_tubes():
    # Define the instrument
    pipette = instruments.P50_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-300ul', '9')])

    # Dispense cell suspension in tubes
    pipette.pick_up_tip()
    for tube in range(10):
        pipette.aspirate(22.5, plate.columns()[tube][5])
        pipette.dispense(22.5, thapsigargin_tube.wells()[tube])
    pipette.drop_tip()

# Step 4- Add medium in negative control wells
def add_medium_in_negative_control_wells():
    # Define the instrument
    pipette = instruments.P50_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-300ul', '9')])

    # Add medium in negative control wells
    pipette.pick_up_tip()
    for well in medium_control_well:
        pipette.aspirate(48, medium_mix_tube[0])
        pipette.dispense(48, well)
    pipette.drop_tip()

# Step 5- Add drug dilutions to tubes
def add_drug_dilutions_to_tubes():
    # Define the instrument
    pipette = instruments.P20_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-20ul', '11')])

    # Add drug dilutions to tubes
    pipette.pick_up_tip()
    tube_positions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    initial_concentrations = ['1mM', '100uM', '10uM', '1uM', '100nM', '50nM', '10nM']
    for position, concentration in zip(tube_positions, initial_concentrations):
        pipette.aspirate(15, thapsigargin_tube[position])
        pipette.dispense(15, thapsigargin_tube[position+'1'])
        pipette.mix(3, 5)
    pipette.drop_tip()

# Step 6- Prepare 4X concentrations of thapsigargin
def prepare_4x_concentrations_of_thapsigargin():
    # Define the instrument
    pipette = instruments.P20_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-20ul', '11')])

    # Define the concentrations and their positions in the tubes
    concentrations = [[1.56, 'C1'], [3.12, 'C2'], [6.24, 'C3'], [12.52, 'C4'], [25, 'C5'], [50, 'C6'], [100, 'D1'], [200, 'D2'], [400, 'D3'], [800, 'D4'], [1600, 'D5'], [2000, 'D6']]

    # Prepare 4X concentrations of thapsigargin
    for conc in concentrations:
        pipette.pick_up_tip()
        pipette.aspirate(5, diluent_tube)
        pipette.dispense(5, thapsigargin_tube[conc[1]+'1'])
        pipette.aspirate(3, thapsigargin_tube[conc[0]])
        pipette.dispense(3, thapsigargin_tube[conc[1]+'1'])
        pipette.mix(3, 5)
        pipette.drop_tip()

# Step 7- Prepare 2X concentrations of thapsigargin
def prepare_2x_concentrations_of_thapsigargin():
    # Define the instrument
    pipette = instruments.P1000_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-1000ul', '3')])

    # Dispense medium in tubes
    pipette.pick_up_tip()
    for tube in medium_mix_tube:
        pipette.aspirate(100, diluent_tube)
        pipette.dispense(100, tube)
    pipette.drop_tip()

    # Add 4X concentration of thapsigargin and mix it
    for row, tube in zip(plate.rows()[1:], thapsigargin_tube[1:7]):
        for conc_tube, well in zip(tube.wells(), row):
            pipette.pick_up_tip()
            pipette.aspirate(100, conc_tube)
            pipette.dispense(100, well)
            pipette.mix(3, 1000)
            pipette.drop_tip()

# Step 8- Add the equal volume of 2X thapsigargin to each well of 96 well plate
def add_2x_thapsigargin_to_96_well_plate():
    # Define the instrument
    pipette = instruments.P1000_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-1000ul', '3')])

    # Add the 2X concentration of thapsigargin to 96 well plate
    for col, conc in zip(thapsigargin_treated_well, concentrations):
        pipette.pick_up_tip()
        pipette.aspirate(100, conc[1]+'1')
        pipette.dispense(100, col)
        pipette.mix(3, 1000)
        pipette.drop_tip()

# Step 9- Carry out the cell viability and cytotoxicity assay
def cell_viability_and_cytotoxicity_assay():
    # Define the instruments
    pipette_20 = instruments.P20_Single(mount='left', tip_racks=[labware.load('opentrons-tiprack-20ul', '11')])
    pipette_50 = instruments.P50_Single(mount='right', tip_racks=[labware.load('opentrons-tiprack-300ul', '8')])

    # Add CellTox Green reagent and incubate
    for row in plate.rows()[1:]:
        pipette_20.pick_up_tip()
        for well in row:
            pipette_20.aspirate(15, celltox_reagent_tube[1])
            pipette_20.dispense(15, well)
        pipette_20.return_tip()

    robot._driver.run_flag.wait()   # Waiting for the robot to be ready for the next operation
    
    robot._driver.run_flag.clear()  # Clearing the run_flag
    
    robot._driver.run_flag.wait()   # Waiting for the robot to complete clearing the run_flag

    robot.pause('Remove plate from Opentrons robot and incubate at room temperature for 15 mins. After the incubation period, place the 96 well plate back on the robot and continue with the next steps.')

    # Read the fluorescence at 485 nm excitation and 520 nm emission
    for row in plate.rows()[1:]:
        pipette_50.pick_up_tip()
        for well in row:
            pipette_50.aspirate(50, well)
            pipette_50.dispense(50, well)
        pipette_50.drop_tip()

    # Add CellTiter Glo 2.0 reagent, incubate and read luminescence
    pipette_50.pick_up_tip()
    for well in celltiter_glo_well:
        pipette_50.aspirate(80, celltiter_glo_reagent_tube[0])
        pipette_50.dispense(80, well)
    pipette_50.mix(3, 50)
    pipette_50.drop_tip()

    robot._driver.run_flag.wait()   # Waiting for the robot to be ready for the next operation
    
    robot._driver.run_flag.clear()  # Clearing the run_flag
    
    robot._driver.run_flag.wait()   # Waiting for the robot to complete clearing the run_flag

    robot.pause('Incubate the plate at room temperature for 10 mins. After the incubation period, place the 96 well plate back on the robot and continue with the next steps.')

    for col in plate.cols():
        pipette_50.pick_up_tip()
        for well in col:
            pipette_50.aspirate(50, well)
            pipette_50.dispense(50, well)
        pipette_50.drop_tip()

# Run the steps in sequence
def main():
    robot.home()

    take_cell_count()

    seed_cells()

    dispense_cell_suspension_in_tubes()

    add_medium_in_negative_control_wells()

    add_drug_dilutions_to_tubes()

    prepare_4x_concentrations_of_thapsigargin()

    prepare_2x_concentrations_of_thapsigargin()

    add_2x_thapsigargin_to_96_well_plate()

    cell_viability_and_cytotoxicity_assay()

if __name__ == "__main__":
    main()
