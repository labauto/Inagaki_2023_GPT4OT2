from opentrons import protocol_api

metadata = {
    'protocolName': 'Exchange hMSC cell culture medium',
    'author': 'Opentrons',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    pbs = protocol.load_labware('opentrons_6_reservoir_50000ul', '3', 'PBS(-)')
    dmem = protocol.load_labware('opentrons_6_reservoir_50000ul', '6', 'D-MEM')

    # Load pipette
    p300_multi = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack])

    # Load trash
    trash = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '5', 'Trash')

    # Transfer old culture medium to waste (A1 well of trash labware)
    for well_index in range(3):
        p300_multi.pick_up_tip()
        p300_multi.transfer(200, well_plate.rows()[0][well_index], trash['A1'].top(), new_tip='never')
        p300_multi.drop_tip()

    # Transfer PBS(-) to wells
    for well_index in range(3):
        p300_multi.pick_up_tip()
        p300_multi.transfer(200, pbs['A1'], well_plate.rows()[0][well_index], new_tip='never')
        p300_multi.drop_tip()

    # Exchange PBS(-) with fresh D-MEM
    for well_index in range(3):
        p300_multi.pick_up_tip()
        p300_multi.transfer(200, well_plate.rows()[0][well_index], trash['A1'].top(), new_tip='never')
        p300_multi.transfer(200, dmem['A1'], well_plate.rows()[0][well_index], new_tip='never')
        p300_multi.drop_tip()

