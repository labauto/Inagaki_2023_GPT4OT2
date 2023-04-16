
def seeding_cells(n_cells, medium, plate_name):
    """
    This function takes the number of cells, medium, and plate name as input and is used to seed the cells into the plate.
    
    Parameter:
    n_cells (int): Number of cells
    medium (str): 10% Ham’s F12K medium
    plate_name (str): Plate name
    
    """
    # Clean the inside of the robot with 70% ethanol and turn on the HEPA filter at low fan speed.
    # Dispense 60 microL of cell suspension with 8000 cells per well in the 96 well plate.
    # Add the medium in wells A5 to C5 as negative control.
    
def drug_additions(drug_tube, drug_conc):
    """
    This function takes the drug tube and drug concentration as input and is used to prepare dilutions and add the drug on to the 96 well plate.
    
    Parameter:
    drug_tube (str): Tube name containing the drug
    drug_conc (list): Concentrations of the drug
    
    """
    # Prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium (4X concentrations)
    # Add the drug to the respective tubes.
    # Prepare 2X concentrations of the drug and add equal volume of drug to each well of 96 well plate in triplicate.

def assays(assay_name, reagent):
    """
    This function is used to add the reagent, shake, incubate and read the fluorescence or luminescence using the Biotek microplate reader.
    
    Parameter:
    assay_name (str): Name of the assay
    reagent (str): Reagent name
    
    """
    # Pick up the respective tip and aspirate the reagent.
    # Dispense the reagent into the plate.
    # Set the Heater shaker to orbital shaking at 500 rpm for 2 minutes.
    # Incubate the plate at RT for 15 minutes.
    # Read the fluorescence or luminescence using the Biotek microplate reader.

# Main function
def main():
    """
    This is the main function and all the other functions are called in this function
    """
    seeding_cells(8000, '10% Ham’s F12K medium', '96 well TC plate')
    drug_additions('A1', ['1mM', '100microM', '10microM', '1microM', '100nM', '50nM', '10nM'])
    assays('CellToxicity', 'CellTox Green Reagent')
    assays('CellViability', 'Cell Titer Glo 2.0 Reagent')

if __name__ == "__main__":
    main()


:*************************


