from opentrons import protocol_api

metadata = {'apiLevel': '2.7'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tip_rack_slot = 10  # Please set the correct slot for the tip rack
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', tip_rack_slot)

    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    dmem = six_well_plate['A1']
    dmem_high_glucose_medium = six_well_plate['A2']

    # Reagents
    osteo = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '4')
    dex = osteo['A1']
    aa = osteo['A2']
    bgp = osteo['A3']
    hMSC_cells = osteo['B1']

    # 96-well plates
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')

    # Transfers
    for i, well in enumerate(plate_os_minus.wells()):
        p300.pick_up_tip(tiprack.wells()[i])
        p300.transfer(100, dmem, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_os_plus.wells()):
        index_of_tip = i + len(plate_os_minus.wells())
        p300.pick_up_tip(tiprack.wells()[index_of_tip])
        p300.transfer(100, dmem_high_glucose_medium, well, new_tip='never')
        p300.transfer(0.1, dex, well, mix_after=(3, 100), new_tip='never')
        p300.transfer(1, aa, well, mix_after=(3, 100), new_tip='never')
        p300.transfer(1, bgp, well, mix_after=(3, 100), new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_os_minus.wells()):
        index_of_tip = i + 2*len(plate_os_minus.wells())
        p300.pick_up_tip(tiprack.wells()[index_of_tip])
        p300.transfer(100, hMSC_cells, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_os_plus.wells()):
        index_of_tip = i + 3*len(plate_os_minus.wells())
        p300.pick_up_tip(tiprack.wells()[index_of_tip])
        p300.transfer(100, hMSC_cells, well, new_tip='never')
        p300.drop_tip()
