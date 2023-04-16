from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Exchange hMSC cell culture medium',
    'author': 'Your Name',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate.',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '3')
    tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '1')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300ul])

    # Reagent wells
    pbs_minus = tuberack.wells_by_name()['A1']
    d_mem = tuberack.wells_by_name()['A2']

    # Perform the medium exchange for each well in the 6-well plate
    for i, well in enumerate(plate.wells()):
        # Aspirate old medium and discard
        p300.pick_up_tip()
        p300.aspirate(200, well)
        p300.dispense(200, pbs_minus)
        p300.drop_tip()

        # Wash with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(200, pbs_minus)
        p300.dispense(200, well)
        p300.mix(3, 150, well)  # Mix to remove any remaining medium
        p300.aspirate(200, well)
        p300.dispense(200, pbs_minus)
        p300.drop_tip()

        # Add new D-MEM
        p300.pick_up_tip()
        p300.aspirate(200, d_mem)
        p300.dispense(200, well)
        p300.mix(3, 150, well)  # Mix to ensure proper distribution of the medium
        p300.drop_tip()
