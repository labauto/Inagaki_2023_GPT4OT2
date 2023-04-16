from opentrons import protocol_api

metadata = {
    'apiLevel': '2.8'
}

# Functions implementing steps of your experiment should be defined here

def clean_robot(ctx):
    # Your cleaning routine logic using ctx commands
    pass

def cell_count(ctx):
    # Your cell counting logic using ctx commands
    pass

def seed_cells(ctx):
    # Your cell seeding logic using ctx commands
    pass

def drug_dilution(ctx):
    # Your drug dilution logic using ctx commands
    pass

def drug_addition(ctx):
    # Your drug addition logic using ctx commands
    pass

def celltox_green_assay(ctx):
    # Your CellTox Green assay logic using ctx commands
    pass

def cell_titer_glo_assay(ctx):
    # Your Cell Titer Glo assay logic using ctx commands
    pass

def read_fluorescence(ctx):
    # Your fluorescence reading logic using ctx commands
    pass

def orbital_shaking(ctx, rpm, duration):
    # Your orbital shaking logic using ctx commands
    pass

def incubate(ctx, duration):
    # Your incubation logic using ctx commands
    pass

def run(ctx: protocol_api.ProtocolContext):
    # Run your experiment steps by calling custom functions using the ctx instance
    clean_robot(ctx)
    cell_count(ctx)
    seed_cells(ctx)
    drug_dilution(ctx)
    drug_addition(ctx)
    celltox_green_assay(ctx)
    orbital_shaking(ctx, 500, 2)
    incubate(ctx, 15)
    read_fluorescence(ctx)
    cell_titer_glo_assay(ctx)
    orbital_shaking(ctx, 500, 2)
    incubate(ctx, 10)
    # Add any additional steps or logic needed for your experiment
