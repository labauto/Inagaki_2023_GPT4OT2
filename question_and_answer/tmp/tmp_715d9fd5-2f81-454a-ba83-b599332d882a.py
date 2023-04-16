
def clean_robot():
    """
    Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells on 96 well plate.
    """
    # code for cleaning robot
    
    
def seed_cells_on_plate():
    """
    Take a 24–48 hours old T-75 flask of A549 cells. Take a cell count using the automated Countess 3 machine (Thermofisher Scientific)
    after treating the cells with Tryple Express enzyme and dislodging the adherent cells.
    Adjust the cell volume in 10% Ham’s F12K medium in such a way that 60 microL of cells contain the cell number mentioned above.
    The cell suspension was then dispensed in ten 1.5mL snap-capped tubes and placed in Slot 6 in the tube rack(225microL).
    The medium was added in wells A5 to C5 as negative control
    """
    # code for seeding cells
    
    
def prepare_drug_dilutions():
    """
    On the second day, roughly after 12 to 16 hours of seeding, the drug dilutions and additions are completed.
    The first tube A1 in Slot 7 contains 35microL of 1mM Thapsigargin.
    Prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium (4X concentrations) after preparing the initial stocks ranging from 10nM to 100microM. 
    """
    # code for preparing drug dilutions
    

def add_thapsigargin_to_plate():
    """
    Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate for one concentration in which cells are seeded.
    This will result in 1X concentration of the drug used for the study.
    Continue adding column-wise the increasing concentrations of thapsigargin.
    """
    # code for adding thapsigarigin to plate
    

def add_celltox_green_reagent():
    """
    Pick up 20microL tip from Slot 10. Transfer 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker.
    Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4, A5 to C5.
    After the addition of the reagent, set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm.
    After the orbital shaking of the heater shaker is complete, incubate the plate at RT for 15 min.
    """
    # code for adding celltox green reagent
    

def add_cell_titer_glo_2_0_reagent():
    """
    Pick up 200microL tip from Slot 4. Aspirate 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack and dispense it into A1 well of the 96 well white TC plate on Heater Shaker module. Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4 and A5 to C5.
    Once the reagent addition is complete, set the Heater shaker to orbital shaking at 500 rpm for 2 minutes. Incubate at RT for 10 minutes.
    """
    # code for adding cell titer glo 2.0 reagent
    
    
def read_fluorescence():
    """
    Remove the plate from the heater shaker and read the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader.
    """
    # code for reading fluorescence
    
    
def read_luminescence():
    """
    Remove the plate from heater shaker and read the plate for luminescence using the Biotek microplate reader.
    """
    # code for reading luminescence
    

def main():
    """
    Main function to run experiment
    """
    
    # clean robot
    clean_robot()
    
    # seed cells on plate
    seed_cells_on_plate()
    
    # prepare drug dilutions
    prepare_drug_dilutions()
    
    # add thapsigargin to plate
    add_thapsigargin_to_plate()
    
    # add celltox green reagent
    add_celltox_green_reagent()
    
    # add cell titer glo 2.0 reagent
    add_cell_titer_glo_2_0_reagent()
    
    # read fluorescence
    read_fluorescence()
    
    # read luminescence
    read_luminescence()

# call main function
main()


:*************************


