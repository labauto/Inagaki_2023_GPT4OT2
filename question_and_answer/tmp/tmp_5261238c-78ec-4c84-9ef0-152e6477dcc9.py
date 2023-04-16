from opentrons import protocol_api

metadata = {
    'protocolName': 'Example Protocol',
    'author': 'Your Name <your.name@example.com>',
    'description': 'Example protocol to run Opentrons machine.',
    'apiLevel': '2.0'
}

# Define our protocol run function.
def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    
    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'left')

    # Reagent volume settings
    pbs_volume = 1000 # μL
    trypsin_volume = 1000 # μL
    medium_volume = 1000 # μL

    # Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well, use 1 ml of PBS(-).
    # (PBS volume set in the variables above)

    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(pbs_volume, tube_rack['A1'])
        p1000.dispense(pbs_volume, well)
        for i in range(5):
            p1000.aspirate(200, well)
            p1000.dispense(200, well)
        p1000.drop_tip()

    # After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
    # (Trypsin volume set in the variables above)
    
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(trypsin_volume, tube_rack['A2'])
        p1000.dispense(trypsin_volume, well)
        p1000.delay(minutes=5)

    # Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
    # (Medium volume set in the variables above)
    
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(medium_volume, tube_rack['A3'])
        p1000.dispense(medium_volume, well)
        p1000.drop_tip()
