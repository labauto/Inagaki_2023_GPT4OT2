from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Making hMSC spheroids',
    'author': 'Your Name <youremail@yourinstitution.com>',
    'description': 'Make hMSC spheroids with and without OS+ and OS- conditions',
    'apiLevel': '2.11'
}


def transfer_medium(pipette, source, dest):
    pipette.pick_up_tip()
    for s, d in zip(source, dest):
        pipette.transfer(100, s, d, new_tip='never')
    pipette.drop_tip()

    
def add_os_plus(pipette, source, dest):
    pipette.pick_up_tip()
    for s, d in zip(source, dest):
        pipette.transfer(0.1, source[0], d, new_tip='never')
        pipette.transfer(1, source[1], d, new_tip='never')
        pipette.transfer(1, source[2], d, new_tip='never')
    pipette.drop_tip()


def transfer_cells(pipette, source, dest):
    pipette.pick_up_tip()
    for s, d in zip(source, dest):
        pipette.transfer(100, s, d, new_tip='never')
    pipette.drop_tip()


def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    cell_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    medium_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Load pipettes
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tip_rack])

    # Define source and destination wells for each step
    medium_source_wells = medium_plate.columns()[0]
    medium_dest_wells_os_minus = cell_plate.columns()
    medium_dest_wells_os_plus = cell_plate.columns()[1]

    os_plus_wells = cell_plate.columns()[1]
    os_minus_wells = cell_plate.columns()[0]

    cell_source_wells = cell_plate.columns()[0]

    # Transfer medium
    transfer_medium(p300_multi, medium_source_wells, medium_dest_wells_os_minus)
    transfer_medium(p300_multi, medium_source_wells, medium_dest_wells_os_plus)

    # Add OS+ supplements to OS+ wells
    add_os_plus(p300_multi, medium_source_wells[-3:], os_plus_wells)

    # Transfer cells
    transfer_cells(p300_multi, cell_source_wells, os_minus_wells)
    transfer_cells(p300_multi, cell_source_wells, os_plus_wells)
