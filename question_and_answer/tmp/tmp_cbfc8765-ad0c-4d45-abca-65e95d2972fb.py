from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid formation',
    'author': 'Name <email@address.com>',
    'description': 'Formation of hMSC spheroids in 96-well plates',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    plate_96s = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_6s = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Adding medium (DMEM) to all wells
    for plate in [plate_96s, plate_6s]:
        dmem = plate.columns()[0]
        protocol.transfer(100, medium, dmem)

    # Adding supplements for OS+ wells
    os_plus = plate_96s.columns()[1]
    supplements_source = protocol.load_labware('opentrons_24_tuberack_1500ul', '3')['A1']
    dex_volume = 0.1
    aa_volume = 1
    bgp_volume = 1
    supplements_os_plus = [well for well in os_plus]

    for idx in range(len(supplements_os_plus)):
        # Check for tip on pipette before attempting to add a new one
        if not protocol._implementation.get_is_tip_attached('p1000_single'):
            protocol.p1000.pick_up_tip()
    
        protocol.p1000.transfer(dex_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
        protocol.p1000.transfer(aa_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
        protocol.p1000.transfer(bgp_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
    
        # Test if the pipette has a tip attached before attempting to drop it
        if protocol._implementation.get_is_tip_attached('p1000_single'):
            protocol.p1000.drop_tip()
    
    # Adding cells to all wells
    cell_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    cell_source = plate_6s.columns()[0]
    cells_os_minus = [well for well in plate_96s.columns()[0]]
    cells_os_plus = [well for well in os_plus]

    for dest in cells_os_minus + cells_os_plus:
        # Check for tip on pipette before attempting to add a new one
        if not protocol._implementation.get_is_tip_attached('p1000_single'):
            protocol.p1000.pick_up_tip()

        protocol.p1000.transfer(100, cell_source, dest, mix_after=(3, 50), new_tip='never')
        
        # Test if the pipette has a tip attached before attempting to drop it
        if protocol._implementation.get_is_tip_attached('p1000_single'):
            protocol.p1000.drop_tip()

    print('Protocol complete')
