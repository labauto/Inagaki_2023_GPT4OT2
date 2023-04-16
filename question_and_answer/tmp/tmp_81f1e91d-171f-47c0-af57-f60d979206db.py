from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Laboratory Experiment',
    'author': 'Assistant',
    'description': 'Wash 6 well plate, add trypsin solution and cell culture medium',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware setup
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    falcon_tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    wellplate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Pipette setup
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagent setup
    PBS_minus = falcon_tuberack.wells_by_name()['A1']
    trypsin_solution = falcon_tuberack.wells_by_name()['A2']
    DMEM = falcon_tuberack.wells_by_name()['A3']

    # Protocol steps:
    # 1. Wash the 6 well plate with PBS(-) by pipetting up and down 5 times
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.transfer(1000, PBS_minus, well.top(), mix_after=(5, 1000), new_tip='never')
        pipette.drop_tip()

    # 2. Add 1 ml of trypsin solution (0.25%) to the cell culture dish
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.transfer(1000, trypsin_solution, well.top(), new_tip='never', mix_after=(1, 1000))
        pipette.drop_tip()

    # 3. Wait for 5 minutes
    protocol.delay(minutes=5)

    # 4. Add 1 mL of cell culture medium (DMEM) to the 6 well plate.
    for well in wellplate.wells():
        pipette.pick_up_tip()
        pipette.transfer(1000, DMEM, well.top(), new_tip='never', mix_after=(1, 1000))
        pipette.drop_tip()

    # 5. Finish the experiment
    protocol.comment('Experiment completed successfully.')
