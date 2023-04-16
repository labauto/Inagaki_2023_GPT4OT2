from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Your Name',
    'description': 'Automated lab experiment with Opentrons robot',
    'apiLevel': '2.11',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware setup
    reagent_plate = protocol.load_labware('nest_12_reservoir_15ml', '1')
    os_minus_medium = reagent_plate.wells()[0]
    os_plus_medium = reagent_plate.wells()[1]
    dex = reagent_plate.wells()[2]
    aa = reagent_plate.wells()[3]
    bgp = reagent_plate.wells()[4]
    hmsc_cells = reagent_plate.wells()[5]
    os_minus_plate = protocol.load_labware('biorad_96_wellplate_200µl_pcr', '2')
    os_plus_plate = protocol.load_labware('biorad_96_wellplate_200µl_pcr', '3')

    # Pipette setup
    p200 = protocol.load_instrument('p300_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_200µl', '5')])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_20µl', '4')])

    # Transferring medium to 96 well plates
    p200.distribute(100, os_minus_medium, os_minus_plate.wells())
    p200.distribute(100, os_plus_medium, os_plus_plate.wells())

    # Adding supplements to OS+ plate
    p20.transfer(0.1, dex, os_plus_plate.wells(), mix_before=(3, 20), mix_after=(3, 20))
    p200.transfer(1, aa, os_plus_plate.wells(), mix_before=(3, 100), mix_after=(3, 100))
    p200.transfer(1, bgp, os_plus_plate.wells(), mix_before=(3, 100), mix_after=(3, 100))

    # Transferring hMSC cells to 96 well plates
    p200.distribute(100, hmsc_cells, os_minus_plate.wells())
    p200.distribute(100, hmsc_cells, os_plus_plate.wells())

    # End of the protocol
    protocol.comment('Experiment completed.')
