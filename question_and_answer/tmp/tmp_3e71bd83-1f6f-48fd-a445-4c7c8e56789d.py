from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',  # API level of your Opentrons machine
    'protocolName': 'Automated Lab Experiment',
    'description': 'Protocol for washing 6 well plate, adding trypsin solution and cell culture medium',
    'author': 'Your Name',
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = reagent_rack.wells_by_name()['A4']
    trypsin = reagent_rack.wells_by_name()['B4']
    medium = reagent_rack.wells_by_name()['C4']

    # Steps

    # 1. Wash the 6 well plate with PBS(-)
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, pbs, well, mix_after=(5, 1000))
        p1000.drop_tip()

    # 2. Add 1 mL of trypsin solution (0.25%) to the cell culture dish
    p1000.pick_up_tip()
    for well in well_plate.wells():
        p1000.transfer(1000, trypsin, well, new_tip='never')
    p1000.drop_tip()

    protocol.delay(minutes=5)  # Wait for 5 minutes

    # 3. Add 1 mL of cell culture medium (DMEM) to the 6 well plate
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(1000, medium, well)
        p1000.drop_tip()

    # 4. Finish the experiment
    protocol.comment('The experiment is complete.')
