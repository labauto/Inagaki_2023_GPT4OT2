from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Lysosome Visualization',
    'author': 'Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tips_200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', '2')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips_200ul])

    # Wells for cell culture
    cell_culture_wells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']

    # Protocol steps
    cells = [six_well_plate.wells_by_name()[well] for well in cell_culture_wells]

    for cell in cells:
        p300.pick_up_tip()
        p300.aspirate(100, cell)
        p300.dispense(100, cell)
        p300.blow_out()
        p300.drop_tip()
