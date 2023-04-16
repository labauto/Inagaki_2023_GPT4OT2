# Opentrons API
from opentrons import protocol_api

def clean_robot(ctx):
    """
    Step 0: Clean the inside of the robot to prevent contamination
    """
    # Add cleaning logic here
    pass


def seed_cells(ctx):
    """
    Step 1-3: Seed A549 cells in a 96 well plate
    """
    # Define labware and locations
    plate = ctx.load_labware('96-well-plate', location='9')
    cell_suspension_tubes = ctx.load_labware('1.5mL-snap-cap', location='6')
    p300 = ctx.load_instrument('p300_single', mount='left')

    for row in cell_suspension_tubes.rows():
        for well in plate.rows():
            p300.pick_up_tip()
            p300.aspirate(60, row)
            p300.dispense(60, well)
            p300.drop_tip()


def prepare_drug_dilutions(ctx):
    """
    Steps 6-9: Prepare thapsigargin dilutions
    """
    # Define labware and locations
    tubes_slot_7 = ctx.load_labware('2mL-screw-cap', location='7')

    # Add dilution logic here
    pass


def add_drug_concentrations(ctx):
    """
    Step 9: Add thapsigargin dilutions to the 96 well plate
    """
    # Define labware and locations
    plate = ctx.load_labware('96-well-plate', location='9')
    drug_stock_tubes = ctx.load_labware('2mL-screw-cap', location='7')
    p300 = ctx.load_instrument('p300_single', mount='left')

    # Add transfer logic here
    pass


def analyze_cells(ctx):
    """
    Steps 10-17: Analyze cell viability and cytotoxicity
    """
    # Define labware and locations
    plate = ctx.load_labware('96-well-plate', location='9')
    reagent_tubes = ctx.load_labware('10-tube-rack', location='8')
    p20 = ctx.load_instrument('p20_single_gen2', mount='left')
    p300 = ctx.load_instrument('p300_single_gen2', mount='right')

    # Add CellTox Green reagent
    for well in plate.wells():
        p20.pick_up_tip()
        p20.aspirate(15, reagent_tubes.wells_by_name()['B2'])
        p20.dispense(15, well)
        p20.drop_tip()

    # Add CellTiter Glo reagent
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(80, reagent_tubes.wells_by_name()['B1'])
        p300.dispense(80, well)
        p300.drop_tip()

    # Add further steps for orbital shaking, incubation, and more
    pass


def main(ctx: protocol_api.ProtocolContext):
    # Clean robot
    clean_robot(ctx)

    # Seed cells in the 96 well plate
    seed_cells(ctx)

    # Prepare thapsigargin dilutions
    prepare_drug_dilutions(ctx)

    # Add thapsigargin dilutions to the 96 well plate
    add_drug_concentrations(ctx)

    # Analyze cell viability and cytotoxicity
    analyze_cells(ctx)
    

if __name__ == '__main__':
    main()
