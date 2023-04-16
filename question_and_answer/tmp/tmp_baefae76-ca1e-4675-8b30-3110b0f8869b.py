from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Immunostained hMSC Cells Visualization for Lysosomes',
    'description': 'Preparing immunostained hMSC cells in a 6-well plate to visualize lysosomes',
    'author': 'Opentrons'}
    
def run(protocol: protocol_api.ProtocolContext):

    # Labware
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])
    
    # Wells with samples
    wells = well_plate.wells()

    # Protocol steps
    for well in wells:
        p300.pick_up_tip()
        # Replace below with actual reagents, incubation, and washing steps for immunostaining hMSC cells
        p300.aspirate(50, well)
        p300.dispense(50, well)
        p300.mix(4, 50, well)
        p300.drop_tip()

# Save the script as a .py file and you can run it with your Opentrons machine. Make sure to adjust the protocol steps as necessary to match the specific reagents, incubation times, and washing steps required for your protocol.
