from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    trough = protocol.load_labware('usascientific_12_reservoir_22ml', 2)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 3)

    # Pipette
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Reagents
    primary_antibody = trough['A1']
    secondary_antibody = trough['A2']
    fixative = trough['A3']

    # Protocol
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, fixative, well, mix_after=(3, 100), new_tip='never')
        p300.drop_tip()

    protocol.delay(minutes=15)

    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, primary_antibody, well, mix_after=(3, 200), new_tip='never')
        p300.drop_tip()

    protocol.delay(minutes=60)

    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, secondary_antibody, well, mix_after=(3, 200), new_tip='never')
        p300.drop_tip()

    protocol.delay(minutes=30)
