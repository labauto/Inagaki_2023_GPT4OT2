from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Immunostaining for Lysosomes in hMSC Cells',
    'author': 'Your Name',
    'description': 'Protocol to prepare immunostained hMSC cells for lysosome visualization',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack])

    # Reagents
    media = reagent_reservoir.wells_by_name()['A1']
    fixative = reagent_reservoir.wells_by_name()['A2']
    wash_buffer = reagent_reservoir.wells_by_name()['A3']
    primary_antibody = reagent_reservoir.wells_by_name()['A4']
    secondary_antibody = reagent_reservoir.wells_by_name()['A5']

    # Protocol
    # Remove media from the wells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(300, well)
        p300.dispense(300, media.bottom())
        p300.drop_tip()

    # Add fixative to the wells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(300, fixative)
        p300.dispense(300, well)
        p300.drop_tip()

    protocol.delay(minutes=15)  # Fixation time

    # Wash the wells with wash buffer
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(300, well)
        p300.dispense(300, wash_buffer.bottom())
        p300.drop_tip()

    # Add primary antibody to the wells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, primary_antibody)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.delay(hours=1)  # Incubation time for primary antibody

    # Add secondary antibody to the wells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, secondary_antibody)
        p300.dispense(200, well)
        p300.drop_tip()

    protocol.delay(hours=1)  # Incubation time for secondary antibody

    # Final wash with wash buffer
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(300, well)
        p300.dispense(300, wash_buffer.bottom())
        p300.drop_tip()

    protocol.comment("Protocol complete. Cells are prepared for lysosome visualization.")
