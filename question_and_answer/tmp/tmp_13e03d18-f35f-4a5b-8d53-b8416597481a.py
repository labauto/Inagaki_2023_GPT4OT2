from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Lysosome Visualization',
    'author': 'Assistant',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reagent_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
    waste_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '4')

    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Reagents
    lysosome_reagent = reagent_tube.wells_by_name()['A1']
    waste_container = waste_tube.wells_by_name()['A1']

    # Protocol
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, lysosome_reagent)
        p300.dispense(200, well)
        p300.mix(5, 200, well)
        p300.blow_out(well.top())
        p300.touch_tip(waste_container)
        p300.drop_tip()

    protocol.comment("Protocol complete.")
