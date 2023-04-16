# Import the Opentrons SDK
from opentrons import protocol_api

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Load the pipettes
    left_pipette = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])
    
    # Define the transfer volumes and locations
    pbs_well = [1, 4] # use wells 1 and 4 for pbs
    dmem_well = [2, 5] # use wells 2 and 5 for dmem
    volume = 200 # transfer 200 uL from each well
    
    # Perform the transfer
    for i in range(len(pbs_well)):
        left_pipette.pick_up_tip()
        left_pipette.transfer(volume, plate.columns()[pbs_well[i]], plate.columns()[dmem_well[i]], new_tip='never')
        left_pipette.drop_tip()
