from opentrons import protocol_api

def run(protocol: protocol_api.ProtocolContext):
    # Set up the pipettes
    left_pipette = protocol.load_instrument('p300_single_gen2', 'left')
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right')

    # Set up the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')

    # Define the reagents
    pbs_neg = reservoir['A1']
    dmem = reservoir['A2']

    # Define the locations of the wells for the plate
    wells = [well for row in plate.rows() for well in row]

    # Distribute PBS(-) to wells
    left_pipette.pick_up_tip()
    for well in wells:
        left_pipette.aspirate(200, pbs_neg)
        left_pipette.dispense(200, well)
    left_pipette.drop_tip()

    # Exchange PBS(-) with D-MEM
    right_pipette.pick_up_tip()
    for well in wells:
        right_pipette.aspirate(200, well)
        right_pipette.dispense(200, reservoir['A3'])
    right_pipette.drop_tip()

    # Add D-MEM to wells
    left_pipette.pick_up_tip()
    for well in wells:
        left_pipette.aspirate(200, dmem)
        left_pipette.dispense(200, well)
    left_pipette.drop_tip()
