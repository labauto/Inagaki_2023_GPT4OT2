# Import the required packages
from opentrons import protocol_api

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Define the containers holding the reagents
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_tube = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '2')
    dmem_tube = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '3')
    
    # Define the pipettes
    p50_single = protocol.load_instrument('p50_single', mount='right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_10ul', '4')])
    
    # Define the steps of the experiment
    # Step 1: Add 300 uL of PBS(-) to each well, mix and remove
    for i in range(6):
        p50_single.pick_up_tip()
        p50_single.transfer(300, pbs_tube.wells()[0], well_plate.wells()[i], new_tip='never')
        p50_single.mix(5, 50, well_plate.wells()[i])
        p50_single.blow_out(well_plate.wells()[i].top())
        p50_single.aspirate(300, well_plate.wells()[i])
        p50_single.drop_tip()
    
    # Step 2: Add 300 uL of D-MEM to each well
    for i in range(6):
        p50_single.pick_up_tip()
        p50_single.transfer(300, dmem_tube.wells()[0], well_plate.wells()[i], new_tip='never')
        p50_single.aspirate(300, well_plate.wells()[i])
        p50_single.drop_tip()
    
    # Step 3: End of the protocol
    protocol.comment('Experiment completed')
