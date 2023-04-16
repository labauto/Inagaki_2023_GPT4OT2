from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name Here <youremail@yourinstitution.com>',
    'description': 'A protocol for washing and treating cells in a 6 well plate',
    'apiLevel': '2.11'
}

# Labware setup
tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

# Pipette setup
p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

def run(protocol: protocol_api.ProtocolContext):

    # Wash 6 well plate with PBS(-)
    p1000.pick_up_tip()
    for well in range(6):
        p1000.aspirate(1000, tube_rack['A1'])
        p1000.dispense(1000, cell_plate.wells()[well])
        for i in range(5):  # pipette up and down 5 times
            p1000.aspirate(1000, cell_plate.wells()[well])
            p1000.dispense(1000, cell_plate.wells()[well])
    p1000.drop_tip()

    # Add trypsin and wait for 5 minutes
    p1000.pick_up_tip()
    for well in range(6):
        p1000.aspirate(1000, tube_rack['A2'])
        p1000.dispense(1000, cell_plate.wells()[well])
    p1000.delay(minutes=5)

    # Add cell culture medium
    p1000.pick_up_tip()
    for well in range(6):
        p1000.aspirate(1000, tube_rack['A3'])
        p1000.dispense(1000, cell_plate.wells()[well])
    p1000.drop_tip()
