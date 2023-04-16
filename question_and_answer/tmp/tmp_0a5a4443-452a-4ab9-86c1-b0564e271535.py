from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Culture',
    'author': 'Your Name <youremail@yourinstitution.com>',
    'description': 'A protocol for culturing hMSC spheroids in two different conditions',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[
        protocol.load_labware('opentrons_96_tiprack_1000ul', '4')
    ])

    # Define transfer volumes and locations
    medium_volume = 100
    cell_volume = 100
    dex_volume = 0.1
    aa_volume = 1
    bgp_volume = 1

    medium_os_minus = plate_96_well.rows()[0]
    medium_os_plus = plate_96_well.rows()[1]
    cells_os_minus = plate_96_well.rows()[2]
    cells_os_plus = plate_96_well.rows()[3]

    supplements_os_plus = medium_os_plus

    # Define reagent location and pick up tips
    supplements_source = plate_6_well.rows()[0][0]
    p1000.pick_up_tip()

    # Transfer medium (DMEM) to 96 well plate (OS-)
    for idx in range(len(medium_os_minus)):
        p1000.transfer(medium_volume, supplements_source, medium_os_minus[idx],
                       new_tip='never')

    # Transfer medium (DMEM high glucose) to 96 well plate (OS+)
    for idx in range(len(medium_os_plus)):
        p1000.transfer(medium_volume, supplements_source, medium_os_plus[idx],
                       new_tip='never')
        
        # Add osteoinduction supplements to medium in 96 well plate (OS+)
        p1000.transfer(dex_volume, supplements_source, supplements_os_plus[idx], new_tip='always')
        p1000.transfer(aa_volume, supplements_source, supplements_os_plus[idx], new_tip='always')
        p1000.transfer(bgp_volume, supplements_source, supplements_os_plus[idx], new_tip='always')

    # Transfer hMSC cells to 96 well plate (OS-)
    for idx in range(len(cells_os_minus)):
        p1000.transfer(cell_volume, supplements_source, cells_os_minus[idx],
                       new_tip='always')

    # Transfer hMSC cells to 96 well plate (OS+)
    for idx in range(len(cells_os_plus)):
        p1000.transfer(cell_volume, supplements_source, cells_os_plus[idx],
                       new_tip='always')

    # Drop tips
    p1000.drop_tip()
