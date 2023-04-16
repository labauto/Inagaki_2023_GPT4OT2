from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Automate Laboratory Experiment',
    'author': 'Assistant',
    'description': 'Automate laboratory experiment using the Opentrons machine'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labwares
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Reagents
    pbs = tuberack.wells('A1')
    trypsin = tuberack.wells('A2')
    dmem = tuberack.wells('A3')

    # Protocol Steps

    # Step 1: Wash the 6 well plate with PBS(-)
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs)
        for _ in range(5):
            p1000.dispense(800, well).aspirate(800, well)
        p1000.dispense(1000, well)
        p1000.blow_out()
        p1000.drop_tip()

    # Step 2: Add trypsin solution (0.25%) to the cell culture dish
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
        p1000.blow_out()
        p1000.drop_tip()

    # Waiting for 5 minutes (incubation period)
    protocol.delay(minutes=5)

    # Step 3: Add cell culture medium (DMEM) to the 6 well plate
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
        p1000.blow_out()
        p1000.drop_tip()

    # Step 4: Finish the experiment (Done)

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.11')
    run(protocol)
