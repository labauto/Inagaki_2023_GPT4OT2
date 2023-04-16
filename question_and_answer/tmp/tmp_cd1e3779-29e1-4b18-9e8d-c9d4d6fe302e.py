import time
import opentrons
from opentrons import protocol_api

# Constants
FLASK_VOLUME = 225
WELL_2X_CONCENTRATIONS = range(1, 7)

# Opentrons Protocol
def initialize_robot() -> protocol_api.ProtocolContext:
    protocol = opentrons.simulate.get_protocol_api("2.1")
    protocol.home()
    return protocol

def clean_robot(protocol: protocol_api.ProtocolContext):
    # Clean the robot and initialize the HEPA filter. This is done manually.
    pass

def seed_cells(protocol: protocol_api.ProtocolContext, cell_volume: float):
    # Seed A549 cells (8,000 per well) in a 96 well plate with 60uL cell suspensions in Ham’s F12K medium
    pass

def mix_tube_and_transfer(protocol: protocol_api.ProtocolContext, source_tube, destination_tube, mixing_volume: int, transfer_volume: int):
    protocol.load_instrument("multichannel", "left").mix(3, mixing_volume, source_tube)
    pipette = protocol.load_instrument("multichannel", "left")
    pipette.aspirate(transfer_volume, source_tube)
    pipette.dispense(transfer_volume, destination_tube)

def prepare_initial_stock(protocol: protocol_api.ProtocolContext):
    # Prepare the initial stock concentrations in tubes A1 - A6 and B1
    pass

def prepare_4x_working_concentrations(protocol: protocol_api.ProtocolContext):
    # Prepare the 4X working concentrations in tubes C1 - C6 and D1 - D6
    pass

def prepare_2x_working_concentrations(protocol: protocol_api.ProtocolContext):
    # Prepare the 2X working concentrations of thapsigargin in tubes C1 - C6 and D1 - D6
    pass

def add_thapsigargin_to_wells(protocol: protocol_api.ProtocolContext):
    # Add the equal volume of 2X thapsigargin to each well of the 96 well plate
    pass

def measure_cytotoxicity(protocol: protocol_api.ProtocolContext):
    # Perform fluorescence reading at 72 hours using CellTox Green reagent and a Biotek microplate reader
    pass

def measure_viability(protocol: protocol_api.ProtocolContext):
    # Perform luminescence measurements using the Cell Titer-Glo 2.0 reagent and a Biotek microplate reader
    pass

def main():
    protocol = initialize_robot()
    clean_robot(protocol)
    seed_cells(protocol, 60)
    prepare_initial_stock(protocol)
    prepare_4x_working_concentrations(protocol)
    prepare_2x_working_concentrations(protocol)
    add_thapsigargin_to_wells(protocol)

    time.sleep(72 * 3600)  # Wait for 72 hours

    measure_cytotoxicity(protocol)
    measure_viability(protocol)

if __name__ == "__main__":
    main()
