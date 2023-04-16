from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    medium_dmem = protocol.load_labware('nest_1_reservoir_195ml', '2')
    medium_dmem_high_glucose = protocol.load_labware('nest_1_reservoir_195ml', '3')
    supplements_stock = protocol.load_labware('nest_12_reservoir_15ml', '4')
    cell_stock = protocol.load_labware('nest_12_reservoir_15ml', '5')
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '7')
    
    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips])
    
    # Reagents
    dmem = medium_dmem['A1']
    dmem_high_glucose = medium_dmem_high_glucose['A1']
    dex = supplements_stock['A1']
    aa = supplements_stock['A2']
    bgp = supplements_stock['A3']
    cells = cell_stock['A1']
    
    # Helper function for transferring supplements
    def transfer_supplements(target_well):
        p300.transfer(0.1, dex, target_well, mix_after=(3, 10), new_tip='never')
        p300.transfer(1, aa, target_well, mix_after=(3, 10), new_tip='never')
        p300.transfer(1, bgp, target_well, mix_after=(3, 10), new_tip='never')
    
    # Perform the experiment steps
    for i in range(96):
        well_os_minus = plate_os_minus.wells()[i]
        well_os_plus = plate_os_plus.wells()[i]
        
        # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
        p300.transfer(100, dmem, well_os_minus, new_tip='once')
        
        # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
        p300.transfer(100, dmem_high_glucose, well_os_plus, new_tip='once')
        
        # Add supplements to each well of 96 well plate (OS+)
        transfer_supplements(well_os_plus)
        
        # Transfer hMSC cells to each well
        p300.pick_up_tip()
        p300.transfer(100, cells, well_os_minus, new_tip='never')
        p300.transfer(100, cells, well_os_plus, new_tip='never')
        p300.drop_tip()
