
def seed_cells():
    # Take a 24–48 hours old T-75 flask of A549 cells
    # Take a cell count using the automated Countess 3 machine
    # Treat the cells with Tryple Express enzyme and dislodge adherent cells
    # 8000 cells are to be seeded in each well of the 96 well plate
    # Adjust the cell volume in 10% Ham’s F12K medium
    # Dispense the cell suspension in ten 1.5mL snap-capped tubes and place on Slot 6
    # Add the medium to wells A5 to C5 for negative controls

def drug_dilution():
    # Take tube A1 from Slot 7 containing 35microL of 1mM Thapsigargin
    # Prepare dilutions of various concentrations of thapsigargin 4X concentrations
    # Prepare 4X concentrations of thapsigargin in tubes C1 to C6 and D1 to D6
    # Prepare 2X concentrations of thapsigargin in slots C1, C3, C5 and D1 to D6

def drug_addition():
    # Add the equal volume of 2X thapsigargin to each well of 96 well plate in triplicate
    # Add increasing concentrations of thapsigargin column-wise

def cell_toxicity_measurement():
    # Pick up 20microL tip from Slot 10
    # Transfer 15microL of CellTox Green reagent from B2 of the Opentrons 10 tube rack
    # Add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4, A5 to C5
    # Set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm
    # Incubate the plate at RT for 15 min
    # Read the fluorescence at 485 nm excitation and 520 nm emission using the Biotek microplate reader
    # Pick up 200microL tip from Slot 4
    # Aspirate 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack
    # Dispense it into A1 well of the 96 well white TC plate on Heater Shaker module
    # Repeat this step to add the reagent to wells B1 to H1, A2 to H2, A3 to H3, A4 to F4 and A5 to C5
    # Set the Heater shaker to orbital shaking at 500 rpm for 2 minutes
    # Incubate at RT for 10 minutes
    # Read the plate for luminescence using the Biotek microplate reader

def main():
    # Clean the inside of the robot with 70 % ethanol
    # Turn on the HEPA filter at low fan speed
    seed_cells()
    drug_dilution()
    drug_addition()
    cell_toxicity_measurement()

if __name__ == '__main__':
    main()


:*************************


