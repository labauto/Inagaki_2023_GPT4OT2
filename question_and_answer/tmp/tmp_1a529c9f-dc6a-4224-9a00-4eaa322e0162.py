from opentrons import protocol_api

metadata = {
    'apiLevel': '2.6',
    'protocolName': 'hMSC cell culture medium exchange',
    'author': 'Assistant',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and SCM130.',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '10')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '5')
    reagent_container = protocol.load_labware('nest_12_reservoir_15ml', '8')

    # Pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs_minus = reagent_container.wells_by_name()['A1']
    scm130 = reagent_container.wells_by_name()['A2']
    
    # Protocol
    for well in well_plate.wells():
        # Remove old medium
        pipette.pick_up_tip()
        pipette.aspirate(200, well)
        pipette.dispense(200, pbs_minus)
        pipette.drop_tip()

        # Wash with PBS(-)
        pipette.pick_up_tip()
        pipette.aspirate(200, pbs_minus)
        pipette.dispense(200, well)
        pipette.return_tip()

        # Add fresh SCM130 medium
        pipette.pick_up_tip()
        pipette.aspirate(200, scm130)
        pipette.dispense(200, well)
        pipette.drop_tip()

    protocol.comment('hMSC cell culture medium exchange completed.')
