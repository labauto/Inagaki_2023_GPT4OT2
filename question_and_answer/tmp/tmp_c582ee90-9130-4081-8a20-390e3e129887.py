from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your Name',
    'description': 'Automated hMSC spheroid culture with or without osteoinduction supplements using Opentrons',
    'apiLevel': '2.10'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):

    # Load the 6-well plate and the 96-well plate
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')

    # Define the pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', mount='left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul_tiprack', '4')])

    # Add growth supplements to the Os+ plate
    dexamethasone = os_plus_plate.cols()[0].top(-5)
    ascorbic_acid = os_plus_plate.cols()[0].top(-10)
    beta_glycerophosphate = os_plus_plate.cols()[0].top(-15)
    p1000.pick_up_tip()
    p1000.aspirate(0.1, dexamethasone)
    p1000.aspirate(1, ascorbic_acid)
    p1000.aspirate(1, beta_glycerophosphate)
    p1000.dispense(2.1, os_plus_plate.cols()[0])
    p1000.drop_tip()

    # Add medium to both plates
    for col in os_minus_plate.cols() + os_plus_plate.cols():
        p1000.pick_up_tip()
        p1000.aspirate(100, six_well_plate.wells()[0].bottom(0.5))
        p1000.dispense(100, col)
        p1000.drop_tip()

    # Add cells to both plates
    for col in os_minus_plate.cols() + os_plus_plate.cols():
        p1000.pick_up_tip()
        p1000.aspirate(100, six_well_plate.wells()[1].bottom())
        p1000.dispense(100, col)
        p1000.drop_tip()
