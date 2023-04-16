from opentrons import protocol_api

metadata = {'apiLevel': '2.9'}

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')
    pbs_tube = protocol.load_labware('eppendorf_15_ml_falcon', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Aspirate and dispense PBS(-) to wash the cells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(1000, pbs_tube['A1'])
        p300.dispense(1000, well)
        p300.mix(3, 1000, well)
        p300.aspirate(1000, well)
        p300.dispense(1000, reservoir['A1'])
        p300.drop_tip()

    # Aspirate and dispense D-MEM to replace the cell culture medium
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(1000, reservoir['A2'])
        p300.dispense(1000, well)
        p300.mix(3, 1000, well)
        p300.drop_tip()
