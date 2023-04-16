# Importing required libraries
from opentrons import protocol_api

metadata = {'apiLevel': '2.7'}

# The run function where the protocol contents will run
def run(ctx: protocol_api.ProtocolContext):

    # Labware setup
    medium_plate = ctx.load_labware("corning_96_wellplate_360ul_flat", 1, label="Medium plate(96 wells, each 360µl)")
    cell_plate = ctx.load_labware("corning_6_wellplate_16.8ml_flat", 2, label="Cell storage plate(6 wells, each 16.8ml)")

    # Pipette setup
    p50_single = ctx.load_instrument("p50_single", "left", tip_racks=[ctx.load_labware("opentrons_96_tiprack_10ul", slot) for slot in [4, 7]])
    p300_multi = ctx.load_instrument("p300_multi", "right", tip_racks=[ctx.load_labware("opentrons_96_tiprack_200ul", slot) for slot in [3, 6]])

    # Specifying the wells to work with
    medium_source_wells = medium_plate.rows("A")
    medium_dest_wells_os_minus = medium_plate.rows("B")

    # Function to transfer the medium
    def transfer_medium(pipette, sources, destinations):
        for s, d in zip(sources, destinations):
            pipette.transfer(100, s, d, new_tip='never')

    # Transfer medium to the wells of medium plate without osteoinductive supplements (OS-)
    transfer_medium(p300_multi, medium_source_wells, medium_dest_wells_os_minus)

    # Specifying the wells to work with - 2nd step
    medium_source_wells = medium_plate.rows("C")
    medium_dest_wells_os_plus = medium_plate.rows("D")

    # Function to add osteoinductive supplements
    def add_supplements(pipette, source, dest, supplement):
        for s, d in zip(source, dest):
            pipette.transfer(supplement, s, d, new_tip='always')

    # Add supplements to the wells of medium plate with osteoinductive supplements (OS+)
    dexamethasone_volume = 0.1  # µl
    ascorbic_acid_volume = 1  # µl
    b_glycerol_volume = 1  # µl
    add_supplements(p50_single, medium_source_wells, medium_dest_wells_os_plus, [dexamethasone_volume, ascorbic_acid_volume, b_glycerol_volume])

    # Specifying the wells to work with - 3rd step
    cell_source_wells = cell_plate.wells()[:2]
    cell_dest_wells = medium_dest_wells_os_minus + medium_dest_wells_os_plus

    # Function to transfer the hMSC cells
    def transfer_cells(pipette, sources, destinations):
        for s, d in zip(sources, destinations):
            pipette.transfer(100, s, d, new_tip='always')

    # Transfer hMSC cells to the wells in both medium plates
    transfer_cells(p300_multi, cell_source_wells, cell_dest_wells)

