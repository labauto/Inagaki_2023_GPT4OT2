from opentrons import protocol_api

metadata = {
    'protocolName': 'Automated Laboratory Experiment',
    'author': 'Assistant',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    well_plate = protocol.load_labware('corning_6_wellplate_16_8ml_flat', 3)

    # Pipettes
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tips])

    # Reagents
    pbs_minus = tube_rack['A1']
    trypsin_solution = tube_rack['A2']
    dmem_medium = tube_rack['A3']

    # Wash 6 well plate with PBS(-)
    for well in well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, pbs_minus)
        pipette.dispense(1000, well)
        for _ in range(5):
            pipette.aspirate(800, well)
            pipette.dispense(800, well)
        pipette.drop_tip()

    # Add trypsin solution to cell culture dish
    for well in well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, trypsin_solution)
        pipette.dispense(1000, well)
        pipette.drop_tip()

    # Wait for 5 minutes
    protocol.delay(minutes=5)

    # Add DMEM to 6 well plate
    for well in well_plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, dmem_medium)
        pipette.dispense(1000, well)
        pipette.drop_tip()
