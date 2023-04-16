from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Opentrons Helper',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tuberack = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', 3)

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tuberack.wells_by_name()['A1']  # PBS(-)
    dmem = tuberack.wells_by_name()['A2']  # D-MEM

    # Medium exchange
    for well in six_well_plate.wells():
        # Remove old medium
        p300.pick_up_tip()
        p300.aspirate(1000, well)
        p300.dispense(1000, pbs.top())  # Discard old medium into PBS(-)
        p300.return_tip()

        # Wash with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(1000, pbs)
        p300.dispense(1000, well)
        p300.mix(3, 1000, well)  # Mix with PBS(-)
        p300.aspirate(1000, well)
        p300.dispense(1000, pbs.top())  # Discard PBS(-)
        p300.return_tip()

        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(1000, dmem)
        p300.dispense(1000, well)
        p300.drop_tip()
