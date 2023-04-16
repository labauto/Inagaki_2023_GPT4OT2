import opentrons.protocol_api as protocol_api

metadata = {
    'protocolName': 'hMSC spheroids in 96 well plates',
    'author': 'Your Name Here',
    'apiLevel': '2.0'
}

# function to transfer liquid with given volume from one well to another
def transfer(source, dest, volume):
    p300.pick_up_tip()
    p300.aspirate(volume, source)
    p300.dispense(volume, dest)
    p300.drop_tip()

# create protocol object
def run(protocol: protocol_api.ProtocolContext):

    # labware and pipettes
    plate_6_TC = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    plate_96_f = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    p300 = protocol.load_instrument('p300_single', 'left')

    # OS- condition: transfer DMEM to all wells (100 µl per well)
    dests_os_negative = [well for row in plate_96_f.rows() for well in row[0:6]]
    for dest in dests_os_negative:
        transfer(plate_6_TC['B1'], dest, 100)

    # OS+ condition: transfer DMEM high glucose to all wells (100 µl per well)
    dests_os_positive = [well for row in plate_96_f.rows() for well in row[6:]]
    for dest in dests_os_positive:
        transfer(plate_6_TC['C1'], dest, 100)

    # OS+ condition: add Dexamethasone, Ascorbic acid, and beta-glycerophosphate (0.1 µl Dex, 1 µl AA, and 1 µl BGP per well)
    source_location_dex = plate_6_TC['C2']
    source_location_aa = plate_6_TC['C3']
    source_location_bgp = plate_6_TC['C4']
    for dest in dests_os_positive:
        transfer(source_location_dex, dest, 0.1)
        transfer(source_location_aa, dest, 1)
        transfer(source_location_bgp, dest, 1)

    # transfer hMSC cells to all wells (100 µl per well)
    source_location_cells = plate_6_TC['A1']
    for dest in dests_os_negative + dests_os_positive:
        transfer(source_location_cells, dest, 100)

    # print message when the protocol is completed
    protocol.comment('Protocol complete.')
