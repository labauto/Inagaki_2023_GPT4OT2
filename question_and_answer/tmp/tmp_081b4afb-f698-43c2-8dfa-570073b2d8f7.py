from opentrons import protocol_api

metadata = {
    'protocolName': 'Lab Automation Protocol',
    'author': 'Your Name',
    'description': 'A protocol for washing and treating cell cultures',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):

    # Define labware
    falcon_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    p1000_tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    p300_tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Define pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[p1000_tiprack])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[p300_tiprack])

    # Define reagents
    pbs_minus = falcon_tube_rack['A1']
    trypsin = falcon_tube_rack['B1']
    cell_medium = falcon_tube_rack['C1']

    # Wash the well plate with PBS(-)
    for well in well_plate.wells():
        for _ in range(5):
            p1000.pick_up_tip()
            p1000.aspirate(1000, pbs_minus)
            p1000.dispense(1000, well)
            p1000.mix(5, 500)
            p1000.drop_tip()

    # Add trypsin to the well plate and wait for 5 minutes
    for well in well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(1000, trypsin)
        p300.dispense(1000, well)
        p300.mix(5, 500)
        p300.drop_tip()

    protocol.delay(minutes=5)

    # Add cell culture medium (DMEM) to the well plate
    for well in well_plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, cell_medium)
        p1000.dispense(1000, well)
        p1000.drop_tip()
