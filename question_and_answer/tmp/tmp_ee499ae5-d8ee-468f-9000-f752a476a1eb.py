from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    dye_container = protocol.load_labware('nest_12_reservoir_15ml', 2)

    # Pipettes
    pipette_300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 3)])

    # Reagents
    cell_stain_solution = dye_container.wells_by_name()['A1']
    hMSC_cells = [well for well in plate_6well.wells()]

    # Protocol
    for well in hMSC_cells:
        pipette_300.pick_up_tip()
        pipette_300.aspirate(200, cell_stain_solution)
        pipette_300.dispense(200, well)
        pipette_300.mix(5, 200, well)
        pipette_300.drop_tip()
