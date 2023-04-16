from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'author': 'Your Name <your.name@example.com>'
}


def clean_and_prepare_robot(protocol: protocol_api.ProtocolContext):
    protocol.comment("Cleaning and preparing robot")
    # Add your robot preparation and cleaning steps here


def seed_a549_cells(protocol: protocol_api.ProtocolContext, well_plate, cell_count, volume):
    protocol.comment(f"Seeding {cell_count} A549 cells in each well")
    # Add seeding procedure based on your specific setup


def prepare_thapsigargin_dilutions(protocol: protocol_api.ProtocolContext, stock_tubes, working_tubes):
    protocol.comment("Preparing Thapsigargin dilutions")
    # Add dilution preparation steps based on your specific setup


def add_thapsigargin_to_well_plate(protocol: protocol_api.ProtocolContext, well_plate, dilution_tubes):
    protocol.comment("Adding Thapsigargin to 96 well plate")
    # Perform the drug addition based on your specific setup


def celltox_green_assay(protocol: protocol_api.ProtocolContext, heater_shaker, well_plate, reagent_tube, tipracks_20):
    protocol.comment("Adding CellTox Green reagent to the well plate")
    # Perform the cell toxicity assay based on your specific setup


def cell_titer_glo_assay(protocol: protocol_api.ProtocolContext, heater_shaker, well_plate, reagent_tube, tipracks_200):
    protocol.comment("Adding Cell Titer Glo 2.0 reagent to the well plate")
    # Perform the cell viability assay based on your specific setup


def run(protocol: protocol_api.ProtocolContext):
    # Define labware, pipettes and modules used in the experiment
    tipracks_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    tipracks_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 6)
    well_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)
    heater_shaker = protocol.load_module('temperature module', 10)

    cell_count = 8000
    cell_volume = 60  # in microL

    clean_and_prepare_robot(protocol)
    seed_a549_cells(protocol, well_plate, cell_count, cell_volume)
    prepare_thapsigargin_dilutions(protocol, tube_rack, tube_rack)
    add_thapsigargin_to_well_plate(protocol, well_plate, tube_rack)
    celltox_green_assay(protocol, heater_shaker, well_plate, tube_rack.well('B2'), tipracks_20)
    cell_titer_glo_assay(protocol, heater_shaker, well_plate, tube_rack.well('B1'), tipracks_200)


if __name__ == '__main__':
    run(protocol_api.ProtocolContext())
