from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    p300_tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    p300_tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    p50_tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 4)
    reagents = protocol.load_labware('usascientific_12_reservoir_22ml', 1)
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[p300_tiprack_1, p300_tiprack_2])
    p50 = protocol.load_instrument('p50_single_gen2', 'right', tip_racks=[p50_tiprack])

    # Reagents
    medium_dmem = reagents.wells_by_name()['A1']
    medium_dmem_high = reagents.wells_by_name()['A2']
    dex = reagents.wells_by_name()['A3']
    aa = reagents.wells_by_name()['A4']
    bgp = reagents.wells_by_name()['A5']
    hmsc_cells = reagents.wells_by_name()['A6']

    # Protocol
    for well in os_minus_plate.wells():
        p50.pick_up_tip()
        p50.transfer(100, medium_dmem, well, new_tip='never')
        p50.transfer(100, hmsc_cells, well, mix_after=(3, 50), new_tip='never')
        p50.drop_tip()

    for well in os_plus_plate.wells():
        p50.pick_up_tip()
        p50.transfer(100, medium_dmem_high, well, new_tip='never')
        p300.pick_up_tip()
        p300.transfer(0.1, dex, well, mix_after=(3, 150), new_tip='never')
        p300.transfer(1, aa, well, mix_after=(3, 150), new_tip='never')
        p300.transfer(1, bgp, well, mix_after=(3, 150), new_tip='never')
        p300.drop_tip()
        p50.transfer(100, hmsc_cells, well, mix_after=(3, 50), new_tip='never')
        p50.drop_tip()
