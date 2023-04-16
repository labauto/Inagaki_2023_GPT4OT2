from opentrons import protocol_api

# labware setup
def setup_labware():
    tiprack_200 = ctx.load_labware("opentrons_96_tiprack_300ul", 3)
    pipette_200 = ctx.load_instrument("p300_multi_gen2", 'left', tip_racks=[tiprack_200])

    # plate setup
    plate_96_osminus = ctx.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate_96_osplus = ctx.load_labware('corning_96_wellplate_360ul_flat', 2)
    
    # trough setup
    trough = ctx.load_labware('usascientific_12_reservoir_22ml', 4)
    loc_dmem_osminus = trough['A1']
    loc_dmem_osplus = trough['A2']
    loc_dex = trough['A3']
    loc_ascorbic_acid = trough['A4']
    loc_bgp = trough['A5']

    return(pipette_200, plate_96_osminus, plate_96_osplus, trough, 
           loc_dmem_osminus, loc_dmem_osplus, loc_dex, loc_ascorbic_acid, loc_bgp)

# step 1: Transfer DMEM to OS- plate
def transfer_dmem_osminus(protocol, plate, pipette):
    loc_dmem_osminus = trough['A1']
    for row in plate.rows():
        pipette.pick_up_tip()
        pipette.transfer(100, loc_dmem_osminus, row, new_tip='never')
        pipette.drop_tip()

# step 2: Transfer DMEM+supplements to OS+ plate
def transfer_dmem_plus_supplements(protocol, plate, pipette):
    loc_dmem_osplus = trough['A2']
    loc_dex = trough['A3']
    loc_ascorbic_acid = trough['A4']
    loc_bgp = trough['A5']
    for row in plate.rows():
        pipette.pick_up_tip()
        pipette.transfer(100, loc_dmem_osplus, row, new_tip='never')
        pipette.transfer(0.1, loc_dex, row, new_tip='never')
        pipette.transfer(1, loc_ascorbic_acid, row, new_tip='never')
        pipette.transfer(1, loc_bgp, row, new_tip='never')
        pipette.drop_tip()

# step 3: Transfer cells to both plates
def transfer_cells_to_both_plates(protocol, plate_96_osminus, plate_96_osplus, pipette):
    loc_source = plate_6_well['A1']
    for dest_osminus, dest_osplus in zip(plate_96_osminus.rows(), plate_96_osplus.rows()):
        pipette.pick_up_tip()
        pipette.transfer(100, loc_source, dest_osminus, new_tip='never')
        pipette.transfer(100, loc_source, dest_osplus, new_tip='never')
        pipette.drop_tip()

# main function
def run(protocol: protocol_api.ProtocolContext):
    pipette_200, plate_96_osminus, plate_96_osplus, trough, loc_dmem_osminus, loc_dmem_osplus, loc_dex, loc_ascorbic_acid, loc_bgp = setup_labware()

    # steps of the protocol
    transfer_dmem_osminus(protocol, plate_96_osminus, pipette_200)
    transfer_dmem_plus_supplements(protocol, plate_96_osplus, pipette_200)
    transfer_cells_to_both_plates(protocol, plate_96_osminus, plate_96_osplus, pipette_200)

