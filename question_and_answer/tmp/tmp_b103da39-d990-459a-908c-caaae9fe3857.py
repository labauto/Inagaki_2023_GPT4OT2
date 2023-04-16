def run(ctx):

    # Get Labware
    plate_6_well = ctx.load_labware("corning_6_wellplate_16.8ml_flat", "1")
    plate_96_well = ctx.load_labware("corning_96_wellplate_360ul_flat", "2")

    # Get Pipettes
    pipette_1 = ctx.load_instrument("p10_single", "left", tip_racks=[ctx.load_labware("opentrons_96_tiprack_10ul", "3")])

    # Add medium (DMEM) to each well of 96 well plate (OS-)
    pipette_1.transfer(100, ctx.loaded_labwares[1].rows_by_name()["A"], plate_96_well.rows_by_name()["A"], new_tip="always")

    # Add medium (DMEM high glucose) to each well of 96 well plate (OS+)
    pipette_1.transfer(100, ctx.loaded_labwares[1].rows_by_name()["A"], plate_96_well.rows_by_name()["B"], new_tip="always")

    # Add supplements (Dex, AA, and BGP) to each well of 96 well plate (OS+)
    pipette_1.transfer(0.1, plate_6_well.wells_by_name()["A1"], plate_96_well.rows_by_name()["B"], new_tip="always")
    pipette_1.transfer(1, plate_6_well.wells_by_name()["B1"], plate_96_well.rows_by_name()["B"], new_tip="always")
    pipette_1.transfer(1, plate_6_well.wells_by_name()["C1"], plate_96_well.rows_by_name()["B"], new_tip="always")

    # Add hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-) and (OS+)
    pipette_1.transfer(100, plate_6_well.wells_by_name()["D1"], plate_96_well.rows_by_name()["A"], new_tip="always")
    pipette_1.transfer(100, plate_6_well.wells_by_name()["E1"], plate_96_well.rows_by_name()["B"], new_tip="always") 
