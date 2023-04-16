from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell culture experiment',
    'author': 'Your Name',
    'description': 'An Opentrons protocol for a cell culture experiment',
    'apiLevel': '2.11'
}

# Define the labware
def run(protocol: protocol_api.ProtocolContext):
    # Define the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Define the pipettes
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])

    # Define the reagents
    pbs = pbs_tuberack['A1']
    trypsin = pbs_tuberack['A2']
    dmem = pbs_tuberack['A3']

    # Protocol Steps
    # Wash wells with PBS(-)
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs)
        p300.dispense(100, well)
        for i in range(5):
            p300.mix(1, 50, well)
        p300.drop_tip()

    # Add trypsin and wait for 5 minutes
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, trypsin)
        p300.dispense(200, well)
        protocol.delay(minutes=5)
        p300.drop_tip()

    # Add DMEM
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(500, dmem)
        p300.dispense(500, well)
        p300.drop_tip()
