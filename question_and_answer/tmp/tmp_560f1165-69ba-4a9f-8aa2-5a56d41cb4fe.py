from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'MSC spheroid culture',
    'author': 'Your Name Here',
    'description': 'Automated culture of MSC spheroids in 96-well plates using Opentrons liquid handler',
    'apiLevel': '2.11'
}

# define labware
well_plate_96 = "corning_96_wellplate_360ul_flat"
well_plate_6 = "corning_6_wellplate_16.8ml_flat"
tiprack = 'opentrons_96_tiprack_300ul'

# define pipette
pipette_type = 'p300_multi'
pipette_mount = 'right'

# define parameters
num_spheroids = 2500
osteosupps = {'Dex': 0.1, 'AA': 1, 'BGP': 1}  # volume in microliters

def transfer_medium(dest_plate, dest_well, medium_vol):
    pipette.pick_up_tip()
    pipette.aspirate(medium_vol, medium)
    pipette.dispense(medium_vol, dest_plate[dest_well])
    pipette.drop_tip()

def add_osteosupps(dest_plate, dest_well, supp_vol_dict):
    pipette.pick_up_tip()
    for supp, vol in supp_vol_dict.items():
        pipette.aspirate(vol, osteosupps[supp])
        pipette.dispense(vol, dest_plate[dest_well])
    pipette.drop_tip()

def transfer_cells(dest_plate, dest_well, num_cells):
    pipette.pick_up_tip()
    pipette.aspirate(num_cells/25, cell_suspension)
    pipette.dispense(num_cells/25, dest_plate[dest_well])
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    # define labware
    plate1 = protocol.load_labware(well_plate_96, 1, 'Destination plate (OS-)')
    plate2 = protocol.load_labware(well_plate_96, 2, 'Destination plate (OS+)')
    cell_plate = protocol.load_labware(well_plate_6, 3, 'Source plate (hMSCs)')
    tip_rack = protocol.load_labware(tiprack, 4, 'Tip Rack')

    # define pipette
    pipette = protocol.load_instrument(pipette_type, mount=pipette_mount, tip_racks=[tip_rack])

    # define solutions
    medium = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", 5)['A1']
    osteosupps['Dex'] = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", 6)['A1']
    osteosupps['AA'] = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", 7)['A1']
    osteosupps['BGP'] = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", 8)['A1']
    cell_suspension = protocol.load_labware(well_plate_6, 9)['A1']

    # transfer medium (DMEM) to all wells in both plates
    for dest_plate, num_plates in [(plate1, 6), (plate2, 12)]:
        pipette.pick_up_tip()
        for i in range(num_plates):
            pipette.aspirate(100, medium)
            pipette.dispense(100, dest_plate[i])
        pipette.drop_tip()

    # add osteoinduction supplements to OS+ plate
    for i in range(6, 12):
        add_osteosupps(plate2, i, osteosupps)

    # transfer cells to all wells
    for dest_plate in [plate1, plate2]:
        for i in range(96):
            transfer_cells(dest_plate, i, num_spheroids)
