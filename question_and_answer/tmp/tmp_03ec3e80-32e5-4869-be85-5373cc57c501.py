from opentrons import protocol_api

metadata = {'apiLevel': '2.9'}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tubes_slot6 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 6)
    tubes_slot7 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)
    tips_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    tips_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips_20])
    p200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips_200])

    # Load Heater-Shaker module
    heater_shaker = protocol.load_module('heaterShakerModuleV1', 5)
    plate_on_heater_shaker = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')

    # Perform your protocol steps as described.
    # For example:
    
    # Step 1: Seeding cells
    # ...

    # Step 5: Second day drug dilutions and additions
    # ...

    # Steps 10-11: Adding CellTox Green reagent
    for row in plate_96.rows():
        source = tubes_slot6['B2']
        dest_wells = row[0:4] + row[5:9]
        p20.transfer(15, source, dest_wells, mix_after=(3, 15))

    # Step 11: Shaking the plate and waiting
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)

    # ...

    # Steps 15-16: Adding Cell Titer Glo 2.0 reagent
    for row in plate_on_heater_shaker.rows():
        source = tubes_slot6['B1']
        dest_wells = row[0:4] + row[5:9]
        p200.transfer(80, source, dest_wells, mix_after=(3, 80))

    # Step 16: Shaking the plate and waiting
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)

    # ...
