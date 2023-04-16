Sure, here's an example script:

```
from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Measurement of cell viability and cytotoxicity of A549 cells treated with thapsigargin',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Step 1: Cell Count
    countess = protocol.load_module('countess', '3')
    countess.reset_tipracks()
    countess.load_container('countess-slide', '384-plate-countess')
    countess.open_lid()
    protocol.pause('Clean the Opentrons robot with 70 % ethanol and turn on the HEPA filter \
                    at low fan speed for about an hour before seeding the cells on 96 well plate. \
                    Continue to keep the HEPA filter turned on during the duration of setting up \
                    the robot with the respective labware, dilutions of the drug (thapsigargin) \
                    on Day 2 and addition of the drug on to the 96 well plate.')
    a549 = countess.side_one.wells('A4').count_cells()
    cell_count = a549.count
    protocol.pause(f'Loaded T-75 flask of A549 cells has {cell_count} cells.')

    # Step 2: Cell Seeding
    tc_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    cells_vol = round(0.6 * 100000 / cell_count, 1)
    cells = protocol.transfer(cells_vol, a549, tc_plate.rows()[0], new_tip='always')
    
    # Step 3: Dispensing Cell Suspension in Tubes
    tube_rack = protocol.load_labware('opentrons_24_tuberack_1500ul', '6')
    tubes = tube_rack.rows()[0]
    cell_tubes = [t for t in tubes if t != tubes[0]]
    for tube in cell_tubes:
        protocol.transfer(25, cells, tube, mix_after=(5, 10))

    # Step 4: Adding Control Medium to TC Plate
    control = tc_plate.rows()[4][:3]
    protocol.transfer(60, '10% Ham’s F12K medium', control)

    # Step 5: Dilution and Addition of Thapsigargin on Day 2
    protocol.pause('Please replace tube rack in Slot 6 with 24 tube rack with 1mM thapsigargin \
                    in tube A1 and continue')
    thapsigargin_tubes = tube_rack.rows()[1]
    thapsigargin = thapsigargin_tubes[0]
    first_col = tc_plate.columns()[0]
    control = first_col[:3]

    # Step 6: Adding 1mM Thapsigargin
    protocol.transfer(35, thapsigargin, control)

    # Step 7: Preparing Dilutions of Various Concentrations of Thapsigargin
    thapsigargin_stocks = [
        ('A2', 100), ('A3', 10), ('A4', 1), ('A5', 0.1), ('A6', 0.05), ('B1', 0.01)
    ]
    for tube_pos, dilution in thapsigargin_stocks:
        conc = dilution * 1e-6
        tube = thapsigargin_tubes[tube_pos]
        protocol.transfer(25, f'{conc} M thapsigargin', tube)

    # Step 8: Preparing 4X and 2X Dilutions of Thapsigargin
    diluents = ['10% Ham’s F12K medium', '3.44% DMSO in 10% Ham’s F12K medium']
    thapsigargin_dilutions = [
        ('C', 1.56), ('C', 3.12), ('C', 6.24), ('C', 12.52), ('C', 25.0), ('C', 50.0), 
        ('D', 100.0), ('D', 200.0), ('D', 400.0), ('D', 800.0), ('D', 1600.0), ('D', 2000.0)
    ]
    for row, conc in thapsigargin_dilutions:
        d = 1 if row == 'C' else 2
        dilution = f'{d}X {conc} nM'
        diluent = diluents[d-1]
        source = thapsigargin_tubes[f'{row}1']
        dests = tc_plate.columns()[int(row):int(row)+3]
        for dest in dests:
            protocol.transfer(50, diluent, dest[:3])
            protocol.transfer(50, source, dest[:3], mix_after=(5, 10))
    
    # Step 9: Adding 1X Dilution of Thapsigargin to TC Plate
    channel = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '8')])
    for col in range(3, 9):
        for idx, well in enumerate(tc_plate.columns()[col]):
            dests = [well, dests[idx] for dests in tc_plate.columns()[col+6:col+9]]
            channel.pick_up_tip()
            channel.transfer(60, dests, tc_plate.wells()[col*8+idx], mix_after=(5, 20), new_tip='never')
            channel.drop_tip()

    # Step 10: Adding CellTox Green Reagent to TC Plate
    ctg = protocol.load_labware('celltiter_glo', '2')
    ctg_tube = ctg.wells_by_name()['B2']
    ctg_dests = tc_plate.wells()[:24] + tc_plate.wells()[33:57]
    channel = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_20ul', '9')])
    for dest in ctg_dests:
        channel.pick_up_tip()
        channel.transfer(15, ctg_tube, dest, new_tip='never')
        channel.drop_tip()

    # Step 11: Orbital Shaking for 2 Minutes at 500 RPM
    for idx in range(0, 8):
        tc_plate.wells_by_name()[f'{chr(idx+65)}1'].set_temperature(25)
    protocol.pause('Place the plate on the heater shaker, and start shaking for 2 minutes at 500 rpm.')
    for idx in range(0, 8):
        tc_plate.wells_by_name()[f'{chr(idx+65)}1'].set_temperature(4)

    # Step 12: Incubate Plate at Room Temperature for 15 Minutes
    protocol.pause('Remove the plate from the heater shaker and incubate at room temperature for 15 minutes.')

    # Step 13: Read Fluorescence at 485 nm Excitation and 520 nm Emission
    reader = protocol.load_module('biotek_elx808', '7')
    reader.connect()
    reader.set_wavelengths(485, 520)
    protocol.pause('Place the plate back on the heater shaker and start with additions for the cell viability assay. \
                    After the addition of the reagent, set the heater shaker to orbital shaking at 500 rpm for \
                    two minutes. Incubate at room temperature for 10 minutes. Remove the plate from heater shaker \
                    after incubation and read the plate for luminescence using the Biotek microplate reader.')

    # Step 14: Adding Cell Titer Glo 2 Reagent to TC Plate
    ctg_tube = ctg.wells_by_name()['B1']
    for dest in ctg_dests:
        channel.pick_up_tip()
        channel.transfer(80, ctg_tube, dest, new_tip='never')
        channel.drop_tip()

    # Step 15: Orbital Shaking for 2 Minutes at 500 RPM, Followed by 10 Minute Incubation at RT
    for idx in range(0, 8):
        tc_plate.wells_by_name()[f'{chr(idx+65)}1'].set_temperature(25)
    protocol.pause('Place the plate on the heater shaker, and start shaking for 2 minutes at 500 rpm. \
                   Incubate at room temperature for 10 minutes.')
    for idx in range(0, 8):
        tc_plate.wells_by_name()[f'{chr(idx+65)}1'].set_temperature(4)

    # Step 16: Read Luminescence on a Microplate Reader
    reader.set_wavelengths(600, 650)
    protocol.pause('Remove the plate from the reader and dispose of it properly.')
``` 

Please note that this is an example script that may need to be modified to fit specific lab equipment and reagents. Check the script carefully before running the experiment.


:*************************


