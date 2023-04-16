from opentrons import protocol_api

metadata = {
    'protocolName': 'Lab Automation Protocol',
    'author': 'Your Name',
    'description': 'Automated experiment for washing well plate, trypsin solution, and medium addition',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Pipettes
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    trypsin_solution = tuberack.wells_by_name()['A2']
    dmem_medium = tuberack.wells_by_name()['A3']

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-)
    pipette.pick_up_tip()
    for well in well_plate.wells():
        for _ in range(5):
            pipette.aspirate(1000, pbs_minus)
            pipette.dispense(1000, well)
    pipette.drop_tip()

    # Step 2: Add trypsin solution to the cell culture dish
    pipette.pick_up_tip()
    for well in well_plate.wells():
        pipette.aspirate(1000, trypsin_solution)
        pipette.dispense(1000, well)
    pipette.drop_tip()

    # Wait for 5 minutes
    protocol.delay(minutes=5)

    # Step 3: Add cell culture medium (DMEM) to the 6 well plate
    pipette.pick_up_tip()
    for well in well_plate.wells():
        pipette.aspirate(1000, dmem_medium)
        pipette.dispense(1000, well)
    pipette.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment('The experiment has been completed.')
