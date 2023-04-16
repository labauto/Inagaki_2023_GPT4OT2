# Import necessary modules
from opentrons import protocol_api

# Initialize the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    medium = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')
    
    # Load the pipette
    pipette = protocol.load_instrument('p1000_single_gen2', tip_racks=[tiprack])
    
    # Wash the 6 well plate with PBS(-)
    pipette.pick_up_tip()
    for well in plate.wells():
        pipette.aspirate(1000, medium['A1'])
        pipette.dispense(1000, well)
        pipette.aspirate(1000, well)
        pipette.dispense(1000, medium['A1'])
    pipette.drop_tip()
    
    # Add trypsin solution
    pipette.pick_up_tip()
    for well in plate.wells():
        pipette.aspirate(1000, medium['A2'])
        pipette.dispense(1000, well)
    pipette.drop_tip()
    protocol.delay(minutes=5)
    
    # Add cell culture medium
    pipette.pick_up_tip()
    pipette.transfer(1000, medium['A3'], plate.wells(), blow_out=True, new_tip='always')
    pipette.drop_tip()
