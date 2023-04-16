from opentrons import simulate, protocol_api

metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    p1000rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[p1000rack])

    # Set up tip tracking
    p1000.starting_tip = p1000.tip_racks[0].rows()[0][0]
    tip_count = len(p1000.tip_racks) * len(p1000.tip_racks[0]._wells)

    # Perform experiment
    p1000.pick_up_tip()
    while tip_count > 0:
        for well in plate.rows()[0]:
            p1000.aspirate(1000, p1000rack['A1'])
            p1000.dispense(1000, well)
            p1000.aspirate(1000, well)
            p1000.dispense(1000, p1000rack['A1'])
            p1000.mix(5, 200, well)
        p1000.return_tip()
        tip_count -= 1

simulation = simulate.get_protocol_api('2.0')
simulation.run(run) # Remove this line if you want to transfer the protocol to the robot correctly.```


:*************************


