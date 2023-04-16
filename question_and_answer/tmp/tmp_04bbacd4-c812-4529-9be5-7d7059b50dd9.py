from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips_10 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    tips_200 = protocol.load_labware('opentrons_96_tiprack_200ul', 2)
    well_plate_96 = protocol.load_labware('nest_96_wellplate_200ul_flat', 3)
    reagent_tubes = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5mL_single', 4)

    # Pipettes
    p10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tips_10])
    p200 = protocol.load_instrument('p200_single', 'left', tip_racks=[tips_200])

    # Reagents
    high_glucose_dmem = reagent_tubes.wells_by_name()['A1']
    dmem = reagent_tubes.wells_by_name()['A2']
    dexamethasone = reagent_tubes.wells_by_name()['A3']
    ascorbic_acid = reagent_tubes.wells_by_name()['A4']
    beta_glycerophosphate = reagent_tubes.wells_by_name()['A5']
    hmsc_cells = reagent_tubes.wells_by_name()['A6']

    # Destinations
    os_plus_wells = well_plate_96.columns_by_name()["1"]
    os_minus_wells = well_plate_96.columns_by_name()["2"]

    # Helper functions
    def transfer_medium(pipette, source, dest_wells):
        for well in dest_wells:
            pipette.transfer(100, source, well, new_tip='always')

    def add_os_plus_supplements(dest_wells):
        for well in dest_wells:
            p10.transfer(0.1, dexamethasone, well, mix_after=(3, 3), new_tip='always')
            p10.transfer(1, ascorbic_acid, well, mix_after=(3, 3), new_tip='always')
            p10.transfer(1, beta_glycerophosphate, well, mix_after=(3, 3), new_tip='always')

    def transfer_hmsc_cells(pipette, source, dest_wells):
        for well in dest_wells:
            pipette.transfer(100, source, well, new_tip='always')

    # Main function
    def main():
        # Transfer medium
        transfer_medium(p200, dmem, os_minus_wells)
        transfer_medium(p200, high_glucose_dmem, os_plus_wells)

        # Add supplements
        add_os_plus_supplements(os_plus_wells)

        # Transfer cells
        transfer_hmsc_cells(p200, hmsc_cells, os_minus_wells)
        transfer_hmsc_cells(p200, hmsc_cells, os_plus_wells)

    main()
