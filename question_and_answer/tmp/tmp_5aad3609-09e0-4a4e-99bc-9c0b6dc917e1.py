from opentrons import protocol_api

metadata = {
    'protocolName': 'viability_and_cytotoxicity_measurement',
    'author': 'Your Name <youremail@example.com>',
    'apiLevel': '2.10',
}

def prepare_cells():
    # Your cell preparation steps here
    pass

def prepare_thapsigargin_dilutions():
    # Your thapsigargin preparation steps here
    pass

def add_celltox_green_reagent():
    # Your CellTox Green reagent steps here
    pass

def add_cell_titer_glo_reagent():
    # Your Cell Titer Glo reagent steps here
    pass

def main(ctx: protocol_api.ProtocolContext):
    # Clean the inside of the robot
    # Turn on the HEPA filter
    # Prepare cells and count
    prepare_cells()

    # Seed cells in the 96 well plate
    # Add medium as negative control
    # Dilute thapsigargin and treat cells
    prepare_thapsigargin_dilutions()

    # Wait 72 hours (simulation will not wait, it's just a placeholder)
    ctx.delay(hours=72)

    # Add CellTox Green reagent
    add_celltox_green_reagent()

    # Read cell fluorescence
    # Read cell luminescence
    pass

def run(ctx: protocol_api.ProtocolContext):
    main(ctx)
