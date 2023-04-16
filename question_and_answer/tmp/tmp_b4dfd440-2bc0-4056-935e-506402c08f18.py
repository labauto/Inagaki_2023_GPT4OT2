from opentrons import protocol_api

metadata = {
    'protocolName': 'A549_cells_thapsigargin_experiment',
    'author': 'Opentrons Assistant',
    'description': 'Measurement of viability and cytotoxicity of A549 cells treated with Thapsigargin',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', 4)
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)
    tube_rack_6 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 6)
    tube_rack_7 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
    falcon_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 8)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p200_single_gen2', 'left', tip_racks=[tiprack_200ul])

    # Heater Shaker
    heater_shaker = protocol.load_module('temperature module', 1)
    heater_shaker.load_labware('corning_96_wellplate_360ul_flat')

    # Thapsigargin dilution and transfer function
    def thapsigargin_dilution_transfer(wells, source, volumes):
        for well, volume in zip(wells, volumes):
            p20.pick_up_tip()
            p20.aspirate(200 - volume, source)
            p20.dispense(200, well)
            p20.mix(3, 20, well)
            p20.aspirate(volume, source)
            p20.dispense(volume, well)
            p20.mix(3, 20, well)
            p20.blow_out(well.top().move(Point(z=-6)))
            p20.drop_tip()

    # Steps 6-8: Thapsigargin dilutions
    thapsigargin_dilution_transfer(tube_rack_7.wells('C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'), tube_rack_7["A1"], [1.56, 3.12, 6.24, 12.52, 25, 50, 100, 200, 400, 800, 1600, 2000])

    # Steps 9: Prepare 2X concentrations
    thapsigargin_dilution_transfer(tube_rack_6.wells('C1', 'C3', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'), tube_rack_7.wells('C1', 'C3', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'), [100, 100, 100, 100, 100, 100, 100, 100, 100])

    # Steps 10: Add CellTox Green reagent
    for well in plate_96_well.wells():
        p20.pick_up_tip()
        p20.aspirate(100, falcon_rack['B2'])
        p20.dispense(100, well)
        p20.blow_out(well.top().move(Point(z=-6)))
        p20.drop_tip()

    # Steps 11: Orbital shaking and incubate
    heater_shaker.set_temperature(23)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)
    protocol.delay(minutes=15)

    # Steps 12: Read the fluorescence
    # Fluorescence reading is performed on Biotek microplate reader at 485 nm excitation and 520 nm emission (not supported by Opentrons API)

    # Steps 15: Add Cell Titer Glo Reagent
    for well in plate_96_well.wells():
        p200.pick_up_tip()
        p200.aspirate(100, falcon_rack['B1'])
        p200.dispense(100, well)
        p200.blow_out(well.top().move(Point(z=-6)))
        p200.drop_tip()

    # Steps 16: Orbital shaking and incubate
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)
    protocol.delay(minutes=10)

    # Steps 17: Read the luminescence
    # Luminescence reading is performed on Biotek microplate reader (not supported by Opentrons API)
