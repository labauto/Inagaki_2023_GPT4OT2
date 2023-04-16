from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS Cell Culture Medium Exchange',
    'author': 'Your full Name <youremail@email.com>',
    'description': 'Automate the exchange of iPS cell culture medium using PBS(-) and D-MEM in a 6-well plate.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reagents_plate = protocol.load_labware('nest_12_reservoir_15ml', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips_300])

    # Reagents
    pbs_minus = reagents_plate['A1']
    d_mem = reagents_plate['A2']

    # Performing experiment
    for well in six_well.wells():

        # Aspirating and discarding the spent medium:
        p300.pick_up_tip()
        p300.aspirate(250, well)
        p300.dispense(250, pbs_minus)
        p300.drop_tip()

        # Washing cell with PBS(-):
        p300.pick_up_tip()
        p300.aspirate(250, pbs_minus)
        p300.dispense(250, well)
        p300.aspirate(250, well)
        p300.dispense(250, pbs_minus)
        p300.drop_tip()

        # Adding fresh D-MEM:
        p300.pick_up_tip()
        p300.aspirate(250, d_mem)
        p300.dispense(250, well)
        p300.drop_tip()
