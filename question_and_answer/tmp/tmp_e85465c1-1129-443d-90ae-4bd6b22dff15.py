from opentrons import simulate

metadata = {'apiLevel': '2.11'}

def run(protocol):
    # Labware
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', location='1')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', location='2')
    dmem_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_15ml', location='4')
    supplements_tube_rack = protocol.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', location='5')
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', location='11')

    # Pipettes
    p200 = protocol.load_instrument('p300_single_gen2', mount='right', tip_racks=[tiprack_200])

    # Solutions
    dmem = dmem_tube_rack.wells_by_name()['A1']
    dmem_high_glucose = dmem_tube_rack.wells_by_name()['A2']
    hmsc_cells = dmem_tube_rack.wells_by_name()['B1']
    dex = supplements_tube_rack.wells_by_name()['A1']
    aa = supplements_tube_rack.wells_by_name()['A2']
    bgp = supplements_tube_rack.wells_by_name()['A3']

    def transfer_medium_os_minus():
        for well in plate_os_minus.wells():
            p200.transfer(100, dmem, well, mix_after=(3, 100))

    def transfer_medium_os_plus():
        for well in plate_os_plus.wells():
            p200.transfer(100, dmem_high_glucose, well, mix_after=(3, 100))

    def add_supplements_os_plus():
        for well in plate_os_plus.wells():
            p200.transfer(0.1, dex, well, mix_after=(3, 25))
            p200.transfer(1, aa, well, mix_after=(3, 25))
            p200.transfer(1, bgp, well, mix_after=(3, 25))

    def transfer_cells():
        for well in plate_os_minus.wells():
            p200.transfer(100, hmsc_cells, well, mix_after=(3, 100))
        for well in plate_os_plus.wells():
            p200.transfer(100, hmsc_cells, well, mix_after=(3, 100))

    # Steps
    transfer_medium_os_minus()
    transfer_medium_os_plus()
    add_supplements_os_plus()
    transfer_cells()

protocol = simulate.get_protocol_api('2.11')
run(protocol)
