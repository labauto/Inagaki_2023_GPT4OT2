from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'created': '',   
    'lastModified': '',
}

# define your protocol
def run(protocol: protocol_api.ProtocolContext):

    # Add your code here
    # Step 1: Cleaning the robot with 70% ethanol and 
    #               turning on the HEPA filter.
    # Step 2: Seeding the A549 cells with Ham’s F12K medium 
    #               at a concentration of 8000 cells/well.
    # Step 3: Adding a negative control i.e medium in wells. 
    # Step 4: Adding drug dilutions to the 96-well plate.
    # Step 5: After the completion of drug dilutions, cell 
    #               treatments are carried out.
    # Step 6: Picking up 20 μL tip and transferring 15 μL of 
    #               CellTox Green reagent to the 96-well plate.
    # Step 7: Setting the Heater Shaker to orbital shaking for 
    #               2 min.
    # Step 8: Incubating the plate at RT for 15 min.
    # Step 9: Reading fluorescence at 485 nm excitation and 
    #               520 nm emission using a microplate reader.
    # Step 10: Adding CellTiter Glo 2.0 reagent to assess 
    #               cell viability to each well of the 96-well 
    #               plate in triplicate.
    # Step 11: Setting the Heater Shaker to orbital shaking for 
    #               2 min, incubating at RT for 10 min, and 
    #               reading luminescence using a microplate reader.
    
# Opentrons API Reference: https://docs.opentrons.com/v2/ 

