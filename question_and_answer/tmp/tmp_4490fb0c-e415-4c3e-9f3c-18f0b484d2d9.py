 import opentrons

def run(ctx):
 """
Function that runs the experiment
"""
 # get parameter values from json
parameters = {
    'cell_type': 'H1',
    'wash_solution': 'PBS(-)',
    'residual_solution': 'PBS(-)',
    'cell_culture_medium': 'DMEM',
    'wash_volume': '2',
    'residual_volume': '3',
    'incubation_solution': 'trypsin',
    'incubation_volume': '3',
    'cell_culture_volume': '10'
    }
    ctx.set_parameter('cell_type', parameters['cell_type'])
    ctx.set_parameter('wash_solution', parameters['wash_solution'])
    ctx.set_parameter('residual_solution', parameters['residual_solution'])
    ctx.set_parameter('cell_culture_medium', parameters['cell_culture_medium'])
    ctx.set_parameter('wash_volume', float(parameters['wash_volume']) / 1000)
    ctx.set_parameter('residual_volume', float(parameters['residual_volume']) / 1000)
    ctx.set_parameter('incubation_solution', parameters['incubation_solution'])
    ctx.set_parameter('incubation_volume', float(parameters['incubation_volume']) / 1000)
    ctx.set_parameter('cell_culture_volume', float(parameters['cell_culture_volume']) / 1000)
    # load cell culture dish
    cell_dish = ctx.load_item('cell_dish', 3)
    # load tube with PBS(-)
    tube = ctx.load_item('tube_single', 1)
    # load trypsin solution in tube
    trypsin_solution = tube.load_item('trypsin_solution', 5)
    # load cell culture medium in tube
    cell_medium = tube.load_item('cell_medium', 6)
    # create variables
    pbs_vol = tube.load_item('pbs_volumetric', 4)
    trypsin_vol = trypsin_solution.load_item('trypsin_volumetric', 7)
    cell_medium_vol = cell_medium.load_item('cell_medium_volumetric', 8)
    cell_dish_vol = cell_dish.volume()
    # run protocol
    ctx.comment('Washing cell culture dish with PBS(-)')
    ctx.comment('\t\tStep 1')
    ctx.comment('\t\t\tPipetting up and down 5 times')
    ctx.comment('\t\t\tUse 2 ml of PBS(-) in the tube for each wash')
    ctx.comment('\t\t\tUse the same tube for all washes')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPipette up and down 5 times')
    ctx.comment('\t\t\tRemove the tube from the cell culture dish')
    ctx.comment('\t\t\tPlace the tube on the waste bin')
    ctx.comment('\t\t\tRepeat for all washes')
    ctx.comment('\t\t\tPlace the tube back on the cell culture dish')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the cell culture dish')
    ctx.comment('\t\t\tIncubate for 5 minutes')
    ctx.comment('\t\t\tPlace the lid on the tube')
    ctx.comment('\t\t\tPlace the tube on the stage')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the cell culture dish')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPlace the lid on the tube')
    ctx.comment('\t\t\tPlace the tube on the stage')
    ctx.comment('\t\t\tPlace the lid on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the cell culture dish')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPlace the lid on the tube')
    ctx.comment('\t\t\tPlace the tube on the stage')
    ctx.comment('\t\t\tPlace the lid on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the cell culture dish')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPlace the lid on the tube')
    ctx.comment('\t\t\tPlace the tube on the stage')
    ctx.comment('\t\t\tPlace the lid on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage')
    ctx.comment('\t\t\tPlace the lid on the cell culture dish')
    ctx.comment('\t\t\tPlace the cell culture dish on the stage')
    ctx.comment('\t\t\tPlace the tube on the cell culture dish')
    ctx.comment('\t\t\tPlace the lid on the tube')
    ctx.comment('\t\t\tPlace the tube on the stage')
    ctx.comment('\t\t\tPlace the lid on the waste bin')
    ctx.comment('\t\t\tPlace the waste bin on the stage
