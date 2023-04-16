from opentrons import simulate, execute, protocol_api
from opentrons.types import Point

# Functions for individual experiment steps
def clean_workspace(pipette, ethanol_vol):
    # Clean the inside of the robot with 70% ethanol
    pass # This step can't be done by the Opentrons robot directly

def prepare_cell_suspension(pipette, well_plate, tubes, cell_vol):
    cell_count = 8000
    cell_volume = cell_vol / cell_count
    for well in well_plate.wells():
        pipette.transfer(cell_volume, tubes['cell_suspension'].bottom(), well.bottom())
       
def prepare_thapsigargin_dilutions(pipette, tube_rack):
    pass # Prepare thapsigargin dilutions manually

def add_thapsigargin(pipette, tube_rack, well_plate):
    pass # Add thapsigargin to well plate manually

def transfer_celltox_green(pipette, reagent_tube, well_plate):
    volume_to_dispense = 15
    pipette.transfer(volume_to_dispense, reagent_tube.bottom(), well_plate.wells())

def shake_and_incubate_and_read_fluorescence(shaker, well_plate):
    shaker.shake(duration=2*60, speed=500)
    well_plate.incubate(minutes=15, temperature=25)
    well_plate.measure_fluorescence(wavelength=(485, 520))

def transfer_cell_titer_glo(pipette, reagent_tube, well_plate):
    volume_to_dispense = 80
    pipette.transfer(volume_to_dispense, reagent_tube.bottom(), well_plate.wells())

def shake_and_incubate_and_read_luminescence(shaker, well_plate):
    shaker.shake(duration=2*60, speed=500)
    well_plate.incubate(minutes=10, temperature=25)
    well_plate.measure_luminescence()

# Main function
def run(protocol: protocol_api.ProtocolContext):
    # Assign labware
    pipette = protocol.load_instrument('p300_multi', 'left')
    well_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    reagent_tube_celltox_green = tube_rack.wells_by_name()['B2']
    reagent_tube_cell_titer_glo = tube_rack.wells_by_name()['B1']
    
    tubes = {
        'cell_suspension': tube_rack.wells_by_name()['A1']
    }
    
    # Call functions for each experiment step
    clean_workspace(pipette, 70)
    prepare_cell_suspension(pipette, well_plate, tubes, 60)
    prepare_thapsigargin_dilutions(pipette, tube_rack)
    add_thapsigargin(pipette, tube_rack, well_plate)
    transfer_celltox_green(pipette, reagent_tube_celltox_green, well_plate)
    shake_and_incubate_and_read_fluorescence(well_plate)
    transfer_cell_titer_glo(pipette, reagent_tube_cell_titer_glo, well_plate)
    shake_and_incubate_and_read_luminescence(well_plate)

# Simulate the protocol (optional)
protocol = simulate.get_protocol_api('2.11')
run(protocol)

