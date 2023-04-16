from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'A549 Thapsigargin Experiment',
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')
    tips_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')
    tube_rack_15 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '6')
    tube_rack_1_5 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '7')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    heater_shaker = protocol.load_module('heater_shaker', '9')
    hs_plate = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    p200 = protocol.load_instrument('p200_single_gen2', 'left', tip_racks=[tips_200])

    # Initial stocks:
    stocks = {
        'A1': 1e-3,
        'A2': 100e-6,
        'A3': 10e-6,
        'A4': 1e-6,
        'A5': 100e-9,
        'A6': 50e-9,
        'B1': 10e-9,
    }

    # Create 4X working concentrations
    working_4x = {
        'C1': 1.56 * 4e-9,
        'C2': 3.12 * 4e-9,
        'C3': 6.24 * 4e-9,
        'C4': 12.52 * 4e-9,
        'C5': 25 * 4e-9,
        'C6': 50 * 4e-9,
        'D1': 100 * 4e-9,
        'D2': 200 * 4e-9,
        'D3': 400 * 4e-9,
        'D4': 800 * 4e-9,
        'D5': 1600 * 4e-9,
        'D6': 2000 * 4e-9,
    }

    # Prepare 2X working concentrations:
    for src_well, dest_well in zip(working_4x.keys(), tube_rack_15.wells()):
        p200.transfer(100, tube_rack_1_5[src_well], dest_well, mix_after=(3, 100))

    # Distribute cells to the 96 well plate
    for well in plate_96.columns()[0]:
        p20.transfer(60, tube_rack_15['A6'], well, mix_after=(3, 60))

    # 2. Add medium to wells A5 to C5
    for well in plate_96.rows()[0][4:7]:
        p200.transfer(100, tube_rack_15['A6'], well)

    # 9. Add thapsigargin to the 96 well plate
    for index, (src_well, concentration) in enumerate(zip(tube_rack_15.wells(), list(working_4x.values())[1:])):
        dest_wells = plate_96.columns()[index + 1]
        if index + 1 == 4:
            dest_wells = dest_wells[:-3]
        p200.pick_up_tip()
        for dest_well in dest_wells:
            p200.transfer(50, src_well, dest_well, mix_after=(3, 50), new_tip='never')
        p200.drop_tip()

    # 11. Addition of the CellTox Green reagent
    for well in hs_plate.wells():
        p20.transfer(15, tube_rack_15['B2'], well, mix_after=(3, 15))

    # 13. Orbital shaking and incubation
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.stop()

    # Perform fluorescence reading (Task will be performed outside the script)

    # 15. Add CellTiter-Glo 2.0 reagent
    for well in hs_plate.wells():
        p200.transfer(80, tube_rack_15['B1'], well, mix_after=(3, 80))

    # 17. Orbital shaking and incubation
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.stop()

    # Perform luminescence reading (Task will be performed outside the script)
