
def cleanRobot():
    """
    Clean the robot with 70% ethanol and turn on the HEPA filter at low fan speed.
    """
    # Code for cleaning robot
    
    
def cellCount():
    """
    Take cell count of A549 cells using Countess 3 machine.
    """
    # Code for taking cell count
    
    
def seedCells(cell_number, cell_volume):
    """
    Seed A549 cells in 96 well plate.
    Parameters:
        cell_number (int): Number of cells to seed.
        cell_volume (float): Volume of cells per well. 
    """
    # Code for seeding cells
    
    
def addNegativeControl():
    """
    Add medium to wells A5 to C5 as negative control.
    """
    # Code for adding negative control
    
    
def prepareThapsigarginSolutions(stock_concentrations):
    """
    Prepare dilutions of thapsigargin.
    Parameters:
        stock_concentrations (list): List of stock concentrations of thapsigargin
    """
    # Code for preparing thapsigargin solutions
    
    
def addThapsigargin(concentrations):
    """
    Add thapsigargin of various concentrations to 96 well plate.
    Parameters:
        concentrations (list): List of concentrations to add to 96 well plate.
    """
    # Code for adding thapsigargin
    

def addCellToxGreen():
    """
    Add CellTox Green reagent to the 96 well plate.
    """
    # Code for adding CellTox Green reagent
    
    
def incubateShakePlate(rpm, time):
    """
    Incubate and shake the 96 well plate in Heater Shaker.
    Parameters:
        rpm (int): Revolution per minute of the heater shaker.
        time (int): Time of incubation and shaking in minutes.
    """
    # Code for incubating and shaking plate
    
    
def measureFluorescence():
    """
    Measure fluorescence at 485 nm excitation and 520 nm emission using Biotek microplate reader.
    """
    # Code for measuring fluorescence
    
    
def measureLuminescence():
    """
    Measure luminescence using Biotek microplate reader.
    """
    # Code for measuring luminescence
    

def main():
    # Clean the robot
    cleanRobot()
    
    # Take cell count
    cell_number = cellCount()
    cell_volume = 60 # microL

    # Seed cells
    seedCells(cell_number, cell_volume)
    
    # Add negative control
    addNegativeControl()
    
    # Prepare thapsigargin solutions
    stock_concentrations = [1mM, 100microM, 10microM, 1microM, 100nM, 50nM, 10nM]
    prepareThapsigarginSolutions(stock_concentrations)
    
    # Add thapsigargin of different concentrations to 96 well plate
    concentrations = [0.39nM, 500nM]
    addThapsigargin(concentrations)
    
    # Add CellTox Green reagent
    addCellToxGreen()
    
    # Incubate and shake plate 
    rpm = 500
    time = 2
    incubateShakePlate(rpm, time)
    
    # Measure fluorescence
    measureFluorescence()
    
    # Measure luminescence
    measureLuminescence()


if __name__ == "__main__":
    main()


:*************************


