from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'hMSC Cell Culture'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tuberack_15ml = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', mount='right', tip_racks=[tiprack_300])

    # Reagents
    dmem = tuberack_15ml.wells_by_name()['A1']
    dmem_high_glucose = tuberack_15ml.wells_by_name()['A2']
    dex = tuberack_15ml.wells_by_name()['A3']
    aa = tuberack_15ml.wells_by_name()['A4']
    bgp = tuberack_15ml.wells_by_name()['A5']
    hmsc = tuberack_15ml.wells_by_name()['A6']

    def transfer_medium_to_os_minus():
        for well in plate_96.wells():
            p300.pick_up_tip()
            p300.transfer(100, dmem, well, new_tip='never')
            p300.drop_tip()

    def transfer_medium_to_os_plus():
        for well in plate_96.wells():
            p300.pick_up_tip()
            p300.transfer(100, dmem_high_glucose, well, new_tip='never')
            p300.drop_tip()

    def transfer_supplements(target_well):
        p300.pick_up_tip()
        p300.transfer(0.1, dex, target_well, mix_after=(3, 10), new_tip='never')
        p300.transfer(1, aa, target_well, mix_after=(3, 10), new_tip='never')
        p300.transfer(1, bgp, target_well, mix_after=(3, 10), new_tip='never')
        p300.drop_tip()

    def transfer_hmsc_to_plate(target_well):
        p300.pick_up_tip()
        p300.transfer(100, hmsc, target_well, mix_after=(3, 10), new_tip='never')
        p300.drop_tip()

    transfer_medium_to_os_minus()

    transfer_medium_to_os_plus()

    for well_os_plus in plate_96.wells():
        transfer_supplements(well_os_plus)

    for well in plate_96.wells():
        transfer_hmsc_to_plate(well)
