from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Medium Exchange',
    'author': 'Your Name <youremail@domain.com>',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    tuberack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
    cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    d_mem = tuberack.wells_by_name()['A2']

    # Procedure
    for well in cell_plate.wells():
        # Aspirate 1 mL of medium from well
        p300.pick_up_tip()
        p300.aspirate(1000, well)
        p300.dispense(1000, well)
        p300.drop_tip()

        # Add 2 mL of PBS(-) to each well
        p300.pick_up_tip()
        p300.aspirate(800, pbs_minus)
        p300.dispense(800, well)
        p300.aspirate(200, pbs_minus)
        p300.dispense(200, well)
        p300.drop_tip()

        # Aspirate 2 mL of PBS(-) and medium from each well
        p300.pick_up_tip()
        p300.aspirate(1000, well)
        p300.dispense(1000, well)
        p300.aspirate(1000, well)
        p300.dispense(1000, well)
        p300.drop_tip()

        # Add 2 mL of D-MEM to each well
        p300.pick_up_tip()
        p300.aspirate(800, d_mem)
        p300.dispense(800, well)
        p300.aspirate(200, d_mem)
        p300.dispense(200, well)
        p300.drop_tip()
