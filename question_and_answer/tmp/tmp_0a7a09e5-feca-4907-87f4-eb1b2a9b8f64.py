from opentrons import protocol_api

metadata = {
    'protocolName': 'Lab Experiment',
    'author': 'Assistant',
    'description': 'Opentrons laboratory experiment protocol',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

    # Reagents
    PBS_minus = tiprack.wells_by_name()['A1']
    trypsin_solution = tiprack.wells_by_name()['A2']
    DMEM = tiprack.wells_by_name()['A3']

    # Protocol steps
    # Step 1: Wash the 6 well plate with PBS(-)
    for well in six_well_plate.wells():
        p1000.transfer(1000, PBS_minus, well, mix_after=(5, 1000))

    # Step 2: Add 1 ml of trypsin solution (0.25%)
    p1000.delay(minutes=5)
    for well in six_well_plate.wells():
        p1000.transfer(1000, trypsin_solution, well)

    # Step 3: Add 1 mL of cell culture medium (DMEM)
    for well in six_well_plate.wells():
        p1000.transfer(1000, DMEM, well)

    # Step 4: Finish the experiment
    protocol.comment('Experiment complete.')
