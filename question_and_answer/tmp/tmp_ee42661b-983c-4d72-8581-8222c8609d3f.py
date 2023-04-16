from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def cell_seeding(protocol: protocol_api.ProtocolContext):
    # Your cell seeding process code here

def prepare_thapsigargin_dilutions(protocol: protocol_api.ProtocolContext):
    # Your code for preparing thapsigargin dilutions here

def drug_addition(protocol: protocol_api.ProtocolContext):
    # Your drug addition process code here

def measure_cytotoxicity(protocol: protocol_api.ProtocolContext):
    # Your measure cytotoxicity process code here

def measure_viability(protocol: protocol_api.ProtocolContext):
    # Your measure viability process code here

def main(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    tiprack_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    tiprack_200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 6)
    drug_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 7)
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    heater_shaker = protocol.load_module('temperature module', 10)
    heater_shaker_plate = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')
    
    # Ensure HEPA filter turned on
    
    # Seeding A549 cells
    cell_seeding(protocol)

    # Addition of various concentrations of Thapsigargin on the second day
    prepare_thapsigargin_dilutions(protocol)
    drug_addition(protocol)

    # After 72 hours of drug treatment, carry out the following steps
    measure_cytotoxicity(protocol)
    measure_viability(protocol)

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.10')
    main(protocol)
