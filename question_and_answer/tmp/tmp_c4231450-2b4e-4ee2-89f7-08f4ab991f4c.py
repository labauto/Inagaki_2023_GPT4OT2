from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC cell culture medium exchange',
    'author': 'Your Name <youremail@example.com>',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')  # 6 well plate for cell culture
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '2')  # 15 mL tube rack for PBS(-) and D-MEM

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right')

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    d_mem = tuberack.wells_by_name()['A2']

    # Protocol
    for well in plate.wells():
        p1000.pick_up_tip()

        # Aspirate cell culture medium
        p1000.aspirate(750, well.bottom(z=2))  # 750µL or appropriate volume based on cell culture
        p1000.dispense(750, well.bottom(z=2))  # Empty aspirated cell culture medium into waste container

        # Wash with PBS(-)
        p1000.aspirate(750, pbs_minus)
        p1000.dispense(750, well.bottom(z=2))
        p1000.aspirate(750, well.bottom(z=2))  # Aspirate PBS(-) after washing
        p1000.dispense(750, well.bottom(z=2))  # Empty aspirated PBS(-) into waste container

        # Add D-MEM
        p1000.aspirate(750, d_mem)
        p1000.dispense(750, well.bottom(z=2))

        p1000.drop_tip()
