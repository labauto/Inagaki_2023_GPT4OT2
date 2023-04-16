from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    reagent_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')

    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Reagents
    cell_suspension = reagent_tube['A1']

    # Procedure
    for well_idx in range(6):
        well_key = 'A' + str(well_idx + 1)
        destination_well = well_plate[well_key]

        # Aspirate cell suspension
        pipette.pick_up_tip()
        pipette.aspirate(200, cell_suspension)

        # Dispense cell suspension
        pipette.dispense(200, destination_well)
        pipette.blow_out(destination_well.top())
        pipette.drop_tip()
