import opentrons
from opentrons import protocol_api, types

metadata = {
    'protocolName': 'A549 Cell Viability and Cytotoxicity Measurement',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of A549 cells',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Step 1 (Cell count and preparation) should be done manually, as it involves human intervention.
    
    # Step 2 (Set up labware)
    tip_rack1 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tip_rack2 = protocol.load_labware('opentrons_96_tiprack_200ul', 4)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 6)

    heater_shaker = protocol.load_module('tempdeck', 1)
    well_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1, share=True)
    plate = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')
    
    # Step 3 (Cell seeding) should be done manually, as it involves human intervention.
    
    # Step 4 (Add medium control)
    add_medium_control(protocol, well_plate, tube_rack, tip_rack1)
    
    # Step 5 (Waiting period) should be done manually, as it involves human intervention.
    
    # Steps 6-9 (Prepare drug dilutions and stocks)
    thapsigargin_stocks = [(tube_rack.wells_by_name()[key], conc) for key, conc in [
        ('A1', 1), ('A2', 100), ('A3', 10), ('A4', 1), ('A5', 0.1), ('A6', 0.05), ('B1', 0.01)]]
    working_concentrations = [(reagent_rack.wells_by_name()[key], conc) for key, conc in [
        ('C1', 1.56), ('C2', 3.12), ('C3', 6.24), ('C4', 12.52), ('C5', 25), ('C6', 50),
        ('D1', 100), ('D2', 200), ('D3', 400), ('D4', 800), ('D5', 1600), ('D6', 2000)]]
    prepare_thapsigargin_dilutions(protocol, well_plate, thapsigargin_stocks, working_concentrations, tube_rack, reagent_rack, tip_rack2)
    
    # Steps 10-17 (Perform the experiment)
    perform_experiment(protocol, well_plate, reagent_rack, heater_shaker, tip_rack1, tip_rack2)
    

def add_medium_control(protocol, well_plate, tube_rack, tip_rack1):
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tip_rack1])
    
    # Add medium to wells A5, B5, and C5
    medium_well = tube_rack.wells_by_name()['A5']
    dest_wells = [well_plate.wells_by_name()[key] for key in ['A5', 'B5', 'C5']]

    for well in dest_wells:
        p20.transfer(60, medium_well, well)
        

def prepare_thapsigargin_dilutions(protocol, well_plate, thapsigargin_stocks, working_concentrations, tube_rack, reagent_rack, tip_rack2):
    p200 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack2])

    # Prepare dilutions
    for (stock, stock_conc), (working, working_conc) in zip(thapsigargin_stocks, working_concentrations):
        stock_vol = (4 * working_conc * 100) / stock_conc
        p200.transfer(stock_vol, stock, working, mix_after=(3, 50))
        
    # Fill wells with respective drug concentrations
    # You may need to adjust this code to fit your specific layout
    for i, (well, conc) in enumerate(working_concentrations):
        row = 'ABCDEFGH'[((i * 3) // 12)]
        col = 2 * ((i * 3) % 12) + 1
        
        for j in range(3):
            well_name = row + str(col + j)
            dest_well = well_plate[well_name]
            p200.transfer(60, well, dest_well, mix_after=(3, 50))

            
def perform_experiment(protocol, well_plate, reagent_rack, heater_shaker, tip_rack1, tip_rack2):
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tip_rack1])
    p200 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack2])

    # Step 10 - Add CellTox Green Reagent
    add_CellToxGreen(protocol, p20, well_plate, reagent_rack, "B2")
    
    # Step 11 - Orbital shaking for 2 minutes
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    
    # Steps 12-13 should be done manually, as it involves human intervention.
    
    # Step 14 - Add Cell Titer Glo 2.0 Reagent
    add_CellTiterGlo(protocol, p200, well_plate, reagent_rack, "B1")
    
    # Step 15 - Orbital shaking for 2 minutes
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    
    # Steps 16-17 should be done manually, as it involves human intervention.
    

def add_CellToxGreen(protocol, pipette, well_plate, reagent_rack, reagent_position):
    reagent_well = reagent_rack[reagent_position]

    for well_name in well_plate.wells_by_name():
        dest_well = well_plate[well_name]
        pipette.pick_up_tip()
        pipette.transfer(15, reagent_well, dest_well, new_tip='never', mix_after=(3, 10))
        pipette.drop_tip()
        

def add_CellTiterGlo(protocol, pipette, well_plate, reagent_rack, reagent_position):
    reagent_well = reagent_rack[reagent_position]

    for well_name in well_plate.wells_by_name():
        dest_well = well_plate[well_name]
        pipette.pick_up_tip()
        pipette.transfer(80, reagent_well, dest_well, new_tip='never', mix_after=(3, 40))
        pipette.drop_tip()
        

if __name__ == '__main__':
    from opentrons.simulate import run_protocol
    run_protocol(run)
