from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)
    
    # Pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    PBS = reagent_rack.wells_by_name()['A1']
    trypsin = reagent_rack.wells_by_name()['A2']
    DMEM = reagent_rack.wells_by_name()['A3']

    # Step 1: Wash with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, PBS, well, mix_after=(5, 1000), new_tip='never')
        p1000.drop_tip()

    # Step 2: Add trypsin
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, trypsin, well, new_tip='never')
        p1000.drop_tip()
    
    protocol.delay(minutes=5)

    # Step 3: Add DMEM
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, DMEM, well, new_tip='never')
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment("Experiment finished.")
