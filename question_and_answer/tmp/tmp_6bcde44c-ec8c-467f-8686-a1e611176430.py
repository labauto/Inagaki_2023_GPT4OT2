from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'hMSC spheroids culture',
    'author': 'Opentrons <protocols@opentrons.com>',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_os_minus = protocol.load_labware('nest_96_wellplate_2000ul', '1')
    plate_os_plus = protocol.load_labware('nest_96_wellplate_2000ul', '2')
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '3')

    # Reagents
    medium_dmem = tuberack.wells_by_name()['A1']
    medium_dmem_high_glucose = tuberack.wells_by_name()['A2']
    dex = tuberack.wells_by_name()['A3']
    aa = tuberack.wells_by_name()['A4']
    bgp = tuberack.wells_by_name()['A5']
    hmsc_cells = tuberack.wells_by_name()['A6']

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left')
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right')

    # Functions
    def transfer_medium(src, dest_plate):
        for well in dest_plate.wells():
            p1000.transfer(100, src, well, new_tip='always')

    def add_supplements():
        for well in plate_os_plus.wells():
            p20.transfer(0.1, dex, well, mix_after=(3, 10), new_tip='always')
            p20.transfer(1, aa, well, mix_after=(3, 10), new_tip='always')
            p20.transfer(1, bgp, well, mix_after=(3, 10), new_tip='always')

    def transfer_cells(src, dest_plate):
        for well in dest_plate.wells():
            p1000.transfer(100, src, well, new_tip='always')

    # Steps
    transfer_medium(medium_dmem, plate_os_minus)
    transfer_medium(medium_dmem_high_glucose, plate_os_plus)
    add_supplements()
    transfer_cells(hmsc_cells, plate_os_minus)
    transfer_cells(hmsc_cells, plate_os_plus)

