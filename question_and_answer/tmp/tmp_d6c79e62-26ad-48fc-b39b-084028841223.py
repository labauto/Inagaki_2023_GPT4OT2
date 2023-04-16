from opentrons import protocol_api

metadata = {'apiLevel': '2.7'}

def run(protocol:protocol_api.ProtocolContext):
    
    # Labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    falcon_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    tube_rack15 = protocol.load_labware('opentrons_15_tuberack_1500ul', 6)
    
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])
    
    # Slots
    stock_tubes = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    vials_4X = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    
    # Functions to make solution
    def create_stock_initial():
        for index, well in enumerate(stock_tubes):
            source_slot = 7
            dest_slot = 6
            p300.pick_up_tip()
            p300.aspirate(100, falcon_rack.wells_by_name()[well])
            p300.dispense(100, tube_rack15.wells_by_name()[stock_tubes[index]])
            p300.mix(3, 100, tube_rack15.wells_by_name()[stock_tubes[index]])
            p300.drop_tip()
    
    
    def create_4x_solution():
        for index, well in enumerate(vials_4X):
            source_slot = 6
            dest_slot = 7
            p300.pick_up_tip()
            
            if index > 0:  
                to_aspirate = (100 - (100 * index))
            else:
                to_aspirate = 100
                
            p300.aspirate(to_aspirate, tube_rack15.wells_by_name()[well])
            p300.dispense(to_aspirate,  tube_rack15.wells_by_name()[vials_4X[index]])
            p300.mix(3, to_aspirate, tube_rack15.wells_by_name()[vials_4X[index]])
            p300.drop_tip()
    
    
    def add_to_plate(wells):
        for index, dest_well in enumerate(wells):
            final_well = tube_rack15.wells_by_name()[vials_4X[index]]
            p300.pick_up_tip()
            p300.aspirate(200 - (200 * index), final_well)
            p300.dispense(200 - (200 * index), plate_96.wells_by_name[dest_well])
            p300.drop_tip()
            
    # Main
    create_stock_initial()
    create_4x_solution()
  
    wells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'A5', 'B5', 'C5']
    wells += ['D4', 'E4', 'F4', 'D3', 'E3', 'F3', 'D2', 'E2', 'F2']
    add_to_plate(wells)

    # Shake and read
    protocol.comment('Start orbital shaking and reading')

