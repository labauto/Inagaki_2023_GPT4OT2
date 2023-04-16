from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '2')
    pipette_200ul = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_200ul])

    # Reagents
    lysis_buffer = plate_6_well.wells_by_name()['A1']
    fixative_solution = plate_6_well.wells_by_name()['A2']
    blocking_buffer = plate_6_well.wells_by_name()['A3']

    # Staining wells
    for i in range(1, 4):
        well = plate_6_well.wells_by_name()[f"A{i}"]

        # Add lysis buffer
        pipette_200ul.pick_up_tip()
        pipette_200ul.aspirate(100, lysis_buffer)
        pipette_200ul.dispense(100, well)
        pipette_200ul.drop_tip()

        # Add fixative solution
        pipette_200ul.pick_up_tip()
        pipette_200ul.aspirate(100, fixative_solution)
        pipette_200ul.dispense(100, well)
        pipette_200ul.drop_tip()

        # Add blocking buffer
        pipette_200ul.pick_up_tip()
        pipette_200ul.aspirate(100, blocking_buffer)
        pipette_200ul.dispense(100, well)
        pipette_200ul.drop_tip()
