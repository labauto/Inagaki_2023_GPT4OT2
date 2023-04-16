from opentrons import protocol_api

metadata = {
    'protocolName': 'Exchange iPS Cell Culture Medium',
    'author': 'Your Name <your_email@example.com>',
    'description': 'iPS cell culture medium exchange using PBS(-) and D-MEM.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    pbs_well = protocol.load_labware('nest_1_reservoir_195ml', 3)['A1']
    dmem_well = protocol.load_labware('nest_1_reservoir_195ml', 4)['A1']

    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Protocol
    for well in plate.wells():
        # Aspirate PBS(-)
        pipette.pick_up_tip()
        pipette.aspirate(300, pbs_well)
        pipette.dispense(300, well)
        pipette.mix(3, 200, well)

        # Remove aspirated PBS(-)
        pipette.aspirate(300, well)
        pipette.dispense(300, pbs_well)
        pipette.drop_tip()

        # Aspirate D-MEM
        pipette.pick_up_tip()
        pipette.aspirate(300, dmem_well)
        pipette.dispense(300, well)
        pipette.mix(3, 200, well)
        pipette.drop_tip()
