from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Assistant',
    'description': 'Python script to exchange hMSC cell culture medium using PBS(-) and DMEM',
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reagent_rack = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', '2')
    tip_rack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack_300])

    # Reagents
    pbs_minus = reagent_rack.wells_by_name()['A1']
    dmem = reagent_rack.wells_by_name()['A2']

    # Protocol
    for well in plate.wells():
        # Aspirate cell culture medium
        p300.pick_up_tip()
        p300.aspirate(200, well)
        p300.dispense(200, pbs_minus)
        p300.drop_tip()

        # Wash with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(200, pbs_minus)
        p300.dispense(200, well)
        p300.mix(5, 200, well)
        p300.aspirate(200, well)
        p300.dispense(200, pbs_minus)
        p300.drop_tip()

        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(200, dmem)
        p300.dispense(200, well)
        p300.drop_tip()
