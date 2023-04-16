# Import necessary Opentrons modules
from opentrons import protocol_api

# Create a protocol object
metadata = {
    'protocolName': 'Immunostained iPS Cell Prep for E-Cadherin Visualization',
    'author': 'Your Name Here',
    'description': 'This protocol prepares immunostained iPS cells to visualize E-Cadherin in a 6-well plate',
    'apiLevel': '2.9'
}

# Metadata
tiprack_type = 'opentrons_96_tiprack_20ul'
plate_type = 'corning_6_wellplate_16.8ml_flat'
antibody_type = 'your_antibody_here'
dye_type = 'your_dye_here'

# Protocol
def run(protocol: protocol_api.ProtocolContext):

    # Set up plate, tipracks, and pipettes
    plate = protocol.load_labware(plate_type, '1')
    tiprack_1 = protocol.load_labware(tiprack_type, '2')
    p20_multi = protocol.load_instrument('p20_multi_gen2', mount='left', tip_racks=[tiprack_1])
    
    # Prepare cells for staining
    for well in plate.wells():
        # Transfer cell suspension from previous well to well in 6-well plate, force to touch well bottom
        p20_multi.transfer(10, well.previous(), well, new_tip='always', touch_tip=True, blow_out=True)
        # Wash cells with 1 mL of PBS, repeat 2 times
        p20_multi.pick_up_tip()
        for _ in range(2):
            p20_multi.transfer(20, well, well.bottom(10), new_tip='never')
            p20_multi.transfer(900, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '3').wells()[0], well.top(), new_tip='never')
        p20_multi.drop_tip()
        # Fix cells with 4% paraformaldehyde
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '4').wells()[0], well, new_tip='never')
        p20_multi.mix(5, 100, well, rate=0.1)
        p20_multi.drop_tip()
        # Permeabilize cells with 0.5% Triton X-100
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '5').wells()[0], well, new_tip='never')
        p20_multi.mix(5, 100, well, rate=0.1)
        p20_multi.drop_tip()
        # Block cells with 5% BSA
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '6').wells()[0], well, new_tip='never')
        p20_multi.mix(5, 100, well, rate=0.1)
        p20_multi.drop_tip()
        
    # Prepare primary antibody solution
    antibody_destination = [plate.wells()[2], plate.wells()[3]]
    p20_multi.pick_up_tip()
    p20_multi.transfer(10, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '7').wells()[0], antibody_destination, new_tip='always', touch_tip=True, blow_out=True)
    p20_multi.mix(5, 10, antibody_destination, rate=0.1)
    p20_multi.drop_tip()
    
    # Incubate primary antibody
    protocol.delay(minutes=20, msg='Incubating primary antibody solution in 6-well plate for 20 minutes.')
    
    # Wash cells with PBS 3 times
    p20_multi.pick_up_tip()
    for well in plate.wells():
        for _ in range(3):
            p20_multi.transfer(20, well, well.bottom(10), new_tip='never')
            p20_multi.transfer(900, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '3').wells()[0], well.top(), new_tip='never')
    p20_multi.drop_tip()
    
    # Prepare secondary antibody solution with dye
    dye_destination = [plate.wells()[4], plate.wells()[5]]
    p20_multi.pick_up_tip()
    p20_multi.transfer(10, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '8').wells()[0], dye_destination, new_tip='always', touch_tip=True, blow_out=True)
    p20_multi.mix(5, 10, dye_destination, rate=0.1)
    p20_multi.drop_tip()
    
    # Incubate secondary antibody and dye
    protocol.delay(minutes=20, msg='Incubating secondary antibody and dye solution in 6-well plate for 20 minutes.')
    
    # Wash cells with PBS 3 times
    p20_multi.pick_up_tip()
    for well in plate.wells():
        for _ in range(3):
            p20_multi.transfer(20, well, well.bottom(10), new_tip='never')
            p20_multi.transfer(900, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '3').wells()[0], well.top(), new_tip='never')
    p20_multi.drop_tip()
