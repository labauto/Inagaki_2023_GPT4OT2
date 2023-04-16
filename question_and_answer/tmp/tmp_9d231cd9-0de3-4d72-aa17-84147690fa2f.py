from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'MSC Spheroid Culture',
    'author': 'Your Name Here',
    'description': 'Protocol for hMSC cell spheroid culture',
    'apiLevel': '2.0'
}

# map wells of both 6 well and 96 well plates
plate_6wells = "corning_6_wellplate_16.8ml_flat"
plate_96wells = "corning_96_wellplate_360ul_flat"

# experimental variables
cells_per_well = 2500  # number of cells to culture per well

# define the protocol
def run(protocol: protocol_api.ProtocolContext):
    # load the 6-well plate and the 96-well plates
    os_minus_plate = protocol.load_labware(plate_96wells, '1')
    os_plus_plate = protocol.load_labware(plate_96wells, '2')
    cell_plate = protocol.load_labware(plate_6wells, '3')

    # create lists to store wells to use
    os_minus_wells = [well for well in os_minus_plate.wells() if well.is_empty()]
    os_plus_wells = [well for well in os_plus_plate.wells() if well.is_empty()]
    cell_wells = [well for well in cell_plate.wells() if well.is_empty()]

    # add medium to each well of the 96-well plates
    for well in os_minus_wells:
        pipette_100uL(protocol, well, 'DMEM')

    for well in os_plus_wells:
        pipette_100uL(protocol, well, 'DMEM High Glucose')
        pipette_XuL(protocol, well, 'Dex', 0.1)
        pipette_XuL(protocol, well, 'AA', 1)
        pipette_XuL(protocol, well, 'BGP', 1)

    # add cells to each well of the 6-well plate
    for well in cell_wells:
        pipette_100uL(protocol, well, 'hMSC Cells')

    # transfer cells to the 96-well plates
    for i, (os_minus_well, os_plus_well) in enumerate(zip(os_minus_wells, os_plus_wells)):
        pipette_100uL(protocol, os_minus_well, cell_wells[i])
        pipette_100uL(protocol, os_plus_well, cell_wells[i])

# define helper functions
def pipette_100uL(protocol, destination, source):
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=None)
    p1000.pick_up_tip()
    p1000.transfer(100, protocol.load_labware(plate_96wells, destination),
                   protocol.load_labware(plate_6wells, source), new_tip='never')
    p1000.drop_tip()

def pipette_XuL(protocol, destination, reagent, volume):
    p10 = protocol.load_instrument('p10_single', 'right', tip_racks=None)
    p10.pick_up_tip()
    p10.transfer(float(volume), protocol.load_labware(plate_96wells, destination),
                   protocol.load_labware(plate_96wells, reagent), new_tip='never')
    p10.drop_tip()
