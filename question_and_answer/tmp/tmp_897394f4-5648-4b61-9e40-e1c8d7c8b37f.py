from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Trypsinization',
    'author': 'Your Name Here',
    'description': 'A protocol to wash a 6-well plate with PBS and add trypsin and cell culture medium',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # labware
    pcr_strip = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "1")
    well_plate = protocol.load_labware("corning_6_wellplate_16.8ml_flat", "2")
    tiprack_1 = protocol.load_labware("opentrons_96_tiprack_1000ul", "3")

    # pipettes
    pipette_1000 = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tiprack_1])

    # steps
    pipette_1000.pick_up_tip()
    for well in well_plate.rows()[0][:]:
        pipette_1000.transfer(1000, pcr_strip.wells()[0], well, new_tip="never")
        pipette_1000.mix(5, 1000, well)
    pipette_1000.drop_tip()

    pipette_1000.pick_up_tip()
    for well in well_plate.rows()[0][:]:
        pipette_1000.transfer(1000, pcr_strip.wells()[1], well, new_tip="never")
        pipette_1000.mix(5, 1000, well)
        protocol.delay(minutes=5)
    pipette_1000.drop_tip()

    pipette_1000.pick_up_tip()
    for well in well_plate.rows()[0][:]:
        pipette_1000.transfer(1000, pcr_strip.wells()[2], well, new_tip="never")
        pipette_1000.mix(5, 1000, well)
    pipette_1000.drop_tip()
