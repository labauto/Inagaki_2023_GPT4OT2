from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10', 
    'protocolName': 'Automate Laboratory Experiment',
    'author': 'Assistant',
    'description': 'A protocol to perform the given experiment steps on an Opentrons robot'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware setup
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)

    p1000_tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 2)
    
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Pipette setup
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[p1000_tiprack])
    
    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1'] 
    trypsin = tuberack.wells_by_name()['A2']
    dmem = tuberack.wells_by_name()['A3']
    
    # Protocol
    # Step 1: Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        for _ in range(5):
            p1000.aspirate(1000, pbs_minus)
            p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 2: Add 1 mL of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.drop_tip()
        
    protocol.delay(minutes=5)

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.drop_tip()

    # Step 4: Finish the experiment (no actions needed)
