from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Automated Cell Culture',
    'author': 'Username',
    'description': 'An automated cell culture experiment using Opentrons',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')

    # Pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tube_rack.wells_by_name()['A1']     # PBS(-) in A1 of tube_rack
    trypsin = tube_rack.wells_by_name()['A2'] # Trypsin (0.25%) in A2 of tube_rack
    dmem = tube_rack.wells_by_name()['A3']    # DMEM in A3 of tube_rack

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs)
        p1000.dispense(1000, well)
        p1000.mix(5, 1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in six_well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment("Cell culture experiment finished.")
