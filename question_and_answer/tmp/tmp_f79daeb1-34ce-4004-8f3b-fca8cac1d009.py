from opentrons import protocol_api

metadata = {
    'author': 'Your Name',
    'description': 'Automation of immunostained hMSC cells to visualize lysosomes.',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define the labware (customize this part based on your experiment setup and labware specifications)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')  # Replace with the tiprack you're using
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Define the pipettes
    p300_single = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    # Define the wells
    source_wells = well_plate.wells_by_name()['A1'], well_plate.wells_by_name()['A2'], well_plate.wells_by_name()['A3']
    
    # Write the experimental protocol
    # This can be modified based on reagents, specific pipetting steps, incubation times, etc. 
    # Here is an example of transferring 100 uL from a source well to a destination well in each well of the plate
    volume_to_transfer = 100

    for well_idx, source_well in enumerate(source_wells, start=1):
        destination_well = well_plate['A'+str(well_idx + 3)]

        # Pipetting steps
        p300_single.pick_up_tip()
        p300_single.aspirate(volume_to_transfer, source_well.bottom(1.5))
        p300_single.dispense(volume_to_transfer, destination_well.bottom(1.5))
        p300_single.blow_out(destination_well)
        p300_single.drop_tip()
