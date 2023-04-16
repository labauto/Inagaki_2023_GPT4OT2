from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    trypsin_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    pbs_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 4)
    
    # Pipette
    p1000_single = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1000])
    
    # Protocol Steps

    # Step 1: Washing the 6 well plate with PBS(-) by pipetting up and down 5 times.
    for well in well_plate.wells():
        p1000_single.pick_up_tip()
        p1000_single.transfer(
            1000,
            pbs_tube_rack['A1'],
            well,
            mix_after=(5, 1000),
            new_tip='never'
        )
        p1000_single.blow_out(well.top())
        p1000_single.drop_tip()
        
    # Step 2: Adding 1 ml trypsin solution (0.25%) to the cell culture dish and waiting for 5 minutes.
    for well in well_plate.wells():
        p1000_single.transfer(
            1000,
            trypsin_tube_rack['A2'],
            well,
            new_tip='once'
        )
    protocol.delay(minutes=5)
    
    # Step 3: Adding 1 mL of cell culture medium (DMEM) to the 6 well plate.
    for well in well_plate.wells():
        p1000_single.transfer(
            1000,
            trypsin_tube_rack['A3'],
            well,
            new_tip='once'
        )
        
    # Step 4: Finishing the experiment.
    protocol.comment('Experiment Finished.')
