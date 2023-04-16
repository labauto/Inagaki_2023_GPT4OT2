from opentrons import protocol_api

metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name',
    'description': 'Description of my protocol',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # your protocol code goes here
