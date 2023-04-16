# Import the required modules
from opentrons import protocol_api

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    pcr_plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    reagent_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Load pipettes
    left_pipette = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_200ul])

    # Define the transfer volume (in µL)
    transfer_vol = 100

    # Add medium to the OS- plate
    for well in pcr_plate_96.wells():
        left_pipette.transfer(transfer_vol, reagent_plate.wells_by_name()['A1'], well)

    # Add medium and supplements to the OS+ plate
    for well in pcr_plate_96.wells():
        left_pipette.transfer(transfer_vol, reagent_plate.wells_by_name()['A2'], well)
        left_pipette.transfer(0.1, reagent_plate.wells_by_name()['B2'], well)
        left_pipette.transfer(1, reagent_plate.wells_by_name()['C2'], well)
        left_pipette.transfer(1, reagent_plate.wells_by_name()['D2'], well)

    # Add cells to both plates
    for well in pcr_plate_96.wells():
        left_pipette.transfer(transfer_vol, reagent_plate.wells_by_name()['A3'], well)

