from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '1')
    tips20 = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tips200 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '6')
    drug_rack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '7')
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '8')
    heater_shaker = protocol.load_module('heaterShakerModuleV1', '9')

    # pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips20])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips200])

    # Steps 10-17 
    heater_shaker_plate = heater_shaker.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', label='heater shaker plate')

    # Step 10
    for well in range(0, 18):
        p20.pick_up_tip()
        p20.aspirate(15, reagent_rack['B2'])
        p20.dispense(15, heater_shaker_plate.rows()[0][well].center(15))
        p20.drop_tip()

    # steps 11-12
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2 + 15)

    # Read fluorescence at 485 nm excitation and 520 nm emission (Step 13)
    # This step cannot be executed in the script and needs to be done manually
    # using a Biotek microplate reader.

    # Step 14-16
    for well in range(0, 18):
        p300.pick_up_tip()
        p300.aspirate(80, reagent_rack['B1'])
        p300.dispense(80, heater_shaker_plate.rows()[0][well])
        p300.drop_tip()

    # steps 15-17
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2 + 10)

    # Read luminescence (Step 17)
    # This step cannot be executed in the script and needs to be done manually
    # using a Biotek microplate reader.

