from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and Cytotoxicity Measurement',
    'author': '<Your Name>',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin Seeding A549 cells and addition of various concentrations of Thapsigargin on the second day after the cells have adhered to the 96 well TC plate.',
    'apiLevel': '2.7'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    # Define the labware and pipettes
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '9')
    tube_rack_6x15ml = protocol.load_labware('opentrons_6_tuberack_15ml', '7')
    countess_slide = protocol.load_labware('thermo_fisher_countess_slide_4pk', '5')
    mix_reagent_tubes = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_white', '4')
    incubation_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    heater_shaker = protocol.load_module('heaterplate', '2')
    trash = protocol.fixed_trash
    
    # Define the pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_200ul])
    
    # Define the functions
    def seed_cells():
        cell_volume = 6  # in microliters
        cell_count_per_well = 8000
        
        wells_to_seed = plate.wells()[:12]  # Seed cells in rows A-D
        
        # Calculate the cell volume
        cells_per_ml = cell_count/countess_count*1000
        cells_to_add = cells_per_ml*cell_volume
        medium_to_add = cell_volume - cells_to_add
        cells_per_ul = cells_per_ml/1000
        
        for well in wells_to_seed:
            p300.pick_up_tip()
            p300.dispense(60, well)  # Add 60 µl of Ham's F12K medium
            p300.air_gap(20)
            p300.drop_tip()
            
            p20.pick_up_tip()
            p20.aspirate(cells_to_add, countess_well)  # Pickup the desired number of cells
            p20.dispense(cells_to_add, well)  # Dispense cells into the well
            p20.aspirate(medium_to_add, medium_reservoir)  # Pick up the medium
            p20.dispense(medium_to_add, well)  # Dispense the medium into the well
            p20.blow_out()

    def prepare_drugs():
        # Define the positions of initial drug stocks in the tube rack as well as their concentrations
        initial_concentrations = {
            'A1': 1000,  # 1 mM
            'A2': 100,  # 100 µM
            'A3': 10,  # 10 µM
            'A4': 1,  # 1 µM
            'A5': 0.1,  # 100 nM
            'A6': 0.05,  # 50 nM
            'B1': 0.01  # 10 nM
        }
        
        # Define the concentrations for 4X working concentrations
        four_x_concentrations = {
            'C1': 1.56,
            'C2': 3.12,
            'C3': 6.24,
            'C4': 12.52,
            'C5': 25,
            'C6': 50,
            'D1': 100,
            'D2': 200,
            'D3': 400,
            'D4': 800,
            'D5': 1600,
            'D6': 2000
        }
        
        # Add the diluent to C and D tubes
        diluent_volume = 300
        for i in range(1, 7):
            tube_c = tube_rack_6x15ml['C' + str(i)]
            tube_d = tube_rack_6x15ml['D' + str(i)]
            p300.pick_up_tip()
            p300.transfer(diluent_volume, medium_reservoir, tube_c, new_tip='never')
            p300.transfer(diluent_volume, medium_reservoir, tube_d, new_tip='never')
            p300.drop_tip()
        
        # Prepare the 4X concentrations
        for i, (position, concentration) in enumerate(four_x_concentrations.items()):
            source_tube = tube_rack_6x15ml['A' + str(i+1)]
            dest_tube_c = tube_rack_6x15ml['C' + str(i+1)]
            dest_tube_d = tube_rack_6x15ml['D' + str(i+1)]
            mix_tube = mix_reagent_tubes.wells()[i]
            mix_volume = 200
            
            # Add the stock drug solution to the corresponding tube
            p20.pick_up_tip()
            p20.transfer(35, source_tube, mix_tube, new_tip='never')
            p20.mix(3, 20, mix_tube)
            p20.drop_tip()
            
            # Prepare 4X dilutions
            initial_concentration = initial_concentrations[position]
            multiplier = initial_concentration/concentration
            volume_to_transfer = 4/multiplier*diluent_volume
            p300.pick_up_tip()
            p300.transfer(volume_to_transfer, medium_reservoir, mix_tube, new_tip='never')
            p300.transfer(volume_to_transfer, mix_tube, dest_tube_c, mix_after=(3, 150), new_tip='never')
            p300.transfer(volume_to_transfer, mix_tube, dest_tube_d, mix_after=(3, 150), new_tip='never')
            p300.drop_tip()
            
            # Prepare 2X dilutions and add them to the plate
            for j in range(1, 5):
                well = plate.rows()[j][i]
                volume_to_add = 200  # µl
                destination = well.bottom(3)
                source = dest_tube_c if j != 4 else dest_tube_d
                p300.pick_up_tip()
                p300.transfer(volume_to_add/2, source, mix_reagent_tubes.wells()[i*2], new_tip='never')
                p300.transfer(volume_to_add/2, source, mix_reagent_tubes.wells()[i*2+1], mix_after=(3, 150), new_tip='never')
                p300.transfer(volume_to_add, mix_reagent_tubes.wells()[i*2], destination, new_tip='never')
                p300.drop_tip()
    
    def viability_measurement():
        # Add CellTox Green reagent to the plate
        for i in range(1, 6):
            for j in range(1, 9):
                well = plate.rows()[i][j]
                mix_tube = mix_reagent_tubes.wells()[i*8-7+(j-1)//2]
                volume_to_add = 15  # µl
                destination = well.bottom(3)
                p20.pick_up_tip()
                p20.transfer(volume_to_add, mix_tube, destination, new_tip='never')
                p20.drop_tip()
        
        # Orbital shake the plate
        heater_shaker.plate = incubation_plate
        heater_shaker.set_temperature(25)
        heater_shaker.set_shaking_amplitude(1.0)
        heater_shaker.set_shaking_duration(minutes=2)
        heater_shaker.start_shaking()
        
        # Wait for incubation period
        protocol.delay(minutes=15)
        heater_shaker.stop_shaking()
        
        # Read fluorescence using the Biotek microplate reader
        # Implement the code here to communicate with the Biotek microplate reader to measure fluorescence values
        
    def cytotoxicity_measurement():
        # Add Cell Titer Glo 2.0 reagent to the plate
        for i in range(1, 6):
            for j in range(1, 9):
                well = plate.rows()[i][j]
                mix_tube = mix_reagent_tubes.wells()[i*8-7+(j-1)//2+24]
                volume_to_add = 80  # µl
                destination = well.bottom(3)
                p300.pick_up_tip()
                p300.transfer(volume_to_add, mix_tube, destination, new_tip='never')
                p300.drop_tip()
        
        # Orbital shake the plate
        heater_shaker.plate = incubation_plate
        heater_shaker.set_temperature(25)
        heater_shaker.set_shaking_amplitude(1.0)
        heater_shaker.set_shaking_duration(minutes=2)
        heater_shaker.start_shaking()
        
        # Wait for incubation period
        protocol.delay(minutes=10)
        heater_shaker.stop_shaking()
        
        # Read luminescence using the Biotek microplate reader
        # Implement the code here to communicate with the Biotek microplate reader to measure luminescence values
        
    # Starting code execution
    # Clean the inside of the robot with 70 % ethanol and turn on the HEPA filter
    # Implement the code here to clean the robot and turn on the HEPA filter
    
    # Take a cell count
    countess_well = countess_slide.wells()[0]
    p300.pick_up_tip()
    p300.aspirate(10, countess_well)  # Aspirate some liquid to ensure proper volume detection
    cell_count = countess.get_cell_count()
    countess_count = countess.last_result.count
    p300.drop_tip()
    
    # Seed cells
    medium_reservoir = tube_rack_6x15ml['A7']
    seed_cells()
    
    # Prepare drugs
    prepare_drugs()
    
    # Perform viability measurement
    viability_measurement()
    
    # Perform cytotoxicity measurement
    cytotoxicity_measurement()
