from opentrons import protocol_api

metadata = {
    'author': 'Your Name',
    'description': 'Exchanging iPS cell culture medium using PBS(-) and SCM130',
    'apiLevel': '2.8'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    pbs_tube = protocol.load_labware('opentrons_24_tuberack_nest_2ml_snapcap', '4')
    scm130_tube = protocol.load_labware('opentrons_24_tuberack_nest_2ml_snapcap', '5')

    # Pipette
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Define reagent positions
    pbs = pbs_tube.wells_by_name()['A1']
    scm130 = scm130_tube.wells_by_name()['A1']

    # Variables
    total_volume = 300  # in uL
    pbs_scm130_ratio = 0.9  # for 90% PBS(-) and 10% SCM130
    pbs_volume = total_volume * pbs_scm130_ratio
    scm130_volume = total_volume - pbs_volume
    mix_volume = total_volume / 2

    wells = ['A1', 'A3', 'A5', 'B1', 'B3', 'B5']

    for well in wells:
        dest = six_well_plate.wells_by_name()[well]

        # Aspirate the medium from the well
        pipette.pick_up_tip()
        pipette.aspirate(total_volume, dest)
        pipette.dispense(total_volume, pbs_tube.wells_by_name()['A2'])  # Discard old medium
        pipette.drop_tip()

        # Transfer PBS(-)
        pipette.pick_up_tip()
        pipette.aspirate(pbs_volume, pbs)
        pipette.dispense(pbs_volume, dest)
        pipette.mix(3, mix_volume, dest)
        pipette.drop_tip()

        # Add SCM130
        pipette.pick_up_tip()
        pipette.aspirate(scm130_volume, scm130)
        pipette.dispense(scm130_volume, dest)
        pipette.mix(3, mix_volume, dest)
        pipette.drop_tip()
