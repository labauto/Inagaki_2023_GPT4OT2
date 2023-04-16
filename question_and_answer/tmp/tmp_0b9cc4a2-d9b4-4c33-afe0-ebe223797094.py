from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'Automated Lab Experiment',
    'description': 'Automated lab experiment using Opentrons',
    'author': 'Opentrons Helper'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)

    # Pipette
    p1000 = protocol.load_instrument('p1000_single', mount='right', tip_racks=[tips])

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    trypsin_sol = tuberack.wells_by_name()['B1']
    dmem = tuberack.wells_by_name()['C1']

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs_minus)
        for _ in range(5):
            p1000.dispense(1000, well)
            p1000.aspirate(1000, well)
        p1000.return_tip()

    # Step 2: Add trypsin solution to the cell culture dish
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin_sol)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Wait for 5 minutes.
    protocol.delay(minutes=5)

    # Step 3: Add DMEM to the 6 well plate
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment("Experiment completed!")
