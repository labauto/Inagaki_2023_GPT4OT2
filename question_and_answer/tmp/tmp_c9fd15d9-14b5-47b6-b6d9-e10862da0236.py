from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'A549_Cytotoxicity_Assay',
    'author': 'Assistant',
    'description': 'Measurement of viability and cytotoxicity of A549 cells treated with thapsigargin',
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tips_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tips_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    slot_6_tubes = protocol.load_labware('opentrons_15_tuberack_falcon_15ml', 6)

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips_200])

    # Reagent locations
    celltox_green = tube_rack_10.wells_by_name()["B2"]
    cell_titer_glo = tube_rack_10.wells_by_name()["B1"]

    # Steps 1 and 2 are manual operations. Assume cell suspension is prepared.

    # Step 3
    cell_suspension = slot_6_tubes.wells()[:10]

    # Load 8,000 cells to each well
    for well in plate_96.wells():
        p20.transfer(60, cell_suspension.pop(0), well)

    # ... (step 4 - step 8)

    # Step 9

    # Dilution series preparation using p20
    dilution_series = [tube_rack_10.wells_by_name()[well] for well in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']]
    for idx, well in enumerate(dilution_series[:-1]):
        p20.transfer(50, well, dilution_series[idx + 1], mix_before=(3, 50), mix_after=(3, 50))

    # ... (step 10 - step 12)

    # Step 13 - Measure fluorescence
    # This step requires measuring fluorescence with a microplate reader, which is not part of the Opentrons protocol. Perform this step manually or with the appropriate integrated device.

    # Step 14 - Cell viability assay reagent addition
    for well in plate_96.wells():
        p200.pick_up_tip()
        p200.aspirate(80, cell_titer_glo)
        p200.dispense(80, well)
        p200.mix(3, 80)
        p200.blow_out(well.top())
        p200.drop_tip()

    # Step 15 - Incubate and shake plate
    protocol.pause("Incubate the plate at room temperature for 10 minutes before proceeding.")

    # Step 16 - Measure luminescence
    # This step requires measuring luminescence with a microplate reader, which is not part of the Opentrons protocol. Perform this step manually or with the appropriate integrated device.

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.10')
    run(protocol)
