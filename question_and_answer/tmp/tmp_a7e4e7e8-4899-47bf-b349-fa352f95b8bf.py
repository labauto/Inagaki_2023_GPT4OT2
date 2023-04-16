from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell viability and cytotoxicity assay',
    'author': 'Your Name Here <your.email@example.com>',
    'description': 'Measurement of viability and cytotoxicity of A549 cells treated with thapsigargin',
    'apiLevel': '2.0'
}

# Protocol run function. The part after the colon lets your editor know
# what type of object to expect as an input
def run(protocol: protocol_api.ProtocolContext):

    # Clean the robot before starting
    clean_robot()

    # Seed cells
    seed_cells(protocol)

    # Add drug dilutions and concentrations
    add_drug(protocol)

    # Perform cell viability assay
    cell_viability_assay(protocol)

    # Perform cell cytotoxicity assay
    cell_cytotoxicity_assay(protocol)

# Function to clean the inside of the robot
def clean_robot():
    # TODO: Add cleaning steps here
    pass

# Function to seed cells
def seed_cells(protocol):
    # TODO: Add cell seeding steps here
    pass

# Function to add drug dilutions and concentrations
def add_drug(protocol):
    # TODO: Add drug dilution and concentration steps here
    pass

# Function to perform cell viability assay
def cell_viability_assay(protocol):
    # TODO: Add cell viability assay steps here
    pass

# Function to perform cell cytotoxicity assay
def cell_cytotoxicity_assay(protocol):
    # TODO: Add cell cytotoxicity assay steps here
    pass
