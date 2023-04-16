from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    falcon_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    
    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single', mount='right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_1000ul', 3)])
    
    # Wash wells with PBS(-)
    p1000.pick_up_tip()
    for well in well_plate.wells():
        p1000.aspirate(1000, falcon_tuberack.wells('A1').bottom(10))
        for _ in range(5):
            p1000.dispense(200, well.bottom(10))
            p1000.aspirate(200, well.bottom(10))
    p1000.drop_tip()
    
    # Add trypsin solution and wait
    p1000.pick_up_tip()
    for well in well_plate.wells():
        p1000.aspirate(1000, falcon_tuberack.wells('A2').bottom(10))
        p1000.dispense(1000, well.bottom(10))
    p1000.delay(minutes=5)
    p1000.drop_tip()
    
    # Add cell culture medium and finish
    p1000.pick_up_tip()
    for well in well_plate.wells():
        p1000.aspirate(1000, falcon_tuberack.wells('A3').bottom(10))
        p1000.dispense(1000, well.bottom(10))
    p1000.drop_tip()


:*************************


