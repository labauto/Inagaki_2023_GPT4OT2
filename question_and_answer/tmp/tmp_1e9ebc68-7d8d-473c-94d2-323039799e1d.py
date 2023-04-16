import opentrons.execute
from opentrons import types
from opentrons.types import Point

protocol = opentrons.execute.get_protocol_api('2.0')

def clean_robot_with_ethanol():
    # Code to clean the inside of the robot with 70% ethanol
    pass

def turn_on_hepa_filter():
    # Code to turn on the HEPA filter at low fan speed for an hour, if this feature is available in your Opentrons machine
    pass

def seed_A549_cells():
    # Code for seeding 8000 A549 cells in each well of the 96 well plate using the cell count information from the Countess 3 machine
    pass

def add_medium_to_wells():
    # Function to add medium to wells A5 to C5 as negative control
    pass

def prepare_initial_stocks_and_4X_concentrations():
    # Code to prepare dilutions of various concentrations of thapsigargin in 10% Ham's F12K medium (4X concentrations) after preparing the initial stocks ranging from 10nM to 100microM
    pass

def prepare_2X_concentrations():
    # Code to prepare 2X concentrations of the drug by transferring 100microL of 4X concentration of thapsigargin to tubes containing 100microL of medium
    pass

def add_drug_to_well_plate():
    # Function to add the equal volume of 2X thapsigargin to each well of the 96 well plate in triplicate for one concentration in which cells are seeded
    pass

def add_CellTox_Green():
    # Function to add 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack to the 96 well plate
    pass

def incubate_and_read_fluorescence():
    # Function to incubate the plate at room temperature and read the fluorescence using the Biotek microplate reader
    pass

def add_CellTiter_Glo():
    # Function to add 80microL of CellTiter Glo 2.0 reagent to the 96 well white TC plate on the Heater Shaker module
    pass

def incubate_and_read_luminescence():
    # Function to incubate the plate at room temperature and read the luminescence using the Biotek microplate reader
    pass

def main():
    clean_robot_with_ethanol()
    turn_on_hepa_filter()
    seed_A549_cells()
    add_medium_to_wells()
    prepare_initial_stocks_and_4X_concentrations()
    prepare_2X_concentrations()
    add_drug_to_well_plate()
    add_CellTox_Green()
    incubate_and_read_fluorescence()
    add_CellTiter_Glo()
    incubate_and_read_luminescence()

if __name__ == "__main__":
    main()
