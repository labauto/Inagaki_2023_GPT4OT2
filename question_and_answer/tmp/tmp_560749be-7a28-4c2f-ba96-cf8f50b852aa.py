
from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware and pipette
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_1])

    # Cell preparation
    cell_suspension = protocol.load_labware('nest_1_reservoir_195ml', '3')['A1']

    # Immunostaining reagent preparation
    reagents = protocol.load_labware('nest_12_reservoir_15ml', '4')['A1']

    # Perform cell transfer and incubation
    for well_idx, well_key in enumerate(well_plate.wells_by_name()):
        if well_idx > 0 and well_idx < 4:
            pipette.pick_up_tip()
            pipette.aspirate(1000, cell_suspension)
            pipette.dispense(1000, well_plate[well_key])
            pipette.drop_tip()

    # Perform antibody staining
    for well_key in well_plate.wells_by_name():
        pipette.pick_up_tip()
        pipette.aspirate(1000, reagents)
        pipette.dispense(1000, well_plate[well_key])
        pipette.drop_tip()
