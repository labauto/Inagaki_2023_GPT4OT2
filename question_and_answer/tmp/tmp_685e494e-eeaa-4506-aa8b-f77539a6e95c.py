from opentrons import protocol_api, types

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Immunostaining iPS cells in 6-well plate'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '2')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '3')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p200_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # Prepare Immunostained iPS Cells to visualize lysosomes
    for well in six_well_plate.wells():
        # Adjust the following volumes according to the experimental requirements
        volume_staining_solution = 3  # Example value
        volume_wash_buffer = 20  # Example value

        p20.pick_up_tip()
        p20.aspirate(volume_staining_solution, well)
        p20.dispense(volume_staining_solution, well)
        p20.blow_out()
        p20.drop_tip()

        p200.pick_up_tip()
        p200.aspirate(volume_wash_buffer, well)
        p200.dispense(volume_wash_buffer, well)
        p200.blow_out()
        p200.drop_tip()
