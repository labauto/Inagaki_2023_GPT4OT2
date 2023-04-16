from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of A549 cells treated with Thapsigargin using Opentrons robot',
    'apiLevel': '2.11'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    tube_rack_1 = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '6')
    tube_rack_2 = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '7')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '9')
    plate_TC_white = protocol.load_labware('corning_96_wellplate_360ul_flat', '8')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '4')

    # pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p200_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # step 1: count cells
    p20.pick_up_tip()
    p20.transfer(10, tube_rack_1['A1'], plate_96_well['A1'], mix_after=(3, 5))
    p20.drop_tip()

    # step 2: seed cells
    p200.pick_up_tip()
    for well in plate_96_well.columns_by_name()['1']:
        p200.transfer(48, tube_rack_1['A1'], well, mix_after=(3, 50))
    p200.drop_tip()

    # step 3: dispense cell suspension to tubes
    for tube in tube_rack_2.columns()[0]:
        p200.transfer(225, plate_96_well['A1'], tube)

    # step 4: add medium to controls
    for well in plate_96_well.columns_by_name()['2']:
        p200.transfer(60, tube_rack_1['A1'], well)

    # step 5: wait 12-16 hours

    # step 6: add Thapsigargin to tube A1
    p20.pick_up_tip()
    p20.transfer(35, tube_rack_2['A1'], tube_rack_2['A2'], mix_after=(3, 10))
    p20.drop_tip()

    # step 7: prepare Thapsigargin dilutions
    dilutions_1xmM = tube_rack_2.columns()[0][1:]
    dilutions_4x = tube_rack_2.columns()[1:]
    working_concs = plate_96_well.columns_by_name()['3':'9']
    conc_4x = [100, 10, 1, 0.1, 0.01, 0.005]
    diluent_vol = 45
    
    for i in range(len(dilutions_1xmM)):
        p200.pick_up_tip()
        p200.transfer(diluent_vol, tube_rack_1['A1'], dilutions_1xmM[i])
        p200.drop_tip()

        for j in range(len(dilutions_4x)):
            p200.pick_up_tip()
            p200.mix(3, 50, dilutions_4x[j])
            p200.aspirate(45, dilutions_4x[j])
            p200.dispense(45, dilutions_4x[j+1])
            p200.blow_out()
            p200.drop_tip()

    # step 8: prepare 2x working concentrations
    tube_C1 = dilutions_4x[0]
    tube_D1_to_D6 = dilutions_4x[1:]
    working_conc_2x = []

    for tube in tube_C1, *tube_D1_to_D6:
        p200.pick_up_tip()
        p200.transfer(diluent_vol, tube_rack_1['A1'], tube)

        for i in range(len(conc_4x)):
            p200.aspirate(100, tube)
            p200.dispense(100, working_concs[i][0])
            p200.mix(3, 50, tube)
            p200.mix(3, 50, working_concs[i][0])
            p200.aspirate(100, working_concs[i][0])
            p200.dispense(100, working_conc_2x[i])
            p200.mix(3, 50, working_conc_2x[i])

        p200.drop_tip()

    # step 9: add drug to cells
    p200.pick_up_tip()
    for col in plate_96_well.columns():
        if col[0].get_name()[0] == 'A':
            p200.transfer(60, tube_rack_1['A1'], col)

    for i, conc in enumerate(working_conc_2x):
        for row in plate_96_well.rows():
            if row[0].get_name()[1] == str(i+1):
                p200.transfer(60, conc, row, mix_after=(3, 50))
    p200.drop_tip()

    # step 10: add CellTox Green reagent
    for well in plate_TC_white.columns()[1:]:
        p20.pick_up_tip()
        p20.transfer(15, tube_rack_1['B2'], well, mix_after=(3, 10))
        p20.drop_tip()

    # step 11: start shaking
    protocol.set_temperature(25)
    protocol.set_plate_temperature(25)
    protocol.comment('Start shaking for 2 minutes @ 500 rpm')
    protocol.shake_plate(plate_TC_white)

    # step 12: incubate
    protocol.delay(minutes=15)

    # step 13: measure fluorescence
    protocol.set_temperature(25)
    protocol.set_plate_temperature(25)
    protocol.comment('Read fluorescence at 485 nm excitation and 520 nm emission')
    protocol.measure_fluorescence(
        plate_TC_white.columns()[1:],
        '485:20',
        '520:20'
    )

    # step 14: start adding CellTiter-Glo 2.0 reagent
    for well in plate_TC_white.columns()[1:]:
        p200.pick_up_tip()
        p200.transfer(80, tube_rack_1['B1'], well, mix_after=(3, 10))
        p200.drop_tip()

    # step 15: start shaking
    protocol.set_temperature(25)
    protocol.set_plate_temperature(25)
    protocol.comment('Start shaking for 2 minutes @ 500 rpm')
    protocol.shake_plate(plate_TC_white)

    # step 16: incubate
    protocol.delay(minutes=10)

    # step 17: measure luminescence
    protocol.set_temperature(25)
    protocol.set_plate_temperature(25)
    protocol.comment('Read luminescence')
    protocol.measure_luminescence(
        plate_TC_white.columns()[1:],
        integration_time_s=1
    )
