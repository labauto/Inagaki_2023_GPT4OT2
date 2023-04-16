from opentrons import protocol_api

metadata = {
    'protocolName': 'Lysosome Immunostaining',
    'author': 'Your Name',
    'description': 'Automated immunostaining of hMSC cells to visualize lysosomes.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    reagent_rack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '2')
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Reagents
    primary_antibody_dilution = reagent_rack.wells_by_name()['A1']
    secondary_antibody_dilution = reagent_rack.wells_by_name()['A2']

    # Protocol
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(500, primary_antibody_dilution, well, new_tip='never')
        p1000.mix(5, 500, well)
        p1000.blow_out()
        p1000.return_tip()

        p1000.pick_up_tip()
        p1000.transfer(500, secondary_antibody_dilution, well, new_tip='never')
        p1000.mix(5, 500, well)
        p1000.blow_out()
        p1000.return_tip()
