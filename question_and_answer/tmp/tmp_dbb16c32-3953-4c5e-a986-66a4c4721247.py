from opentrons import simulate, protocol_api
from opentrons.types import Point

metadata = {
    'protocolName': 'Viability and Cytotoxicity Experiment',
    'author': 'Assay Biotech',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 treated with thapsigargin',
}

# Specify custom labware
custom_lw = {
    'greiner_96_wellplate_200ul': 'labware/custom_greiner_96_wellplate_200ul/1/custom_greiner_96_wellplate_200ul.json',
    'opentrons_50ul_tiprack': 'labware/opentrons_96_tiprack_300ul/1/opentrons_96_tiprack_300ul.json',
    'opentrons_200ul_tiprack': 'labware/opentrons_96_tiprack_300ul/1/opentrons_96_tiprack_300ul.json',
}

# Load labware definitions
metadata['apiLevel'] = '2.10'
protocol = protocol_api.ProtocolContext(file=__file__,
                                        custom_labware=custom_lw,
                                        simulate=True,
                                        metadata=metadata)

# Load necessary labware
cell_plate = protocol.load_labware('greiner_96_wellplate_200ul', '3')
tubes_1 = protocol.load_labware('opentrons_50ul_tiprack', '4')
tubes_2 = protocol.load_labware('opentrons_200ul_tiprack', '6')

# Define functions
def count_cells():
    # Add your code for counting cells here
    pass

def seed_cells():
    plate_type = 'greiner_96_wellplate_200ul'
    num_wells = 96
    plate = protocol.load_labware(plate_type, '3')
    cell_count = 8000
    well_volume = 200

    cell_volume = well_volume * 0.1
    cells_per_well = cell_volume / cell_count
    cell_suspension_tube = tubes_1.wells()[0]
    cell_suspension_tube_name = cell_suspension_tube.get_name()
    protocol.comment('Add {} cells to {}.'.format(cell_count, cell_suspension_tube_name))

    # Do the seeding
    for well in plate.wells():
        if well == plate.wells()[0]:
            continue
        well.transfer(cells_per_well, cell_suspension_tube)

def load_drugs():
    # Add loading of drugs starting from tube rack
    pass

def distribute_drugs():
    # Add distributing of drugs to wells on the plate
    pass

def add_reagent():
    for well in cell_plate.wells():
        if well.row == 'A' and well.col in [4, 5, 6]:
            # Negative control
            continue
        elif well.row == 'D' and well.col in [1, 2, 3]:
            # Cells treated with 0.39 nM thapsigargin
            continue
        elif well.row == 'D' and well.col == 4:
            # Set up CellTox Green reagent in row D for thapsigargin treatment
            reagent = tubes_2.wells()[1]
        else:
            reagent = tubes_2.wells()[0]
        well.transfer(15, reagent)

def read_fluorescence():
    # Add reading of fluorescence
    pass

def add_cell_titer_glo_2():
    for well in cell_plate.wells():
        if well.row == 'A' and well.col in [4, 5, 6]:
            # Negative control; no cells present
            continue
        elif well.row == 'D' and well.col in [1, 2, 3]:
            # Cells treated with 0.39 nM thaps.
            continue
        else:
            reagent = tubes_2.wells()[0]
            well.transfer(80, reagent)

def read_luminescence():
    # Add reading of luminescence
    pass

# Execute
def run(protocol):
    count_cells()
    seed_cells()
    load_drugs()
    distribute_drugs()
    add_reagent()
    read_fluorescence()
    add_cell_titer_glo_2()
    read_luminescence()

run(protocol)
