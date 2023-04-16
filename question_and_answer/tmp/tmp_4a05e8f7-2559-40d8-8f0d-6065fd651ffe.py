from opentrons import protocol_api

metadata = {
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '7')
    trough_12 = protocol.load_labware('usascientific_12_reservoir_22ml', '10')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Reagents
    pbs_minus = trough_12.wells_by_name()['A1']
    scm130 = trough_12.wells_by_name()['A2']

    # Exchanging iPS cell culture medium using PBS(-) and SCM130
    for well in ['A1', 'A3', 'B1', 'B3', 'C1', 'C3']:
        dest = six_well_plate.wells_by_name()[well]

        # Aspirate PBS(-)
        p300.pick_up_tip()
        p300.aspirate(200, pbs_minus)
        p300.dispense(200, dest)
        p300.blow_out(dest.top())
        p300.drop_tip()

        # Aspirate SCM130
        p300.pick_up_tip()
        p300.aspirate(200, scm130)
        p300.dispense(200, dest)
        p300.blow_out(dest.top())
        p300.drop_tip()
