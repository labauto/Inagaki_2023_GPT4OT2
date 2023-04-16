# Import modules
from opentrons import protocol_api

# Protocol metadata
metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your Name Here',
    'description': 'Opentrons protocol for hMSC spheroid culture',
    'apiLevel': '2.4'
}

# Protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # Labware definition
    medium = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    dmem = protocol.load_labware('corning_6_wellplate_16.2ml_flat', '2')
    supplements_source = dmem['A1']
    plate_96_wells_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.2ml_flat', '4')

    # Pipette definition
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '5')])

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    p1000.transfer(100, medium, plate_96_wells_os_minus.wells(), new_tip='once')

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    plate_96_wells_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    p1000.pick_up_tip()
    for i, well in enumerate(plate_96_wells_os_plus.wells()):
        if i == 0:
            p1000.transfer(100, medium, well, new_tip='never')
        else:
            p1000.transfer(100, medium, well, new_tip='always')
    p1000.drop_tip()

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    dex_volume = 0.1
    aa_volume = 1
    bgp_volume = 1
    supplements_os_plus = [plate_6_wells['B1'], plate_6_wells['A1']]
    for idx, dest in enumerate(plate_96_wells_os_plus.wells()):
        p1000.pick_up_tip()
        p1000.transfer(dex_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
        p1000.mix(3, 100, supplements_os_plus[idx])
        p1000.transfer(aa_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
        p1000.mix(3, 100, supplements_os_plus[idx])
        p1000.transfer(bgp_volume, supplements_source, supplements_os_plus[idx], new_tip='never')
        p1000.mix(3, 100, supplements_os_plus[idx])
        p1000.transfer(dex_volume + aa_volume + bgp_volume, supplements_os_plus[idx], dest, new_tip='never')
        p1000.mix(3, 100, dest)
        p1000.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    cells_source = dmem['A2']
    cells_volume = 100
    p1000.pick_up_tip()
    for dest in plate_96_wells_os_minus.wells():
        p1000.transfer(cells_volume, cells_source, dest, new_tip='never')
    p1000.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    p1000.pick_up_tip()
    for dest in plate_96_wells_os_plus.wells():
        p1000.transfer(cells_volume, cells_source, dest, new_tip='never')
    p1000.drop_tip()

    # End
