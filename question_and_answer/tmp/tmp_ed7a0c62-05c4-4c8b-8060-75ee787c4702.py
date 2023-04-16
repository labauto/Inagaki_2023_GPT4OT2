from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid experiment',
    'author': 'Your Name <your.email@example.com>',
    'description': 'A protocol to culture hMSC cells to spheroids in 96-well plates with or without osteoinduction supplements',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define the locations of the labware
    pcr_plate_96 = protocol.load_labware('sarstedt_96_wellplate_200ul', '1')
    plate_os_plus = protocol.load_labware('sarstedt_96_wellplate_200ul', '2')

    tipracks_300 = [
        protocol.load_labware('opentrons_96_filtertiprack_200ul', slot)
        for slot in ['3', '5', '6']
    ]

    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tipracks_300)

    def transfer_medium(dest_plate):
        for well in dest_plate.rows()[0]:
            p300.transfer(100, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '4').wells()[0], well)

    def add_os_plus(dest_plate):
        for well in dest_plate.rows()[0]:
            p300.transfer(0.1, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '4').columns()[0][0], well)
            p300.transfer(1, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '4').columns()[0][1], well)
            p300.transfer(1, protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '4').columns()[0][2], well)
    
    def transfer_cells(source_plate, dest_plate):
        for source_well, dest_well in zip(source_plate.rows()[0], dest_plate.rows()[0]):
            p300.transfer(100, source_well, dest_well)

    # Step 1: Transfer DMEM medium to each well of plate OS-
    protocol.comment('Transferring DMEM medium to each well of plate OS-')
    transfer_medium(pcr_plate_96)

    # Step 2: Transfer DMEM high glucose medium with osteoinduction supplements to each well of plate OS+
    protocol.comment('Transferring DMEM high glucose medium with osteoinduction supplements to each well of plate OS+')
    add_os_plus(plate_os_plus)

    # Step 3: Transfer hMSC cells to each well of plates OS- and OS+
    protocol.comment('Transferring hMSC cells to each well of plates OS- and OS+')
    source_plate = protocol.load_labware('agilent_6_wellplate_16ml', '7')
    transfer_cells(source_plate, pcr_plate_96)
    transfer_cells(source_plate, plate_os_plus)

    # End of the protocol
    protocol.comment('Protocol complete!')
