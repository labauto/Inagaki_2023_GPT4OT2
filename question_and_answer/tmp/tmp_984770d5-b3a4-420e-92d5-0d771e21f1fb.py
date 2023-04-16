from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiptiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiptiprack_300ul])

    # Prepare immunostained iPS cells to visualize lysosomes
    for well in six_well_plate.wells():
        p300.pick_up_tip()
        # Add your specific steps here using p300 functions, such as "aspirate()" and "dispense()"
        p300.drop_tip()
