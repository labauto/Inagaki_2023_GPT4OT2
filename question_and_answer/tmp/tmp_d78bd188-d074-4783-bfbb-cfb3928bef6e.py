from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Your Name <youremail@example.com>',
    'description': 'An example protocol for exchanging hMSC cell culture medium with PBS(-) and D-MEM',
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '7')
    p300_single = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_300])
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')
    pbs_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '5')
    dm_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '6')

    # Preparing Tubes
    pbs = pbs_tube.wells('A1')
    dm = dm_tube.wells('A2')

    # Transfer to 6-well Plate
    for well in plate_6_well.columns()[0]:
        p300_single.pick_up_tip()
        p300_single.transfer(1000, pbs, well)
        p300_single.transfer(1000, dm, well)
        p300_single.mix(5, 300, well)
        p300_single.drop_tip()

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.7')
    run(protocol)

