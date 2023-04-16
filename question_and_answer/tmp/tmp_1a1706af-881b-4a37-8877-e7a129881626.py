from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    
    # Pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = reagent_rack.wells_by_name()['A1']
    trypsin = reagent_rack.wells_by_name()['A2']
    dmem = reagent_rack.wells_by_name()['A3']

    # Protocol Steps
    # Step 1: Wash the 6-well plate with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        for i in range(5):
            p1000.aspirate(1000, pbs)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Wait for 5 minutes
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
