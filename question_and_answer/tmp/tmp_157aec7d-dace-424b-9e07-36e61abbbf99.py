from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Your Name',
    'apiLevel': '2.11'  # Must specify the target API level.
}

def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    p300_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    p1000_tip_rack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    pbs_tube = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '4')
    dmem_tube = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '5')

    # Define pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[p300_tip_rack])
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[p1000_tip_rack])

    # Protocol steps
    # 1. Aspirate PBS(-) from the first tube
    p1000.pick_up_tip()
    p1000.aspirate(1000, pbs_tube.wells()[0])

    # 2. Dispense PBS(-) to each well of the 6-well plate
    for well in plate_6_well.wells():
        p1000.dispense(166.66, well)  # Dispense an equal volume to each well
        p1000.blow_out(well.top())

    p1000.drop_tip()

    # 3. Aspirate the cell culture medium from each well using p300
    for well in plate_6_well.wells():
        p300.pick_up_tip()
        p300.aspirate(250, well)
        p300.dispense(250, pbs_tube.wells()[0])  # Dispense back in the same PBS(-) tube
        p300.blow_out(pbs_tube.wells()[0].top())
        p300.drop_tip()

    # 4. Aspirate D-MEM from the first tube
    p1000.pick_up_tip()
    p1000.aspirate(1000, dmem_tube.wells()[0])

    # 5. Dispense D-MEM to each well of the 6-well plate
    for well in plate_6_well.wells():
        p1000.dispense(166.66, well)  # Dispense an equal volume to each well
        p1000.blow_out(well.top())

    p1000.drop_tip()
