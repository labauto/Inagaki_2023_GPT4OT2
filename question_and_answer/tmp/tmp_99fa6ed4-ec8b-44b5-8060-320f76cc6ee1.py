from opentrons import protocol_api

metadata = {
    'apiLevel': '2.8',
    'protocolName': 'hMSC_spheroids_experiment',
    'author': 'Assistant',
    'description': 'Automating hMSC spheroids experiment',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    hMSC_source_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    os_minus_dest_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    os_plus_dest_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 4)
    reagent_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips300])

    dmem_medium = hMSC_source_plate.wells()[0]           # Well A1 of 6-well plate
    dmem_high_glucose_medium = hMSC_source_plate.wells()[1] # Well B1 of 6-well plate
    hMSC_cells = hMSC_source_plate.wells()[2]            # Well C1 of 6-well plate
    dex = reagent_plate.wells()[0]                       # Well A1 of 96-well plate
    aa = reagent_plate.wells()[1]                        # Well B1 of 96-well plate
    bgp = reagent_plate.wells()[2]                       # Well C1 of 96-well plate

    # Transfer DMEM medium to OS(-) wells
    for well in os_minus_dest_plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, dmem_medium, well, new_tip='never')
        p300.drop_tip()

    # Transfer DMEM high glucose medium to OS(+) wells
    for well in os_plus_dest_plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, dmem_high_glucose_medium, well, new_tip='never')
        p300.drop_tip()

    # Add Dex, AA, and BGP to OS(+) wells
    for well in os_plus_dest_plate.wells():
        p300.pick_up_tip()
        p300.transfer(0.1, dex, well, mix_after=(3, 50), new_tip='never')
        p300.transfer(1, aa, well, mix_after=(3, 50), new_tip='never')
        p300.transfer(1, bgp, well, mix_after=(3, 50), new_tip='never')
        p300.drop_tip()

    # Transfer hMSC cells to OS(-) wells
    for well in os_minus_dest_plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, hMSC_cells, well, new_tip='never')
        p300.drop_tip()

    # Transfer hMSC cells to OS(+) wells
    for well in os_plus_dest_plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, hMSC_cells, well, new_tip='never')
        p300.drop_tip()
