from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Protocol',
    'author': 'Your Name <your.email@your-institution.org>',
    'description': 'A protocol for washing and trypsinizing cells in a 6-well plate',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware and pipettes
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    pipette = protocol.load_instrument('p1000_single', tip_racks=[tiprack])

    # Define volumes
    pbs_volume = 1000  # µL
    trypsin_volume = 1000  # µL
    medium_volume = 1000  # µL

    # Set up the experiment
    pbs = tuberack['A1']
    trypsin = tuberack['A2']
    medium = tuberack['A3']

    pipette.pick_up_tip()

    # Wash the plate with PBS(-)
    for well in plate.wells():
        pipette.aspirate(pbs_volume, pbs)
        pipette.dispense(pbs_volume, well)
        for i in range(5):
            pipette.mix(1, pbs_volume)
    pipette.drop_tip()

    # Add trypsin to the plate and wait for 5 minutes
    pipette.pick_up_tip()
    for well in plate.wells():
        pipette.aspirate(trypsin_volume, trypsin)
        pipette.dispense(trypsin_volume, well)
        pipette.mix(1, trypsin_volume)
    protocol.delay(minutes=5)
    pipette.drop_tip()

    # Add medium to the plate
    pipette.pick_up_tip()
    for well in plate.wells():
        pipette.aspirate(medium_volume, medium)
        pipette.dispense(medium_volume, well)
    pipette.drop_tip()
