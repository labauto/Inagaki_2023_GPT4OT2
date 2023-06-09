 import math

import opentrons

def comment(text):
 """
Comment function.
"""
pass


def run_experiment(ctx):
 """
Function for running the experiment.
"""
# get parameter values from json string
# set values for parameter variables
# run protocol
# end protocol
# run function
# end function

def run_protocol(ctx):

def run_function(ctx):


def main():
 """
Main function.
"""
ctx = opentrons.load_device(
'generic_xl_450mm_pcr_slot',
'left',
description='generic_xl_450mm_pcr_slot')
# create variable
trypsin_solution = ctx.load_liquid(
'nest_15ml_trypsin_solution',
'1',
description='15ml trypsin solution')
cell_culture_medium = ctx.load_liquid(
'nest_15ml_cell_culture_medium',
'2',
description='15ml cell culture medium')
pbs = ctx.load_liquid(
'opentrons_96_tube_5000ul_pcr_safelock_cap',
'3',
description='96-tube PBS(-)')
# create variable
cell_culture_dish = ctx.load_object(
'cell_culture_dish_200ml',
'4',
description='cell culture dish')
# run protocol
trypsin_solution.flow_rate.aspirate = 0.5
trypsin_solution.flow_rate.dispense = 1
trypsin_solution.flow_rate.speed = 0.5
trypsin_solution.flow_rate.aspirate_offset = 50
trypsin_solution.flow_rate.dispense_offset = 50
trypsin_solution.flow_rate.aspirate_rate = 0.5
trypsin_solution.flow_rate.dispense_rate = 0.5
trypsin_solution.flow_rate.aspirate_dist = 50
trypsin_solution.flow_rate.dispense_dist = 50
trypsin_solution.flow_rate.aspirate_height = 10
trypsin_solution.flow_rate.dispense_height = 10
trypsin_solution.flow_rate.speed_range = [0.5, 0.5]
trypsin_solution.flow_rate.aspirate_range = [50, 50]
trypsin_solution.flow_rate.dispense_range = [50, 50]
trypsin_solution.flow_rate.aspirate_offset_range = [50, 50]
trypsin_solution.flow_rate.dispense_offset_range = [50, 50]
trypsin_solution.flow_rate.aspirate_rate_range = [0.5, 0.5]
trypsin_solution.flow_rate.dispense_rate_range = [0.5, 0.5]
trypsin_solution.flow_rate.aspirate_height_range = [10, 10]
trypsin_solution.flow_rate.dispense_height_range = [10, 10]
trypsin_solution.flow_rate.aspirate_rate_offset = 50
trypsin_solution.flow_rate.dispense_rate_offset = 50
trypsin_solution.flow_rate.aspirate_offset_rate = 0.5
trypsin_solution.flow_rate.dispense_offset_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_rate = 0.5
trypsin_solution.flow_rate.dispense_height_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_offset = 50
trypsin_solution.flow_rate.dispense_height_offset = 50
trypsin_solution.flow_rate.aspirate_rate_height = 0.5
trypsin_solution.flow_rate.dispense_rate_height = 0.5
trypsin_solution.flow_rate.aspirate_rate_height_offset = 50
trypsin_solution.flow_rate.dispense_rate_height_offset = 50
trypsin_solution.flow_rate.aspirate_rate_height_rate = 0.5
trypsin_solution.flow_rate.dispense_rate_height_rate = 0.5
trypsin_solution.flow_rate.aspirate_offset_height = 50
trypsin_solution.flow_rate.dispense_offset_height = 50
trypsin_solution.flow_rate.aspirate_offset_height_rate = 0.5
trypsin_solution.flow_rate.dispense_offset_height_rate = 0.5
trypsin_solution.flow_rate.aspirate_offset_height_offset = 50
trypsin_solution.flow_rate.dispense_offset_height_offset = 50
trypsin_solution.flow_rate.aspirate_height_height = 10
trypsin_solution.flow_rate.dispense_height_height = 10
trypsin_solution.flow_rate.aspirate_height_height_offset = 50
trypsin_solution.flow_rate.dispense_height_height_offset = 50
trypsin_solution.flow_rate.aspirate_height_height_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_rate_offset = 50
trypsin_solution.flow_rate.dispense_height_height_rate_offset = 50
trypsin_solution.flow_rate.aspirate_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_rate_offset = 50
trypsin_solution.flow_rate.dispense_height_height_rate_offset = 50
trypsin_solution.flow_rate.aspirate_height_height_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_offset_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_rate_offset = 50
trypsin_solution.flow_rate.dispense_height_height_rate_offset = 50
trypsin_solution.flow_rate.aspirate_height_height_rate_offset_rate = 0.5
trypsin_solution.flow_rate.dispense_height_height_rate_offset_rate = 0.5
trypsin_solution.flow_rate.aspirate_height_height_offset = 50
trypsin_solution.flow_rate.dispense_height_height_offset = 50
trypsin_solution.flow_rate.aspirate_height_height_offset_rate = 0
