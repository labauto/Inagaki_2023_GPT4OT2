from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS Cell Culture Medium Exchange',
    'author': 'Opentrons',
    'description': 'Exchange medium in a 6-well plate using PBS(-) and SCM130',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    pbs_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_15ml_conical', '3')
    scm130_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_15ml_conical', '6')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # Pipettes
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Wells
    pbs_well = pbs_tuberack.wells_by_name()['A1']
    scm130_well = scm130_tuberack.wells_by_name()['A1']

    # Perform medium exchange
    for well in ['A1', 'A3', 'B1', 'B3', 'C2']:
        dest = six_well_plate.wells_by_name()[well]
        
        # Remove old medium with PBS(-)
        pipette.pick_up_tip()
        pipette.transfer(1000, pbs_well, dest, new_tip='never')
        pipette.blow_out(dest)
        pipette.drop_tip()

        # Add fresh SCM130 medium
        pipette.pick_up_tip()
        pipette.transfer(1000, scm130_well, dest, new_tip='never')
        pipette.blow_out(dest)
        pipette.drop_tip()
