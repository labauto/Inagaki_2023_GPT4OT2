from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 1)
    medium_dmem = protocol.load_labware('usascientific_12_reservoir_22ml', 2)
    medium_dmem_high_glucose = protocol.load_labware('usascientific_12_reservoir_22ml', 3)
    supplements = protocol.load_labware('usascientific_12_reservoir_22ml', 4)
    cells = protocol.load_labware('usascientific_12_reservoir_22ml', 5)
    plate_os_minus = protocol.load_labware('nest_96_wellplate_200ul_flat', 6)
    plate_os_plus = protocol.load_labware('nest_96_wellplate_200ul_flat', 7)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    # Transfer medium (DMEM) to 96 well plate (OS-)
    p200.transfer(100, medium_dmem.wells()[0], plate_os_minus.columns()[0], new_tip='always')

    # OS+ condition: Transfer medium (DMEM high glucose) to 96 well plate (OS+)
    p200.transfer(100, medium_dmem_high_glucose.wells()[0], plate_os_plus.columns()[0], new_tip='always')

    # OS+ condition: Add supplements to 96 well plate (OS+)
    p20.transfer(0.1, supplements.wells('A1'), plate_os_plus.columns()[0], mix_after=(3, 20), new_tip='always')   # Dex (Dexamethasone)
    p20.transfer(1, supplements.wells('A2'), plate_os_plus.columns()[0], mix_after=(3, 20), new_tip='always')    # AA (Ascorbic acid)
    p20.transfer(1, supplements.wells('A3'), plate_os_plus.columns()[0], mix_after=(3, 20), new_tip='always')    # BGP (beta-glycerophosphate)

    # Transfer hMSC cells to both 96 well plates
    p200.transfer(100, cells.wells()[0], plate_os_minus.columns()[0], new_tip='always')
    p200.transfer(100, cells.wells()[0], plate_os_plus.columns()[0], new_tip='always')
