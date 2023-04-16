from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    dmem_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    hg_dmem_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)
    dex_aa_bgp_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 4)
    cell_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 5)
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 7)

    # Load pipette
    pipette = protocol.load_instrument("p10_single", "right", tip_racks=[tiprack_10])

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    pipette.pick_up_tip()
    for well in os_minus_plate.wells():
        pipette.transfer(100, dmem_6_well['A1'], well, new_tip='never')
    pipette.drop_tip()

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    pipette.pick_up_tip()
    for well in os_plus_plate.wells():
        pipette.transfer(100, hg_dmem_6_well['A1'], well, new_tip='never')
    pipette.drop_tip()

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    pipette.pick_up_tip()
    for well in os_plus_plate.wells():
        pipette.transfer(0.1, dex_aa_bgp_6_well['A1'], well, new_tip='never')
    pipette.drop_tip()

    pipette.pick_up_tip()
    for well in os_plus_plate.wells():
        pipette.transfer(1, dex_aa_bgp_6_well['A2'], well, new_tip='never')
    pipette.drop_tip()

    pipette.pick_up_tip()
    for well in os_plus_plate.wells():
        pipette.transfer(1, dex_aa_bgp_6_well['A3'], well, new_tip='never')
    pipette.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    pipette.pick_up_tip()
    for well in os_minus_plate.wells():
        pipette.transfer(100, cell_6_well['A1'], well, new_tip='never')
    pipette.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    pipette.pick_up_tip()
    for well in os_plus_plate.wells():
        pipette.transfer(100, cell_6_well['A1'], well, new_tip='never')
    pipette.drop_tip()

    return
