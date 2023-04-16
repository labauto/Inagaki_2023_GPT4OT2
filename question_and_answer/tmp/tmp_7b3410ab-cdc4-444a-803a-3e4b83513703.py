from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # Load pipette
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300ul])

    # Prepare immunostained iPS cells to visualize lysosomes
    # The specific protocol details are not provided, so this is a general example
    cell_well = plate.wells_by_name()['A1']
    pipette.pick_up_tip()
    pipette.mix(5, 150, cell_well)
    pipette.drop_tip()
