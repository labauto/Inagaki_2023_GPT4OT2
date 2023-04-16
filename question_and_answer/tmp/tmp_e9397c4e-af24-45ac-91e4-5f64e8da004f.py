from opentrons import protocol_api

metadata = {'apiLevel': '2.8'}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    pbs_tube = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 2)
    scm130_tube = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 3)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    # Pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Locations
    pbs = pbs_tube.wells()[0]           # PBS location
    scm130 = scm130_tube.wells()[0]     # SCM130 location
    wells = six_well_plate.wells()      # Cell culture wells

    # Exchange cell culture medium
    for well in wells:
        pipette.pick_up_tip()
        
        # Remove PBS(-)
        pipette.aspirate(300, pbs)
        pipette.dispense(300, well)

        # Remove SCM130
        pipette.aspirate(300, scm130)
        pipette.dispense(300, well)

        pipette.drop_tip()
