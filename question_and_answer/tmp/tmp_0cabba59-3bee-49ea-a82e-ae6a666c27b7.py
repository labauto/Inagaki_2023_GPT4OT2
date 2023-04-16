from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Automated Lab Experiment'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Locate reagents
    pbs = tube_rack.wells_by_name()['A1']
    trypsin = tube_rack.wells_by_name()['B1']
    dmem = tube_rack.wells_by_name()['A2']

    # Step 1: Wash the wells with 1 ml of PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):  # repeat 5 times
            p1000.aspirate(1000, pbs)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 ml of trypsin solution (0.25%) to the wells
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Pause for 5 minutes
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment
    protocol.comment("Experiment finished.")
