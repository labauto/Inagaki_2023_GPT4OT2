# Import the Opentrons API
from opentrons import protocol_api

# Metadata
metadata = {
    'apiLevel': '2.11'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load the 6-well plate and tip rack
    plate = protocol.load_labware('corning_6_wellplate_16.76ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # Load the pipette
    pipette = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack])

    # Define the wells to be used
    wells = [plate['A1'], plate['A2'], plate['A3'], plate['A4'], plate['A5'], plate['A6']]

    # Add 500ul of PBS to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Add 500ul of 4% PFA in PBS to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.mix(5, 300)
        pipette.blow_out()
        pipette.drop_tip()

    # Add 500ul of blocking solution (10% normal goat serum, 0.1% Triton X-100 in PBS) to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.mix(5, 300)
        pipette.blow_out()
        pipette.drop_tip()

    # Add 500ul of primary antibody solution to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.mix(5, 300)
        pipette.blow_out()
        pipette.drop_tip()

    # Add 500ul of secondary antibody solution to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.mix(5, 300)
        pipette.blow_out()
        pipette.drop_tip()

    # Add 500ul of DAPI (4',6-diamidino-2-phenylindole) counterstain solution to each well in the plate
    for well in wells:
        pipette.pick_up_tip()
        pipette.aspirate(500, well)
        pipette.dispense(500, well)
        pipette.mix(5, 300)
        pipette.blow_out()
        pipette.drop_tip()
