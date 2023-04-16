# Import necessary modules
from opentrons import protocol_api

# Metadata
metadata = {'apiLevel': '2.0', 'protocolName': 'Immunostaining hMSC Cells for Lysosomes'}

# Initialize protocol API
protocol = protocol_api.ProtocolContext(metadata=metadata)

# Define the protocol run function
def run(protocol):
    
    # Load the 6-well plate onto the Opentrons deck
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    
    # Load the reagents onto the Opentrons deck
    PBS_buffer = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    block_solution = protocol.load_labware('usascientific_12_reservoir_22ml', '3')
    
    # Define the pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '4')])
    p300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '5')])
    
    # Transfer 1 ml of PBS to each well
    for well in plate_6_well.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, PBS_buffer['A1'])
        p1000.dispense(1000, well)
        p1000.mix(5, 500)
        p1000.drop_tip()
    
    # Transfer 200 µl of block solution to each well and incubate for 30 min.
    for well in plate_6_well.wells():
        p300.pick_up_tip()
        p300.aspirate(200, block_solution['A1'])
        p300.dispense(200, well)
        p300.mix(5, 150)
        p300.drop_tip()
        
    protocol.incubate(30, wait_minutes=30,
                      tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '6'),
                              protocol.load_labware('opentrons_96_tiprack_300ul', '7')],
                      trash_container=protocol.fixed_trash[0])
    
    # Wash the cells with PBS
    for well in plate_6_well.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, PBS_buffer['A1'])
        p1000.dispense(1000, well)
        p1000.mix(5, 500)
        p1000.drop_tip()
    
    protocol.comment("Protocol complete!")

