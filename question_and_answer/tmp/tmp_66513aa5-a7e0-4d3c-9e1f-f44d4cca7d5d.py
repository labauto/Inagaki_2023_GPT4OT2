from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tiprack_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 3)
    tiprack_200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200ul])

    # Task 6: Transfer 30 µL of 1mM Thapsigargin from tube A1 to wells A2-A6 and B1 of tube_rack_10
    p20.pick_up_tip()
    for well in ['A2', 'A3', 'A4', 'A5', 'A6', 'B1']:
        p20.aspirate(20, tube_rack_10['A1'])
        p20.dispense(20, tube_rack_10[well])
        p20.mix(3, 20, tube_rack_10[well])
    p20.drop_tip()

    # Rest of the tasks, make sure to adjust pipette volumes accordingly
