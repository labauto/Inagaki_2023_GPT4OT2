 #!/usr/bin/env python

import opentrons

def run(ctx):
 """
Function for running the experiment
"""
 # get parameter values from json
parameters = {
    'protocols': '1',
    'tube_type': 'opentrons_96_tube_rack',
    'tube_position': 'right',
    'pcr_plate': 'opentrons_96_wellplate_200ul',
    'pcr_well_location': 'right',
    'pcr_well_name': 'A1',
    'pcr_well_volume': '3',
    'cell_dish_type': 'opentrons_96_wellplate_200ul',
    'cell_dish_position': 'left',
    'cell_dish_name': 'A1',
    'cell_dish_volume': '10',
    'wash_tube_type': 'opentrons_96_tube_rack',
    'wash_tube_position': 'left',
    'wash_tube_name': 'A1',
    'wash_tube_volume': '2'
}

# load the cell culture dish
cell_dish = ctx.load_object('cell_dish_type', 'cell_dish_position',
                                   'cell_dish_name',
                                  'cell_dish_volume')

# load the tube rack
tube_rack = ctx.load_object('tube_rack_type', 'tube_position',
                                 'tube_name',
                                  'tube_volume')

# load the PCR plate
pcr_plate = ctx.load_object('pcr_plate_type', 'pcr_plate_position',
                                 'pcr_well_name',
                                 'pcr_well_volume')

# load the wash tube
wash_tube = ctx.load_object('wash_tube_type', 'wash_tube_position',
                                 'wash_tube_name',
                                 'wash_tube_volume')

# create variable for trypsin solution
trypsin_solution = tube_rack.wells()[0]

# create variable for cell culture medium
cell_medium = cell_dish.wells()[0]

# create variable for PBS(-)
pbs = ctx.load_source('PBS_96_vial', 'pbs_source', 'right')

# create variable for final cell culture dish
final_cell_dish = ctx.load_object('cell_dish_type', 'final_cell_dish_position',
                                  'final_cell_dish_name',
                                 'final_cell_dish_volume')

# add trypsin solution to cell culture dish
ctx.comment('Adding trypsin solution to cell culture dish')
 trypsin_solution.flow_rate.min = 0
 trypsin_solution.flow_rate.max = 0.5
 trypsin_solution.flow_rate.set(0.1)

for well in cell_dish.wells():
 trypsin_solution.flow_rate.pause(seconds=1)
 trypsin_solution.aspirate(5, well)
 trypsin_solution.dispense(5, well)

ctx.comment('Adding cell culture medium to cell culture dish')
 cell_medium.flow_rate.min = 0
 cell_medium.flow_rate.max = 0.5
 cell_medium.flow_rate.set(0.1)
 cell_medium.aspirate(10, cell_dish)
 cell_medium.dispense(10, cell_dish)

# add wash buffer to cell culture dish
ctx.comment('Adding wash buffer to cell culture dish')
 for well in cell_dish.wells():
 pbs.flow_rate.pause(seconds=1)
 pbs.aspirate(2, well)
 pbs.dispense(2, well)

# close cell culture dish
ctx.comment('Closing cell culture dish')
 cell_dish.close()

# close tube rack
tube_rack.close()

# close PCR plate
pcr_plate.close()

# close wash tube
wash_tube.close()

# comment the results
ctx.comment('Protocols: {0}'.format(parameters['protocols']))
 ctx.comment('Tube rack: {0}'.format(tube_rack))
 ctx.comment('Cell culture dish: {0}'.format(cell_dish))
 ctx.comment('PBS: {0}'.format(pbs))
 ctx.comment('Final cell culture dish: {0}'.format(final_cell_dish))
 ctx.comment('Wash buffer: {0}'.format(pbs))
 ctx.comment('Trypsin solution: {0}'.format(trypsin_solution))
 ctx.comment('Cell culture medium: {0}'.format(cell_medium))
 ctx.comment('Protocols completed.')

def run(ctx):
 """
Function for running the experiment
""" # get parameter values from json
parameters = {
    'protocols': '1',
    'tube_type': 'opentrons_96_tube_rack',
    'tube_position': 'right',
    'pcr_plate': 'opentrons_96_wellplate_200ul',
    'pcr_well_location': 'right',
    'pcr_well_name': 'A1',
    'pcr_well_volume': '3',
    'cell_dish_type': 'opentrons_96_wellplate_200ul',
    'cell_dish_position': 'left',
    'cell_dish_name': 'A1',
    'cell_dish_volume': '10',
    'wash_tube_type': 'opentrons_96_tube_rack',
    'wash_tube_position': 'left',
    'wash_tube_name': 'A1',
    'wash_tube_volume': '2'
}

# load the cell culture dish
cell_dish = ctx.load_object('cell_dish_type', 'cell_dish_position',
                                 
