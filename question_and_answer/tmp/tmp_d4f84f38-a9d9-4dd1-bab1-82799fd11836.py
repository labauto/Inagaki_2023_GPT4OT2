import json
from opentrons import protocol_api

# Load labware definition
with open('path/to/usascientific_6_reservoir_15ml.json') as labware_file:
    labware_def = json.load(labware_file)

# Define protocol
metadata = {
    'protocolName': 'example_protocol',
    'author': 'Your Name Here',
    'description': 'An example protocol using custom labware'
}

def run(protocol: protocol_api.ProtocolContext):
  
  # Load labware from definition
  medium_reservoir = protocol.load_labware_from_definition(labware_def, location='2')
  
  # continue with experiment...
