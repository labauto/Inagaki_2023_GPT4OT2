from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    dmem_medium = protocol.load_labware('nest_1_reservoir_195ml', 1)
    dmem_high_glucose_medium = protocol.load_labware('nest_1_reservoir_195ml', 2)
    dex = protocol.load_labware('nest_1_reservoir_195ml', 3)
    aa = protocol.load_labware('nest_1_reservoir_195ml', 4)
    bgp = protocol.load_labware('nest_1_reservoir_195ml', 5)
    hMSC_cells = protocol.load_labware('nest_1_reservoir_195ml', 6)

    plate_os_negative = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 7)
    plate_os_positive = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 8)

    tiprack_300 = [protocol.load_labware('opentrons_96_tiprack_300ul', slot) for slot in [9, 10, 11]]

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tiprack_300)

    # Transfer 100 µl of medium (DMEM) to OS- plate
    for well in plate_os_negative.wells():
        p300.pick_up_tip()
        p300.aspirate(100, dmem_medium['A1'])
        p300.dispense(100, well)
        p300.drop_tip()

    # Transfer 100 µl of medium (DMEM high glucose) to OS+ plate
    for well in plate_os_positive.wells():
        p300.pick_up_tip()
        p300.aspirate(100, dmem_high_glucose_medium['A1'])
        p300.dispense(100, well)
        p300.drop_tip()

    # Add 0.1 µl of Dex, 1 µl of AA, 1 µl of BGP to OS+ plate
    for well in plate_os_positive.wells():
        p300.pick_up_tip()

        p300.aspirate(0.1, dex['A1'])
        p300.dispense(0.1, well)

        p300.aspirate(1, aa['A1'])
        p300.dispense(1, well)

        p300.aspirate(1, bgp['A1'])
        p300.dispense(1, well)

        p300.drop_tip()

    # Transfer 100 µl of hMSC cells to OS- and OS+ plates
    for os_minus_well, os_plus_well in zip(plate_os_negative.wells(), plate_os_positive.wells()):
        p300.pick_up_tip()

        p300.aspirate(100, hMSC_cells['A1'])
        p300.dispense(100, os_minus_well)

        p300.aspirate(100, hMSC_cells['A1'])
        p300.dispense(100, os_plus_well)

        p300.drop_tip()

