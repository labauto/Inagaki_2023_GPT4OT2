from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    cell_suspension_reservoir = protocol.load_labware('nest_1_reservoir_195ml', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Pipette
    pipette = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Reagents
    cell_suspension = cell_suspension_reservoir['A1']

    # Protocol
    for well_idx in range(6):
        if well_idx < 3: # 0, 1, 2
            well_key = 'A' + str(well_idx + 1)
        else: # 3, 4, 5
            well_key = 'B' + str(well_idx - 2)

        destination_well = well_plate[well_key]

        pipette.pick_up_tip()
        pipette.aspirate(1000, cell_suspension)
        pipette.dispense(1000, destination_well)
        pipette.drop_tip()
