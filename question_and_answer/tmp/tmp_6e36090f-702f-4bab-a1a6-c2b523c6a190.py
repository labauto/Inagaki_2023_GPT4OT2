from opentrons import protocol_api

metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name',
    'description': 'Description of my protocol',
    'apiLevel': '2.0'
}


def run(ctx: protocol_api.ProtocolContext):
    # Protocol steps go here
    ctx.comment('Hello, world!')
