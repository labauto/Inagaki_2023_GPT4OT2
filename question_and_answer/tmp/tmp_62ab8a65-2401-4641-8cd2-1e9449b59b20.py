import opentrons.execute
from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate.'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware Configuration
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    6_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    medium_tube = protocol.load_labware('eppendorf_5ml', '3')
    
    # Pipette Configuration
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    # Reagent Locations
    pbs_minus = medium_tube.wells_by_name()['A1']
    d_meme = medium_tube.wells_by_name()['A2']
    
    # Aspirate and Dispense Volumes
    pbs_aspirate_volume = 1000  # You can adjust this value based on your requirements
    d_meme_dispense_volume = 1000 # You can adjust this value based on your requirements
    
    # Remove Old Media and Add PBS(-)
    for well in 6_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(pbs_aspirate_volume, pbs_minus)
        p300.dispense(pbs_aspirate_volume, well)
        p300.mix(3, pbs_aspirate_volume//2, well)  # Mix number of times, volume to mix
        p300.blow_out(well.top())  # Blow air in to push the liquid out
        p300.aspirate(pbs_aspirate_volume, well)  # Aspirate the mixed liquid
        p300.dispense(pbs_aspirate_volume, pbs_minus)  # Discard liquid into waste container
        p300.drop_tip()
    
    # Add D-MEM
    for well in 6_well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(d_meme_dispense_volume, d_meme)
        p300.dispense(d_meme_dispense_volume, well)
        p300.drop_tip()
