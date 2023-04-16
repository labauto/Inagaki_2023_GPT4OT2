from opentrons import protocol_api

metadata = {'apiLevel': '2.8'}

def run(protocol: protocol_api.ProtocolContext):
    # Load 96 well plate and 6 well plate
    source_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    dest_plate_os_pos = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    dest_plate_os_neg = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    source_6_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Load tips
    tips20 = protocol.load_labware('opentrons_96_tiprack_20ul', '5')

    # Set pipettes
    pipette_20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips20])

    # Transfer DMEM to each well (OS-)
    pipette_20.pick_up_tip()
    for dest_well in dest_plate_os_neg.rows()[0]:
        pipette_20.transfer(100, source_plate.wells_by_name()['A1'], dest_well, new_tip='never')
    pipette_20.drop_tip()

    # Transfer DMEM high glucose to each well (OS+) and add supplements
    pipette_20.pick_up_tip()
    for dest_well in dest_plate_os_pos.rows()[0]:
        pipette_20.transfer(100, source_plate.wells_by_name()['A1'], dest_well, new_tip='never')
        pipette_20.transfer(0.1, source_6_well_plate.wells_by_name()['A1'], dest_well, new_tip='never')
        pipette_20.transfer(1, source_6_well_plate.wells_by_name()['B1'], dest_well, new_tip='never')
        pipette_20.transfer(1, source_6_well_plate.wells_by_name()['C1'], dest_well, new_tip='never')
    pipette_20.drop_tip()

    # Transfer hMSC cells to each well (OS- and OS+)
    pipette_20.pick_up_tip()
    for dest_well_os_neg, dest_well_os_pos in zip(dest_plate_os_neg.rows()[0], dest_plate_os_pos.rows()[0]):
        pipette_20.transfer(100, source_6_well_plate.wells_by_name()['A1'], dest_well_os_neg, new_tip='never')
        pipette_20.transfer(100, source_6_well_plate.wells_by_name()['A2'], dest_well_os_pos, new_tip='never')
    pipette_20.drop_tip()
