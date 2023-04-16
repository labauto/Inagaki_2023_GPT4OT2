from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Load pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagent wells in tuberack
    pbs_well = tuberack.wells_by_name()['A1']  # PBS(-)
    trypsin_well = tuberack.wells_by_name()['B1']  # trypsin solution
    dmem_well = tuberack.wells_by_name()['C1']  # DMEM

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        pipette.pick_up_tip()
        for _ in range(5):  # Pipetting up and down 5 times
            pipette.transfer(1000, pbs_well, well, mix_after=(5, 1000), new_tip='never')
        pipette.drop_tip()

    # Step 2: Add 1 ml trypsin solution
    for well in well_plate.wells():
        pipette.transfer(1000, trypsin_well, well)

    # Waiting for 5 minutes
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM)
    for well in well_plate.wells():
        pipette.transfer(1000, dmem_well, well)

    # Step 4: Finish the experiment is implicit as the script ends here
