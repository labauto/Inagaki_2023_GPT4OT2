from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '2')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '3')
    supplements = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '4')
    plate_os_minus = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')
    plate_os_plus = protocol.load_labware('nest_96_wellplate_200ul_flat', '6')
    hmsc_cells = protocol.load_labware('nest_1_reservoir_195ml', '7')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Reagents
    dmem = medium_dmem.wells_by_name()['A1']
    dmem_high_glucose = medium_dmem_high_glucose.wells_by_name()['A1']
    dex = supplements.wells_by_name()['A1']
    aa = supplements.wells_by_name()['A2']
    bgp = supplements.wells_by_name()['A3']
    cells = hmsc_cells.wells_by_name()['A1']

    def transfer_medium_to_os_minus():
        for well in plate_os_minus.wells():
            p300.pick_up_tip()
            p300.transfer(100, dmem, well, new_tip='never')
            p300.drop_tip()

    def transfer_medium_to_os_plus():
        for well in plate_os_plus.wells():
            p300.pick_up_tip()
            p300.transfer(100, dmem_high_glucose, well, new_tip='never')
            p300.drop_tip()

    def transfer_supplements(well_os_plus):
        for target_well in well_os_plus:
            p300.pick_up_tip()
            p300.transfer(0.1, dex, target_well, mix_after=(3, 10), new_tip='never')
            p300.transfer(1, aa, target_well, mix_after=(3, 10), new_tip='never')
            p300.transfer(1, bgp, target_well, mix_after=(3, 10), new_tip='never')
            p300.drop_tip()

    def transfer_cells(well_os_minus, well_os_plus):
        for target_well in well_os_minus:
            p300.pick_up_tip()
            p300.transfer(100, cells, target_well, mix_after=(3, 10), new_tip='never')
            p300.drop_tip()

        for target_well in well_os_plus:
            p300.pick_up_tip()
            p300.transfer(100, cells, target_well, mix_after=(3, 10), new_tip='never')
            p300.drop_tip()

    transfer_medium_to_os_minus()
    transfer_medium_to_os_plus()
    transfer_supplements(plate_os_plus.wells())
    transfer_cells(plate_os_minus.wells(), plate_os_plus.wells())
