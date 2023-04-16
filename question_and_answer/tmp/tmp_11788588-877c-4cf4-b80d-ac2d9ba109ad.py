from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name',
    'description': 'A protocol for washing and trypsinizing cells in a 6 well plate.',
    'apiLevel': '2.12'
}

# Define labware and pipettes
tips_300 = [protocol_api.labware.load('opentrons_96_tiprack_300ul', slot)
            for slot in ['1', '2']]
tips_1000 = [protocol_api.labware.load('opentrons_96_tiprack_1000ul', slot)
             for slot in ['3']]
plate = protocol_api.labware.load('corning_6_wellplate_16.8ml_flat', '4')
wash_tube = protocol_api.labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '5')
trypsin_tube = protocol_api.labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '6')
p300 = protocol_api.instruments.P300_Single(mount='left', tip_racks=tips_300)
p1000 = protocol_api.instruments.P1000_Single(mount='right', tip_racks=tips_1000)

def run(protocol: protocol_api.ProtocolContext):
    # Wash wells with PBS(-)
    p300.pick_up_tip()
    for well in plate.wells():
        for _ in range(5):
            p300.aspirate(200, wash_tube.wells()[0])
            p300.dispense(200, well)
    p300.drop_tip()

    # Add trypsin and wait
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(2000, trypsin_tube.wells()[0])
        p1000.dispense(2000, well)
    protocol.delay(minutes=5)

    # Add cell culture medium
    p1000.pick_up_tip()
    for well in plate.wells():
        p1000.aspirate(5000, wash_tube.wells()[0])
        p1000.dispense(5000, well)
    p1000.drop_tip()
