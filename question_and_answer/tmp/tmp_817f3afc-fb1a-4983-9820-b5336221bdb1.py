
def robot_clean():
    """This function runs the robot cleaning process
    
    This function cleans the robot with 70% ethanol to ensure sterility 
    before seeding the cells.
    """
    # cleaning the robot with 70% ethanol
    # turn on the HEPA filter at low fan speed for about an hour
    
def seed_cells():
    """This function seeds A549 cells on 96 well plate
    
    This function takes an 24-48 hours old T-75 flask of A549 cells, 
    takes cell count, prepares the cell suspension, seeds 8000 cells 
    in each well of the 96 well plate, adds the medium in wells A5-C5 
    as negative control, and incubate the plate.
    """
    # take an 24-48 hours old T-75 flask of A549 cells
    # take cell count 
    # prepare cell suspension
    # seed 8000 cell into each well of the 96 well plate
    # add the medium in wells A5-C5 as negative control
    # incubate the plate

def prepare_thapsigargin_dilutions():
    """This function prepares the dilutions of thapsigargin
    
    This function prepares the initial stock of thapsigargin 
    ranging from 10nM to 100microM, prepares 4X concentrations
    of thapsigargin and 2X concentrations of thapsigargin,
    and adds the thapsigargin to the 96 well plate.
    """
    # prepare initial stock of thapsigargin ranging from 10nM to 100microM
    # prepare 4X concentrations of thapsigargin
    # prepare 2X concentrations of thapsigargin
    # add the thapsigargin to 96 well plate

def measure_viability_and_cytotoxicity():
    """This function measures the viability and cytotoxicity of cells
    
    This function adds CellTox Green reagent to the cells, incubates the
    plate, reads the fluorescence, and adds Cell Titer Glo 2.0 reagent to
    the cells, incubates the plate, and reads the luminescence.
    """
    # add CellTox Green reagent to the cells
    # incubate the plate
    # read the fluorescence 
    # add Cell Titer Glo 2.0 reagent to the cells
    # incubate the plate
    # read the luminescence

def main():
    """Main function that runs the entire experiment
    
    This function calls all the other functions to run the entire
    experiment.
    """
    # run the robot cleaning process
    robot_clean()
    
    # seed A549 cells
    seed_cells()
    
    # prepare dilutions of thapsigargin
    prepare_thapsigargin_dilutions()
    
    # measure the viability and cytotoxicity of cells
    measure_viability_and_cytotoxicity()

# run the main function
if __name__ == "__main__":
    main()


:*************************


