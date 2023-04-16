# Import the necessary libraries
from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Immunostaining hMSC Cells for Lysosome Visualization',
    'author': 'Your name here',
    'description': 'Protocol for immunostaining hMSC cells on a 6-well plate for visualization of lysosomes',
    'apiLevel': '2.4'
}

# Define the `run(ctx)` function
def run(ctx: protocol_api.ProtocolContext):

    # Define the deck layout
    tiprack_1000 = ctx.load_labware('opentrons_96_tiprack_1000ul', '1')
    plate_6_well = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reagent_plate = ctx.load_labware('nest_96_wellplate_2ml_deep', '3')
    waste_reservoir = ctx.load_labware('nest_1_reservoir_195ml', '10')

    # Define the pipettes
    p1000 = ctx.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Define the reagents
    primary_antibody = reagent_plate['A1']
    secondary_antibody = reagent_plate['A2']
    dapi = reagent_plate['A3']

    # Define the wells
    sample_wells = plate_6_well.columns_by_name()['1']

    # Add primary antibody
    for well in sample_wells:
        p1000.pick_up_tip()
        p1000.transfer(200, primary_antibody, well, new_tip='never')
        p1000.drop_tip()

    # Wash 1
    for well in sample_wells:
        p1000.pick_up_tip()
        p1000.transfer(1000, waste_reservoir, well, new_tip='never')
        p1000.drop_tip()

    # Add secondary antibody
    for well in sample_wells:
        p1000.pick_up_tip()
        p1000.transfer(200, secondary_antibody, well, new_tip='never')
        p1000.drop_tip()

    # Wash 2
    for well in sample_wells:
        p1000.pick_up_tip()
        p1000.transfer(1000, waste_reservoir, well, new_tip='never')
        p1000.drop_tip()

    # Add DAPI
    for well in sample_wells:
        p1000.pick_up_tip()
        p1000.transfer(200, dapi, well, new_tip='never')
        p1000.drop_tip()

    ctx.comment('Protocol complete.')
