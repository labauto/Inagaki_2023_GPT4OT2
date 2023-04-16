from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Viability and Cytotoxicity Assay'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Declare labware
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_15ml = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 6)
    stock_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)
    reagent_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 8)
    plate_96_well = protocol.load_labware('opentrons_96_tc_plate_200ul', 9)
    heater_shaker = protocol.load_module('temperature module gen2', 1)
    shaker_plate = heater_shaker.load_labware('opentrons_96_tc_plate_200ul')
    temp_plate = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 11)
    
    # Declare pipettes
    p20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack_200ul])

    # First labware, 1mM Thapsigargin (A1)
    stock_A1 = stock_rack.wells_by_name()['A1']
    
    # Thapsigargin stock concentrations
    stock_concentrations = ['100uM', '10uM', '1uM', '100nM', '50nM', '10nM']
    
    # Volume transfer per concentration
    volume_transfer = [25, 22.5, 20, 17.5, 15, 12.5]

    # Prepare Thapsigargin stocks
    for i in range(6):
        p300.transfer(volume_transfer[i], stock_A1, stock_rack.wells_by_name()[f'A{i + 2}'])

    # Dilution concentrations
    dilutions_4x = ['1.56nM', '3.12nM', '6.24nM', '12.52nM', '25nM', '50nM', '100nM', '200nM', '400nM', '800nM', '1600nM', '2000nM']
    dilutions_2x = [dil.replace('nM', 'nM_2X') for dil in dilutions_4x]

    # Prepare wells
    well_list = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']

    # Prepare 4X dilutions
    for i, tube_well in enumerate(well_list):
        p300.transfer(50, stock_rack.wells_by_name()[f'A{i + 1}'], stock_rack.wells_by_name()[tube_well])

    # Prepare 2X dilutions
    for i in range(12):
        p300.transfer(100, stock_rack.wells_by_name()[well_list[i]], tube_rack_15ml.wells_by_name()[f'C{i + 1}'])

    # Map to 96 well plate
    well_symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    concentration_map = {
        (i, j): dilutions_2x[(i // 2) + ((j - 1) * 4)] for j in range(1, 5) for i in range(1, 7)
    }

    # Fill 96 well plate with 2X concentrated dilutions
    for i, well_sym in enumerate(well_symbols):
        for j in range(1, 13):
            if (i, j) in concentration_map:
                p300.transfer(60, tube_rack_15ml.wells_by_name()[f'C{j - 1}'],
                              plate_96_well.wells_by_name()[f'{well_sym}{j}'])

    # Function to add reagent with specific mixing parameters
    def add_reagent(reagent_well, volume, mix_volume, num_mixes):
        p20.pick_up_tip()
        for dest_well in plate_96_well.rows()[0]:
            if dest_well in plate_96_well.wells_by_name():
                p20.distribute(volume, reagent_rack.wells_by_name()[reagent_well], dest_well,
                               mix_after=(num_mixes, mix_volume))
        p20.drop_tip()

    # Add CellTox Green reagent
    add_reagent("B2", 15, 20, 3)

    # Shaking and timed incubation
    heater_shaker.shake(duration=2*60, speed=500)
    protocol.delay(15*60)
    
    # Add Cell Titer Glo 2.0 reagent
    add_reagent("B1", 80, 100, 5)

    # Shaking and timed incubation
    heater_shaker.shake(duration=2*60, speed=500)
    protocol.delay(10*60)

    # End of protocol
