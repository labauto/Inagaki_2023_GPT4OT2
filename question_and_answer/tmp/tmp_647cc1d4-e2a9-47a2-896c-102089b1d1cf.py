
def clean_robot():
    """
    Clean the robot with 70% ethanol and turn on the HEPA filter at low fan speed for 1 hour before seeding cells.
    """

def cell_count():
    """
    Take a 24–48 hours old T-75 flask of A549 cells. Take a cell count using the automated Countess 3 machine
    after treating the cells with Tryple Express enzyme and dislodging the adherent cells.
    """

def seed_cells():
    """
    Seed 8000 cells in each well of the 96 well plate in 10% Ham’s F12K medium.
    """

def add_medium_control():
    """
    Add the medium in wells A5 to C5 as negative control.
    """

def prepare_drug():
    """
    Prepare dilutions of various concentrations of thapsigargin in 10% Ham’s F12K medium (4X concentrations) after
    preparing the initial stocks ranging from 10nM to 100microM.
    """

def add_drug():
    """
    Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate.
    """

def add_reagent():
    """
    Pick up 20microL tip from Slot 10. Transfer 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack
    with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker.
    Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4, A5 to C5.
    """

def shake_plates():
    """
    Set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm.
    """

def incubate_plate():
    """
    Incubate the plate at RT for 15 min.
    """

def read_fluorescence():
    """
    Read the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader.
    """

def add_titer():
    """
    Pick up 200microL tip from Slot 4. Aspirate 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube
    rack and dispense it into A1 well of the 96 well white TC plate on Heater Shaker module. Repeat this step to add the
    reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4 and A5 to C5.
    """

def incubate_titer():
    """
    Incubate at RT for 10 minutes.
    """

def read_luminescence():
    """
    Remove the plate from heater shaker and read the plate for luminescence using the Biotek microplate reader.
    """

def main():
    clean_robot()
    cell_count()
    seed_cells()
    add_medium_control()
    prepare_drug()
    add_drug()
    add_reagent()
    shake_plates()
    incubate_plate()
    read_fluorescence()
    add_titer()
    incubate_titer()
    read_luminescence()

if __name__ == '__main__':
    main()


:*************************


