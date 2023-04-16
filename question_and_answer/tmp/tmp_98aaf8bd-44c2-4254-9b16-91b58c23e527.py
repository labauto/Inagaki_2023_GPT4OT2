from opentrons import protocol_api

# Define the protocol
metadata = {
    'protocolName': 'Cell Culture Experiment',
    'author': 'Your Name',
    'description': 'A protocol to wash a cell culture dish and add trypsin and medium.',
    'apiLevel': '2.7'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):

    # Load the pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[])
    p200 = protocol.load_instrument('p200_single', 'left', tip_racks=[])

    # Define the labware
    wash_tube = protocol.load_labware('opentrons_50ml_tube', 1)
    culture_dish = protocol.load_labware('corning_90mm_non-treated_petri_dish', 2)
    medium_tube = protocol.load_labware('opentrons_10ml_1_well_tube', 3)

    # Define the reagents
    pbs = wash_tube.wells()[0]
    trypsin = wash_tube.wells()[1]
    medium = medium_tube.wells()[0]

    # Wash the culture dish with PBS(-)
    for i in range(5):
        p1000.pick_up_tip()
        p1000.aspirate(200, pbs)
        p1000.dispense(200, culture_dish.wells()[0])
        p1000.aspirate(200, culture_dish.wells()[0])
        p1000.dispense(200, pbs)
        p1000.mix(5, 200)
        p1000.drop_tip()

    # Add trypsin and wait for 5 minutes
    p200.pick_up_tip()
    p200.aspirate(300, trypsin)
    p200.dispense(300, culture_dish.wells()[0])
    protocol.delay(minutes=5)
    p200.drop_tip()

    # Add cell culture medium
    p1000.pick_up_tip()
    p1000.aspirate(10000, medium)
    p1000.dispense(10000, culture_dish.wells()[0])
    p1000.drop_tip()

    # Finish the experiment
    protocol.comment('Experiment finished.')
