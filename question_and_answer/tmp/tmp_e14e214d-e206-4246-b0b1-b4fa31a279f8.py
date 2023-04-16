from opentrons import protocol_api

metadata = {'protocolName': 'A549 Cell Viability and Cytotoxicity Assay',
            'author': 'Your Name <youremail@example.com>',
            'description': 'This protocol automates the A549 Cell Viability and Cytotoxicity Assay using Opentrons robot'}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware definitions
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    snap_tubes = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '6')
    dilution_tubes = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '7')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    
    # Pipettes definition
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])
    
    # Step 1: Count A549 cells using Countess 3 machine
    countess_3 = Countess3()
    countess_3.instrument_resuming(p300)
    cell_count = countess_3.run()
    
    # Step 2: Seeding of A549 cells
    cell_vol = 60 / 1000  # Volume of cells required in each well
    cell_conc = cell_count / (cell_vol * 96)  # Concentration of cells in the suspension
    p300.pick_up_tip()
    for col in plate_96.columns_by_name()['1']:
        p300.aspirate(cell_vol, stripwell['A1'])
        p300.dispense(cell_vol, col)
    p300.drop_tip()
    
    # Step 3: Dispensing cell suspension into snap-capped tubes
    cell_suspension_tube_vol = 225 / 1000  # Volume of cell suspension required in each tube
    for tube in snap_tubes.wells():
        p300.pick_up_tip()
        p300.aspirate(cell_suspension_tube_vol, plate_96.wells()[0])
        p300.dispense(cell_suspension_tube_vol, tube)
        p300.mix(3, 100, tube)
        p300.drop_tip()
    
    # Step 4: Adding medium to the control wells
    p300.pick_up_tip()
    for well in plate_96.rows_by_name()['A'][4:6]:
        p300.aspirate(cell_vol, dilution_tubes.wells()[0])
        p300.dispense(cell_vol, well)
    p300.drop_tip()
    
    # Step 5: Add drug dilutions
    stock_tube = snap_tubes.well('A1')
    for i, conc in enumerate([1, 0.1, 0.01, 0.001, 0.0001, 0.00005, 0.00001]):
        conc_tube = snap_tubes.well(chr(66+i))
        dilution_tube_4x = dilution_tubes.well(chr(67+i))
        dilution_tube_2x = dilution_tubes.well(chr(67+i+6))
        p300.pick_up_tip()
        p300.aspirate(35, stock_tube) # Transfer 35 µL of 1mM stock concentration
        p300.dispense(35, conc_tube)
        p300.mix(3, 50, conc_tube)
        p300.transfer(35, conc_tube, dilution_tube_4x, new_tip='always')
        
        # Add diluent
        p300.aspirate(140, dilution_tubes.wells_by_name()[chr(67+i)])
        p300.dispense(140, dilution_tube_4x)
        # Add thapsigargin
        p300.aspirate(140, snap_tubes.wells_by_name()['A1'])
        p300.dispense(140, dilution_tube_4x)
        p300.mix(3, 150, dilution_tube_4x)
        # Transfer to next adjacent tube
        p300.transfer(140, dilution_tube_4x, dilution_tube_2x, new_tip='always')
        p300.drop_tip()
    
    # Step 9: Add CellTox Green reagent
    p20.pick_up_tip()
    for col in plate_96.columns():
        if col[0] == 4:
            continue  # Skip control wells
        p20.aspirate(15, dilution_tubes.wells_by_name()['B2'])
        p20.dispense(15, col[0])
    p20.drop_tip()

    # Step 10: Use Heater Shaker to shake for 2min at 500rpm
    protocol.comment('Set to Heater Shaker, orbital 2min at 500rpm')
    
    # Step 11: Incubate at room temperature for 15min
    protocol.comment('Incubating at room temperature for 15min')

    # Step 13: Read fluorescence at 485 nm excitation and 520 nm emission
    protocol.comment('Reading fluorescence at 485 nm excitation and 520 nm emission')
    
    # Step 15: Add Cell Titer Glo reagent
    p200.pick_up_tip()
    for row in plate_96.rows():
        if row[0] in ['A', 'D']:  # Skip control wells
            continue
        p200.transfer(80, dilution_tubes.wells_by_name()['B1'], row[0])
    p200.drop_tip()

    # Step 16: Use Heater Shaker to shake for 2min at 500rpm
    protocol.comment('Set to Heater Shaker, orbital 2min at 500rpm')

    # Step 17: Incubate at room temperature for 10min
    protocol.comment('Incubating at room temperature for 10min')

    # Step 18: Read luminescence
    protocol.comment('Reading luminescence')    
