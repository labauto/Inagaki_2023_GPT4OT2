
def cleaning_robot():
    """Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter at low fan speed for about an hour before seeding the cells on 96 well plate.""" 
    print("Cleaning robot with 70 % ethanol...")
    print("Turning on the HEPA filter at low fan speed...")

def seeding_cells():
    """Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day after the cells have adhered to the 96 well TC plate."""
    print("Taking a 24–48 hours old T-75 flask of A549 cells...")
    print("Adjusting cell volume in 10% Ham’s F12K medium to contain 8000 cells in 60 microL...")
    print("Dispensing cell suspension in 1.5mL snap-capped tubes and placing in Slot 6...")
    print("Adding medium in wells A5 to C5 as negative control...")

def preparing_dilutions():
    """On the second day, roughly after 12 to 16 hours of seeding, the drug dilutions and additions are completed."""
    print("Preparing initial stocks ranging from 10nM to 100microM thapsigargin...")
    print("Preparing 4X concentrations of thapsigargin in tubes C1 to C6 and D1 to D6...")
    print("Preparing 2X concentrations of thapsigargin by adding 100microL of medium to tubes C1, C3, C5 and D1 to D6...")
    print("Adding equal volume of 2X thapsigargin to each well of 96 well plate in triplicate for one concentration...")

def thapsigargin_addition():
    """Adding column-wise the increasing concentrations of thapsigargin. Namely A1, B1, C1 of 96 well plate contains control cells. D1, E1 and F1 contains 0.39nM concentration of thapsigargin treated cells. The wells in D4, E4 and F4 contains cells with 500nM thapsigargin concentration. The wells from A5 to C5 contain medium without any cells (medium control)."""
    print("Adding control cells in wells A1, B1, C1 of 96 well plate...")
    print("Adding 0.39nM concentration of thapsigargin treated cells in wells D1, E1 and F1...")
    print("Adding 500nM thapsigargin concentration in wells D4, E4 and F4...")
    print("Adding medium without any cells (medium control) in wells from A5 to C5...")

def cytotoxicity_assay():
    """After 72 hours of drug treatment, carry out the following steps."""
    print("Transferring 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack with Falcon 4X50 mL, 6X15mL Conical-Rack to A1 of 96 well plate placed on the Heater Shaker...")
    print("Setting the Heater Shaker to orbital shaking for 2 minutes at 500 rpm...")
    print("Incubating the plate at RT for 15 min...")
    print("Reading the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader...")

def cell_viability_assay():
    """For the cell viability assay carry out the following steps."""
    print("Transferring 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack and dispensing into A1 well of the 96 well white TC plate on Heater Shaker module...")
    print("Setting the Heater shaker to orbital shaking at 500 rpm for 2 minutes...")
    print("Incubating at RT for 10 minutes...")
    print("Reading the plate for luminescence using the Biotek microplate reader...")

def main():
    cleaning_robot()
    seeding_cells()
    preparing_dilutions()
    thapsigargin_addition()
    cytotoxicity_assay()
    cell_viability_assay()

if __name__ == "__main__":
    main()


:*************************


