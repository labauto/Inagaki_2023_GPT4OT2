from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Thapsigargin Experiment',
    'author': 'Opentrons',
    'description': 'Automated A549 cell treatment protocol using Opentrons',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tips_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1_5 = protocol.load_labware('opentrons_15_tuberack_generic_15ml_13x100', 6)
    tube_rack_2 = protocol.load_labware('opentrons_96_tuberack_generic_235x138x48', 7)

    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)
    heater_shaker = protocol.load_module('heatershaker', 3)
    opentrons_10_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 8)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tips_20)
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tips_200)

    # Reagents
    cell_suspension = tube_rack_1_5.wells()
    thapsigargin_stocks = tube_rack_2.wells()
    cell_tox_green = opentrons_10_tube_rack.wells_by_name()['B2']
    cell_titer_glo = opentrons_10_tube_rack.wells_by_name()['B1']

    # Seeding cells
    for i, well in enumerate(plate_96_well.wells()):
        p300.pick_up_tip()
        p300.aspirate(60, cell_suspension[i % 10])
        p300.dispense(60, well)
        p300.drop_tip()

    # Thapsigargin addition
    for stock, dest_wells in zip(thapsigargin_stocks, plate_96_well.columns()):
        for well in dest_wells:
            p300.pick_up_tip()
            p300.aspirate(60, stock)
            p300.dispense(60, well)
            p300.mix(5, 40, well)
            p300.drop_tip()

    # Experiments

    # CellTox Green assay
    for well in plate_96_well.wells():
        p20.pick_up_tip()
        p20.aspirate(15, cell_tox_green)
        p20.dispense(15, well)
        p20.drop_tip()

    heater_shaker.shake(duration_sec=2 * 60, speed_rpm=500)
    protocol.delay(minutes=15)

    # Fluorescence reading at 485nm excitation, 520nm emission

    # Cell viability assay - CellTiter-Glo
    for well in plate_96_well.wells():
        p300.pick_up_tip()
        p300.aspirate(80, cell_titer_glo)
        p300.dispense(80, well)
        p300.drop_tip()

    heater_shaker.shake(duration_sec=2 * 60, speed_rpm=500)
    protocol.delay(minutes=10)

    # Luminescence reading
plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)
