from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0',
    'protocolName': 'MSC spheroids',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Culture hMSC spheroids with and without osteoinduction supplements.'
}

def run(protocol: protocol_api.ProtocolContext):
    # load the plate
    os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

    # load the tube rack
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_snapcap', '5')
    supplements = tube_rack['A4']

    # load the pipettes
    pipette = protocol.load_instrument('p50_multi', 'left', tip_racks=[
        protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    ])

    # helper function for transferring media
    def transfer_to_plate(volume, source, dest_plate):
        for dest in dest_plate:
            pipette.transfer(volume, source, dest.top(), new_tip='always')

    # step 1: transfer DMEM to os_minus plate
    transfer_to_plate(100, protocol.load_labware('corning_96_wellplate_360ul_flat', '4').rows()[0], os_minus.wells())

    # step 2: transfer DMEM, Dex, AA, BGP to os_plus plate
    transfer_to_plate(100, protocol.load_labware('corning_96_wellplate_360ul_flat', '4').rows()[0], os_plus.wells())
    pipette.transfer(0.1, supplements[0], os_plus.wells(), new_tip='once')
    pipette.transfer(1, supplements[1], os_plus.wells(), new_tip='once')
    pipette.transfer(1, supplements[2], os_plus.wells(), new_tip='once')

    # step 3: transfer cells to both plates
    cell_source = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    transfer_to_plate(100, cell_source.rows()[0], os_minus.wells())
    transfer_to_plate(100, cell_source.rows()[0], os_plus.wells())

