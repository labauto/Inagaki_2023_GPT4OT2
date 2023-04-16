def main(ctx):
    ctx.comment("Starting the experiment")
    seeding_cells(ctx)
    ctx.delay(seconds=12 * 60 * 60)  # 12 to 16 hours delay
    drug_dilution_preparation(ctx)
    drug_addition_to_wells(ctx)
    ctx.delay(seconds=72 * 60 * 60)  # 72 hours delay
    cytotoxicity_measurement(ctx)
    cell_viability_measurement(ctx)
    ctx.comment("Experiment completed")
