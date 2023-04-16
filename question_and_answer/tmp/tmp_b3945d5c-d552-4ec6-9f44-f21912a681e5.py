from opentrons import protocol_api

# constants
DEST_PLATE_TYPE = 'corning_96_wellplate_360ul_flat'
SOURCE_PLATE_TYPE = 'corning_6_wellplate_16.8ml_flat'
VOL_MEDIUM = 100
VOL_SUPPLEMENTS_D = 0.1
VOL_SUPPLEMENTS_AA = 1
VOL_SUPPLEMENTS_BGP = 1
VOL_CELLS = 100

DEX = 'Dexamethasone'
AA = 'Ascorbic acid'
BGP = 'beta-glycerophosphate'

def transfer_medium_to_os(pos, dest_plate):
    dest_well = dest_plate[pos]
    pipette.aspirate(VOL_MEDIUM, medium_source)
    pipette.dispense(VOL_MEDIUM, dest_well)

def add_supplements_to_os(pos, dest_plate):
    dest_well = dest_plate[pos]
    pipette.aspirate(VOL_SUPPLEMENTS_D, d_source)
    pipette.dispense(VOL_SUPPLEMENTS_D, dest_well)
    pipette.aspirate(VOL_SUPPLEMENTS_AA, aa_source)
    pipette.dispense(VOL_SUPPLEMENTS_AA, dest_well)
    pipette.aspirate(VOL_SUPPLEMENTS_BGP, bgp_source)
    pipette.dispense(VOL_SUPPLEMENTS_BGP, dest_well)

def transfer_cells_to_os(pos, dest_plate):
    dest_well = dest_plate[pos]
    pipette.aspirate(VOL_CELLS, cells_source)
    pipette.dispense(VOL_CELLS, dest_well)

def run(protocol: protocol_api.ProtocolContext):
    # labwares
    medium_source = protocol.load_labware(
        SOURCE_PLATE_TYPE, '1', 'DMEM medium source').wells()[0]
    os_pos_dest_plate = protocol.load_labware(
        DEST_PLATE_TYPE, '2', 'OS(+) destination plate').wells()
    os_neg_dest_plate = protocol.load_labware(
        DEST_PLATE_TYPE, '3', 'OS(-) destination plate').wells()
    cells_source = protocol.load_labware(
        SOURCE_PLATE_TYPE, '4', 'Cells source').wells()[0]
    d_source = protocol.load_labware(
        SOURCE_PLATE_TYPE, '5', 'Dex source').wells()[0]
    aa_source = protocol.load_labware(
        SOURCE_PLATE_TYPE, '6', 'AA source').wells()[0]
    bgp_source = protocol.load_labware(
        SOURCE_PLATE_TYPE, '7', 'BGP source').wells()[0]
    
    # pipette
    pipette = protocol.load_instrument(
        'p300_single_gen2', 'right', tip_racks=[protocol.load_labware(
            'opentrons_96_tiprack_300ul', '8')])

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for well in os_neg_dest_plate:
        pipette.aspirate(VOL_MEDIUM, medium_source)
        pipette.dispense(VOL_MEDIUM, well)

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for well in os_pos_dest_plate:
        pipette.aspirate(VOL_MEDIUM, medium_source)
        pipette.dispense(VOL_MEDIUM, well)

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), 
    # and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for i, well in enumerate(os_pos_dest_plate):
        add_supplements_to_os(i, os_pos_dest_plate)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in os_neg_dest_plate:
        pipette.aspirate(VOL_CELLS, cells_source)
        pipette.dispense(VOL_CELLS, well)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in os_pos_dest_plate:
        pipette.aspirate(VOL_CELLS, cells_source)
        pipette.dispense(VOL_CELLS, well)
