from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Formation',
    'author': 'Your Name',
    'description': 'hMSC spheroids formation in 96-well plates with and without osteoinduction supplements',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack])

    # Reagents
    dmem = reagent_reservoir.wells_by_name()['A1']
    dmem_high_glucose = reagent_reservoir.wells_by_name()['A2']
    dex = reagent_reservoir.wells_by_name()['A3']
    aa = reagent_reservoir.wells_by_name()['A4']
    bgp = reagent_reservoir.wells_by_name()['A5']
    hmsc_cells = reagent_reservoir.wells_by_name()["A6"]

    # Transfer 100 µL of DMEM to each well of the 96-well plate (OS-)
    for well in os_minus_plate.wells():
        p300.transfer(100, dmem, well)

    # Transfer 100 µL of DMEM high glucose to each well of the 96-well plate (OS+)
    for well in os_plus_plate.wells():
        p300.transfer(100, dmem_high_glucose, well)

    # Add supplements to each well of the 96-well plate (OS+)
    for well in os_plus_plate.wells():
        p300.transfer(0.1, dex, well, mix_after=(3, 25))
        p300.transfer(1, aa, well, mix_after=(3, 25))
        p300.transfer(1, bgp, well, mix_after=(3, 25))

    # Transfer 100 µL of hMSC cells to each well of the 96-well plate (OS-)
    for well in os_minus_plate.wells():
        p300.transfer(100, hmsc_cells, well, mix_after=(3, 25))

    # Transfer 100 µL of hMSC cells to each well of the 96-well plate (OS+)
    for well in os_plus_plate.wells():
        p300.transfer(100, hmsc_cells, well, mix_after=(3, 25))

    # End
