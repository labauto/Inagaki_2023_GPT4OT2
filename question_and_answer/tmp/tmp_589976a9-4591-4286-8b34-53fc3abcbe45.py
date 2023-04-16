from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and cytotoxicity assay of A549 cells with Thapsigargin',
    'author': 'Your Name <your.email@example.com>',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '1')

    pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tiprack_20ul])

    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')

    tube_rack_6x15ml = protocol.load_labware('opentrons_6_tuberack_15ml', '7')

    medium_tube = tube_rack_6x15ml['A2']
    control_tube = tube_rack_6x15ml['A3']
    drug_tube = tube_rack_6x15ml['A1']
    
    # Step 1: Seed the cells and incubate overnight
    add_cell_to_well(pipette, plate_96_well, medium_tube, 8, (0, 0))
    add_cell_to_well(pipette, plate_96_well, medium_tube, 8, (0, 1))
    # ... continue seeding cells in the rest of the wells

    # Step 2: Add negative control
    add_medium_to_well(pipette, plate_96_well, medium_tube, (4, 0), (6, 0))

    # Step 3: Prepare drug dilution
    # ... add various concentrations of thapsigargin to tube_rack_6x15ml

    # Step 4: Prepare 2X drug dilution
    # ... add 2X drug concentration to the 96-well plate

    # Step 5: Incubate cells with drug
    # ... incubate at 37°C for 72 hours

    # Step 6: Add CellTox Green reagent
    # ... read fluorescence at 485 nm excitation and 520 nm emission

    # Step 7: Add Cell Titer Glo 2.0 reagent
    # ... read the plate for luminescence

def add_cell_to_well(pipette, plate, source, vol, well):
    pipette.pick_up_tip()
    pipette.aspirate(vol, source)
    pipette.dispense(vol, plate.wells()[plate.columns()[well[1]][well[0]]])
    pipette.drop_tip()

def add_medium_to_well(pipette, plate, source, src_well, dest_well):
    pipette.pick_up_tip()
    pipette.aspirate(60, source.wells()[src_well])
    pipette.dispense(60, plate.wells()[dest_well])
    pipette.blow_out()
    pipette.drop_tip()
