from opentrons import protocol_api

metadata = {
    'protocolName': 'Automate Laboratory Experiment',
    'author': 'Assistant',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware and Pipettes
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    pipette_1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1000])
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Reagents
    PBS = tuberack.wells_by_name()['A1']
    trypsin = tuberack.wells_by_name()['A2']
    DMEM = tuberack.wells_by_name()['A3']
    
    # Steps

    # Step 1: Wash the 6-well plate with 1 ml of PBS(-)
    for well in well_plate.wells():
        pipette_1000.pick_up_tip()
        pipette_1000.aspirate(1000, PBS)
        for _ in range(5):
            pipette_1000.dispense(1000, well)
            pipette_1000.aspirate(1000, well)
        pipette_1000.drop_tip()

    # Step 2: Add 1 mL of trypsin solution (0.25%) to the cell culture dish
    protocol.delay(minutes=5)

    for well in well_plate.wells():
        pipette_1000.pick_up_tip()
        pipette_1000.aspirate(1000, trypsin)
        pipette_1000.dispense(1000, well)
        pipette_1000.drop_tip()

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6-well plate
    for well in well_plate.wells():
        pipette_1000.pick_up_tip()
        pipette_1000.aspirate(1000, DMEM)
        pipette_1000.dispense(1000, well)
        pipette_1000.drop_tip()

    # Finish the experiment
    protocol.comment('The experiment is now complete.')
