from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Lab Experiment',
    'author': 'Assistant',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1000])

    # Reagents
    pbs = tuberack.wells_by_name()['A1']  # PBS(-)
    trypsin = tuberack.wells_by_name()['A2']  # 0.25% trypsin solution
    dmem = tuberack.wells_by_name()['A3']  # DMEM medium

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs)
        for _ in range(5):
            p1000.dispense(1000, well)
            p1000.aspirate(1000, well)
        p1000.dispense(1000, pbs)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution and wait for 5 minutes
    p1000.distribute(1000, trypsin, [well.top() for well in well_plate.wells()])
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in well_plate.wells():
        p1000.transfer(1000, dmem, well, new_tip='always')

    # Step 4: Finish the experiment
    protocol.comment("Experiment finished.")
