from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '1')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '2')
    hmsc_cells = protocol.load_labware('nest_12_reservoir_15ml', '3')
    
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    
    tiprack_20_single = [protocol.load_labware('opentrons_96_tiprack_20ul', slot) for slot in ['6', '7', '8']]
    tiprack_20_multi = [protocol.load_labware('opentrons_96_tiprack_20ul', slot) for slot in ['9', '10', '11']]
    
    # Pipettes
    p20_single = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=tiprack_20_single)
    p20_multi = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=tiprack_20_multi)
    
    # Transfer medium (DMEM) to each well of OS- plate
    dest_os_minus = os_minus_plate.rows()[0][::2]
    p20_multi.transfer(100, medium_dmem.wells()[0], dest_os_minus, new_tip='always')
    
    # Transfer medium (DMEM high glucose) to each well of OS+ plate
    dest_os_plus = os_plus_plate.rows()[0]
    for dest in dest_os_plus:
        p20_single.transfer(100, medium_dmem_high_glucose.wells()[0], dest, new_tip='always')
    
    # Add osteoinduction supplements to OS+ plate
    for dest in dest_os_plus:
        p20_single.transfer(0.1, hmsc_cells.wells_by_name()['A2'], dest, mix_after=(3, 20), new_tip='always')
        p20_single.transfer(1, hmsc_cells.wells_by_name()['A3'], dest, mix_after=(3, 20), new_tip='always')
        p20_single.transfer(1, hmsc_cells.wells_by_name()['A4'], dest, mix_after=(3, 20), new_tip='always')
    
    # Transfer hMSC cells to each well of OS- plates
    p20_multi.transfer(100, hmsc_cells.wells()[0], dest_os_minus, new_tip='always')
    
    # Transfer hMSC cells to each well of OS+ plates
    for dest in dest_os_plus:
        p20_single.transfer(100, hmsc_cells.wells()[0], dest, new_tip='always')
