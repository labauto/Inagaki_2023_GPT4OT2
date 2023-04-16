from opentrons import protocol_api

metadata = {
    'protocolName': 'Lab Automation Protocol',
    'author': 'Assistant',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', 2)])
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    # Reagents
    pbs_minus = tuberack.wells_by_name()['A1']
    trypsin_solution = tuberack.wells_by_name()['A2']
    cell_culture_medium = tuberack.wells_by_name()['A3']

    # Protocol Steps
    # Step 1
    for well in plate.wells():
        pipette.pick_up_tip()
        for _ in range(5):
            pipette.aspirate(1000, pbs_minus)
            pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 2
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, trypsin_solution)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    protocol.delay(minutes=5)

    # Step 3
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, cell_culture_medium)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    # Step 4: End of the experiment
