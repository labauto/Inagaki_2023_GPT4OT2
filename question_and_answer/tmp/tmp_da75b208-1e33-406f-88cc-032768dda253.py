from opentrons import protocol_api

metadata = {
    "apiLevel": "2.11"
}

def transfer_medium(ctx, pipette, plate, start_well_index, volume, medium_type, dest_plate):
    for well_index in range(start_well_index, start_well_index + 48):
        pipette.transfer(volume, plate.wells(medium_type), dest_plate.wells(well_index), new_tip="always")

def add_supplements(ctx, pipette, supplements, plate):
    for well in plate.wells()[:48]:
        for supplement, volume in supplements.items():
            pipette.transfer(volume, supplement, well, mix_after=(3, 10), new_tip="always")

def transfer_cells(ctx, pipette, cells, start_well_index, dest_plate):
    for well_index in range(start_well_index, start_well_index + 48):
        pipette.transfer(100, cells, dest_plate.wells(well_index), new_tip="always")

def run(ctx: protocol_api.ProtocolContext):
    # Labware
    tiprack = ctx.load_labware("opentrons_96_tiprack_300ul", "1")
    supplement_stock_tuberack = ctx.load_labware("opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap", "2")
    medium_stock_plate = ctx.load_labware("corning_96_wellplate_360ul_flat", "3")
    cell_stock_tuberack = ctx.load_labware("opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap", "4")
    dest_plate = ctx.load_labware("corning_96_wellplate_360ul_flat", "5")

    # Reagents
    dmem_low = medium_stock_plate.wells("A1")
    dmem_high = medium_stock_plate.wells("A2")
    dex = supplement_stock_tuberack.wells("A1")
    aa = supplement_stock_tuberack.wells("A2")
    bgp = supplement_stock_tuberack.wells("A3")
    hmsc_cells = cell_stock_tuberack.wells("A1")

    supplements = {
        dex: 0.1,
        aa: 1,
        bgp: 1,
    }

    # Pipettes
    pipette = ctx.load_instrument("p300_single_gen2", "right", tip_racks=[tiprack])

    # Transferring Media
    transfer_medium(ctx, pipette, medium_stock_plate, 0, 100, "A1", dest_plate)
    transfer_medium(ctx, pipette, medium_stock_plate, 48, 100, "A2", dest_plate)

    # Adding Supplements
    add_supplements(ctx, pipette, supplements, dest_plate)

    # Transferring Cells
    transfer_cells(ctx, pipette, hmsc_cells, 0, dest_plate)
    transfer_cells(ctx, pipette, hmsc_cells, 48, dest_plate)

    ctx.comment("Experiment Finished.")
