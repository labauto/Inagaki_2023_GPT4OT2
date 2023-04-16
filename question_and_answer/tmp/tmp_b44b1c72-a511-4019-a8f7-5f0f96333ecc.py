from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', 3)

    # Pipettes
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = reagent_rack.wells_by_name()['A1']
    trypsin = reagent_rack.wells_by_name()['B1']
    medium = reagent_rack.wells_by_name()['C1']

    # Protocol Steps
    # Step 1: Wash 6 well plate with PBS(-) by pipetting up and down 5 times using 1 ml of PBS(-) for each well
    wash_volume = 1000
    for well in well_plate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(wash_volume, pbs)
            pipette.dispense(wash_volume, well)
        pipette.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    trypsin_volume = 1000
    for well in well_plate.wells():
        pipette.transfer(trypsin_volume, trypsin, well)
    
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    medium_volume = 1000
    for well in well_plate.wells():
        pipette.transfer(medium_volume, medium, well)

    # Step 4: Finish the experiment
    protocol.comment("Experiment completed.")
