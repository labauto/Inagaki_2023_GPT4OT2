from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Measurement',
    'author': 'Your Name Here',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'apiLevel': '2.0',
}

# Create the protocol object
protocol = protocol_api.ProtocolContext()

# Define your protocol steps here
# Clean the robot with 70% ethanol
...

# Add the cell suspension to the 96-well plate
...

# Add dilutions of thapsigargin to the plate
...

# Shake the plate and incubate
...

# Add CellTox Green reagent
...

# Shake and incubate
...

# Add CellTiter Glo 2.0 reagent
...

# Shake and incubate
...

# End of protocol
