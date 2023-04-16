from opentrons import protocol_api

metadata = {'apiLevel': "2.11"}


def run(protocol: protocol_api.ProtocolContext):

    # Define labware
    tiprack_10 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    wellplate_6 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    wellplate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    wellplate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', 4)
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 5)

    # Define pipettes
    pipette = protocol.load_instrument("p10_single_gen2", "right", tip_racks=[tiprack_10])

    # Define medium bottles and supplements
    dmem = tuberack.wells_by_name()["A1"]
    dmem_high_glucose = tuberack.wells_by_name()["B1"]
    dex = tuberack.wells_by_name()["C1"]
    aa = tuberack.wells_by_name()["D1"]
    bgp = tuberack.wells_by_name()["E1"]
    hmsc_cells = wellplate_6.wells()[0]

    # Transfer medium (DMEM) to OS(-) wells
    for well in wellplate_96_os_minus.wells():
        pipette.pick_up_tip()
        pipette.aspirate(100, dmem)
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Transfer medium (DMEM high glucose) to OS(+) wells
    for well in wellplate_96_os_plus.wells():
        pipette.pick_up_tip()
        pipette.aspirate(100, dmem_high_glucose)
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Add supplements to OS(+) wells
    for well in wellplate_96_os_plus.wells():
        # Add Dex
        pipette.pick_up_tip()
        pipette.aspirate(0.1, dex)
        pipette.dispense(0.1, well)
        pipette.blow_out()
        pipette.drop_tip()

        # Add AA
        pipette.pick_up_tip()
        pipette.aspirate(1, aa)
        pipette.dispense(1, well)
        pipette.blow_out()
        pipette.drop_tip()

        # Add BGP
        pipette.pick_up_tip()
        pipette.aspirate(1, bgp)
        pipette.dispense(1, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Transfer hMSC cells to OS(-) wells
    for well in wellplate_96_os_minus.wells():
        pipette.pick_up_tip()
        pipette.aspirate(100, hmsc_cells)
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.drop_tip()

    # Transfer hMSC cells to OS(+) wells
    for well in wellplate_96_os_plus.wells():
        pipette.pick_up_tip()
        pipette.aspirate(100, hmsc_cells)
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.drop_tip()
