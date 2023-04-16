from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Automated Laboratory Experiment',
    'author': 'Assistant',
    'description': 'Python script for automating biology experiment using Opentrons machine',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    
    # Pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])
    
    # Solutions
    PBS_minus = tuberack.wells_by_name()['A1']
    trypsin_solution = tuberack.wells_by_name()['A2']
    DMEM_medium = tuberack.wells_by_name()['A3']

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(1000, PBS_minus)
            pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 2: Add 1 ml trypsin (0.25%) to the 6 well plate
    for well in well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, trypsin_solution)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    protocol.delay(minutes=5) # 5 minute waiting time

    # Step 3: Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, DMEM_medium)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 4: Finish the experiment
