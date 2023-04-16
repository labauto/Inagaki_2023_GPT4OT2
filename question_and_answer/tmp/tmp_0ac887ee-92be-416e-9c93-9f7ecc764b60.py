from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    
    def transfer_medium(dest_plate):
        for i in range(12):
            for j in range(8):
                well_id = chr(ord('A') + j) + str(i + 1)
                pipette.transfer(100, medium_reservoir.wells()[i], dest_plate.wells(well_id))
            
    def add_supplements(dest_plate):
        for supplement, volume in ((dex, 0.1), (aa, 1), (bgp, 1)):
            for i in range(12):
                for j in range(8):
                    well_id = chr(ord('A') + j) + str(i + 1)
                    pipette.transfer(volume, supplement, dest_plate.wells(well_id), mix_after=(5, 10))
    
    def transfer_cells(dest_plate):
        for i in range(12):
            for j in range(8):
                well_id = chr(ord('A') + j) + str(i + 1)
                pipette.transfer(100, cells_reservoir.wells()[i], dest_plate.wells(well_id))

    # Load labware
    medium_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '1')
    cells_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    plate_os_minus = protocol.load_labware('nest_96_wellplate_200ul', '3')
    plate_os_plus = protocol.load_labware('nest_96_wellplate_200ul', '4')
    dex = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '5').wells('A1')
    aa = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '5').wells('A2')
    bgp = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '5').wells('A3')
    
    # Load pipette
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '6')])

    # Steps
    transfer_medium(plate_os_minus)
    transfer_medium(plate_os_plus)
    add_supplements(plate_os_plus)
    transfer_cells(plate_os_minus)
    transfer_cells(plate_os_plus)
