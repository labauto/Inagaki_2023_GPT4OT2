from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC Cells Visualization',
    'author': 'Assistant',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes in a 6 well plate.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reagent_tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '2')

    # Tip racks
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '3')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # Reagents
    l_lamp1 = reagent_tube_rack['A1'] # Primary antibody - LAMP1 (Lysosome Marker)
    l_secondary_antibody = reagent_tube_rack['A2'] # Secondary antibody conjugated with a fluorophore
    l_media = reagent_tube_rack['A3'] # Medium to wash and resuspend cells

    # Transfer primary antibody to each well
    for well in plate.wells():
        p20.pick_up_tip()
        p20.aspirate(10, l_lamp1)
        p20.dispense(10, well)
        p20.drop_tip()

    # Transfer secondary antibody to each well
    for well in plate.wells():
        p20.pick_up_tip()
        p20.aspirate(10, l_secondary_antibody)
        p20.dispense(10, well)
        p20.drop_tip()

    # Transfer medium, wash and resuspend cells
    for well in plate.wells():
        p20.pick_up_tip()
        p20.aspirate(20, l_media)
        p20.dispense(20, well)
        p20.mix(5, 10, well) # Mix the cell suspension to help wash and resuspend cells
        p20.drop_tip()

