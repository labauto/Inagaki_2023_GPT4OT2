# Importing the required Opentrons modules
from opentrons import protocol_api

# Creating a protocol object
metadata = {'apiLevel': '2.9'}
protocol = protocol_api.ProtocolContext(metadata=metadata)


# Define a function that specifies the robot’s movements
def run(protocol):
    
    # Define the parameters for the experiment
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Transfer cell culture medium to a waste container
    p300.transfer(150, plate.wells_by_name()['A1'], plate.wells_by_name()['A1'].top(-5), new_tip='always')
    p300.transfer(150, plate.wells_by_name()['A1'], plate.wells_by_name()['A1'].top(-5), new_tip='always')
    
    # Exchange the medium with PBS(-)
    for i in range(6):
        p300.transfer(200, plate.columns()[i][0], plate.columns()[i][1].top(-5), new_tip='always')
        p300.transfer(200, plate.columns()[i][1], plate.columns()[i][0].top(-5), new_tip='always')
        p300.transfer(200, plate.columns()[i][0], plate.columns()[i][1].top(-5), new_tip='always')

    # Exchange the medium with SCM130
    for i in range(6):
        p300.transfer(200, plate.columns()[i][0], plate.columns()[i][1].top(-5), new_tip='always')
        p300.transfer(200, plate.columns()[i][1], plate.columns()[i][0].top(-5), new_tip='always')
        p300.transfer(200, plate.columns()[i][0], plate.columns()[i][1].top(-5), new_tip='always')
            
# Run the protocol on the specified robot            
run(protocol)
