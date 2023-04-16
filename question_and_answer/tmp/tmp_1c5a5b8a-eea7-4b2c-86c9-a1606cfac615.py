# Import the required Opentrons modules
from opentrons import simulate, protocol_api

# Create a protocol object using API version 2.0
metadata = {'apiLevel': '2.0'}
protocol = protocol_api.ProtocolContext(metadata=metadata)

# Define the labware and pipettes
plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 2)
p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack])

# Define the reagents and samples
wash_buffer = protocol.load_labware('nest_12_reservoir_15ml', 3).wells()[:2]
fixative = protocol.load_labware('nest_12_reservoir_15ml', 3).wells(2)
primary_antibody = protocol.load_labware('nest_12_reservoir_15ml', 3).wells(3)
secondary_antibody = protocol.load_labware('nest_12_reservoir_15ml', 3).wells(4)
hMSC_cells = plate.wells()[:6]

# Define the protocol steps
def run_protocol():
    # Add fixative to the cells and incubate
    for well in hMSC_cells:
        p20.pick_up_tip()
        p20.transfer(2, fixative, well, new_tip='never')
        p20.mix(3, 10, well)
        p20.drop_tip()

    protocol.pause('Incubate for 10 minutes at room temperature.')
    
    # Wash the cells with buffer
    for well in hMSC_cells:
        for buffer in wash_buffer:
            p20.pick_up_tip()
            p20.transfer(20, buffer, well, new_tip='never')
            p20.mix(3, 10, well)
            p20.drop_tip()
            
    # Add primary antibody and incubate
    for well in hMSC_cells:
        p20.pick_up_tip()
        p20.transfer(2, primary_antibody, well, new_tip='never')
        p20.mix(3, 10, well)
        p20.drop_tip()

    protocol.pause('Incubate for 1 hour at room temperature.')
    
    # Wash the cells with buffer
    for well in hMSC_cells:
        for buffer in wash_buffer:
            p20.pick_up_tip()
            p20.transfer(20, buffer, well, new_tip='never')
            p20.mix(3, 10, well)
            p20.drop_tip()
    
    # Add secondary antibody and incubate
    for well in hMSC_cells:
        p20.pick_up_tip()
        p20.transfer(2, secondary_antibody, well, new_tip='never')
        p20.mix(3, 10, well)
        p20.drop_tip()

    protocol.pause('Incubate for 1 hour at room temperature.')
    
    # Wash the cells with buffer
    for well in hMSC_cells:
        for buffer in wash_buffer:
            p20.pick_up_tip()
            p20.transfer(20, buffer, well, new_tip='never')
            p20.mix(3, 10, well)
            p20.drop_tip()

# Run the protocol
run_protocol()
