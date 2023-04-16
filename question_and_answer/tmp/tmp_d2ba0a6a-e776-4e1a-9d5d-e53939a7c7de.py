from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS Medium Exchange',
    'author': 'Your Name',
    'description': 'Automated medium exchange for iPS cells using Opentrons',
    'apiLevel': '2.2'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')

    # Load pipettes
    p300 = protocol.load_instrument('p300_single', 'left')
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 50

    # Define the positions of the wells in the plate
    wells = [well for row in plate.rows() for well in row]

    # Define the positions of the solutions in the reservoir
    pbs = reservoir['A1']
    medium = reservoir['A2']

    # Perform the medium exchange
    for well in wells:
        # Aspirate old medium
        p300.pick_up_tip()
        p300.aspirate(200, well.bottom(1.5))
        p300.drop_tip()

        # Wash with PBS
        p300.pick_up_tip()
        p300.aspirate(250, pbs)
        p300.dispense(250, well.bottom(1.5))
        p300.mix(5, 200, well.bottom(1.5))
        p300.drop_tip()

        # Add new medium
        p300.pick_up_tip()
        p300.aspirate(250, medium)
        p300.dispense(250, well.bottom(1.5))
        p300.mix(5, 200, well.bottom(1.5))
        p300.blow_out()
        p300.drop_tip()
