from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    medium_dmem = protocol.load_labware('nest_1_reservoir_195ml', '2')
    medium_dmem_high_glucose = protocol.load_labware('nest_1_reservoir_195ml', '3')
    dex = protocol.load_labware('nest_1_reservoir_195ml', '4')
    aa = protocol.load_labware('nest_1_reservoir_195ml', '5')
    bgp = protocol.load_labware('nest_1_reservoir_195ml', '6')
    hmsc_cells = protocol.load_labware('nest_1_reservoir_195ml', '7')

    plate_osm = protocol.load_labware('nest_96_wellplate_200ul_flat', '8')
    plate_osp = protocol.load_labware('nest_96_wellplate_200ul_flat', '9')

    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack])

    # Transfer medium (DMEM) to each well of plate (OS-)
    for well in plate_osm.wells():
        p300.pick_up_tip()
        p300.transfer(100, medium_dmem.wells()[0], well, new_tip='never')
        p300.drop_tip()

    # Transfer medium (DMEM high glucose) to each well of plate (OS+)
    for well in plate_osp.wells():
        p300.pick_up_tip()
        p300.transfer(100, medium_dmem_high_glucose.wells()[0], well, new_tip='never')
        p300.drop_tip()

    # Add osteoinduction supplements to each well of the plate (OS+)
    for well in plate_osp.wells():
        p300.pick_up_tip()
        p300.transfer(0.1, dex.wells()[0], well, new_tip='never')
        p300.transfer(1, aa.wells()[0], well, new_tip='never')
        p300.transfer(1, bgp.wells()[0], well, new_tip='never')
        p300.drop_tip()

    # Transfer hMSC cells to each well of plates (OS- and OS+)
    for well in plate_osm.wells() + plate_osp.wells():
        p300.pick_up_tip()
        p300.transfer(100, hmsc_cells.wells()[0], well, new_tip='never')
        p300.drop_tip()
