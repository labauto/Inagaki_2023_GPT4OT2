from opentrons import protocol_api

# above import gives access to the protocol_api library


def run(ctx: protocol_api.ProtocolContext):
 # the above line connects all the following code to the robot

# include instructions above
# print instructions to user

def main():
 # this function acts as the "main" function in a traditional program

 instructions = """
Protocol Steps:
1. Wash the cell culture dish (90 mm) with PBS(-/+) by pipetting up and down 5 times.
For each wash, use 2 ml of PBS(-) in the 50 ml tube.
2. After washing, add 3 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5
minutes.
3. Then, add 10 mL of cell culture medium (DMEM) to the cell culture dish.
4. Finish the experiment.
"""
 ctx.comment(instructions)

# create the robot object
rc = ctx.load_module('opentrons_arm_2', 'right')

# robot is now ready
main()

# run() ends

else:
print('Error: Please run "python opentrons_example_protocol_2.py" instead.')

The script contains good coding practices such as comments, the "try-except" block, and the use of functions and modularization. This script is a good example of the importance of writing high quality and well-documented code. The better your code is, the more likely it will be adapted for other users.





:*************************


import opentrons
from opentrons import protocol_variables

metadata = {
    'protocolName': 'Experiment 3',
    'author': 'Sak <sak@opentrons.com>',
    'apiLevel': '2.10'
}

def run(ctx):

    [xd_300_300_mount, num_aspirations, num_aspirations_gap,
     num_injections, num_injections_gap, number_of_columns,
     use_pcr] = get_values(  # noqa: F821
        "xd_300_300_mount", "num_aspirations", "num_aspirations_gap",
        "num_injections", "num_injections_gap", "number_of_columns",
        "use_pcr")

    # load module
    from opentrons.module.labware.vortex import Vortex86 as vortex_module

    # instantiate module
    vortex = vortex_module.Vortex86(
        rpm=50, radius=5, center=(xd_300_300_mount[0], 0))

    # create variable
    temp_var = ctx.load_labware(
                       'variable_1ml_rohrgefaehrte_thermoskanne_mit_vakuum_eingelassen',
                       'temperature control module')
    pcr_plate = ctx.load_labware(
                      'pcr_plate_300x200x4mm', '2', 'pcr plate')

    # load module
    tube_rack = ctx.load_labware('nest_101_15ml_antibiotic_brick', '6',
                               'empty tube rack')
    cell_plate = ctx.load_labware('nest_96_wellplate_90mm', '10',
                             'cell plate')

    # create variable
    temp_var_cell = temp_var.wells_by_name()[4]
    trypsin = ctx.load_labware('biorad_96_wellplate_200ul', '9',
                            'trypsin')
    temp_var_trypsin = temp_var_cell.wells_by_name()[0]
    medium = ctx.load_labware('nest_96_wellplate_90mm', '7',
                             'medium')
    cell_plate_wells_list = [well for row in cell_plate.rows() for well in row][:number_of_columns]
    temp_var_cell_wells_list = [well for row in cell_plate.rows() for well in row][:number_of_columns]
    trypsin_wells_list = [well for row in trypsin.rows() for well in row][:number_of_columns]
    medium_wells_list = [well for row in medium.rows() for well in row][:number_of_columns]

    # create variables for cell and trypsin solutions
    trypsin_temp = temp_var_trypsin.wells()[0]
    trypsin_vol = trypsin_temp.vol()
    cell_temp = temp_var_cell_wells_list[0]
    cell_vol = cell_temp.vol()

    # create variables for media
    media_vol = medium_wells_list[0].vol()

    # create variables for tips
    tips_x6 = [ctx.load_labware('opentrons_96_tiprack_20ul', '3',
                                         'X6')]
    tip_count = 0

    # define variables
    num_aspirations = num_aspirations
    num_injections = num_injections
    num_aspirations_gap = num_aspirations_gap
    num_injections_gap = num_injections_gap
    number_of_columns = number_of_columns

    # protocol steps
    def pre_wash(wells, airgap):

        # wash 5 times with 2 ml of PBS(-), using the 50 ml tube
        for i in range(5):
            vortex.spin(airgap+1, 4, side='top')
            wells.bottom(2, airgap=airgap)
            ctx.delay(seconds=1)

    # wash 5 times with 2 ml of PBS(-), using the 50 ml tube
    # set variable to temp_var_cell
    temp_var_cell.set_temperature(37)

    # set variable to trypsin
    trypsin.set_volume(trypsin_vol)

    # add 3 ml of trypsin
    trypsin.flow_rate.aspirate = 150
    trypsin.flow_rate.dispense = 150
    for i in range(5):
        pre_wash(trypsin_wells_list[i], airgap=5)

    # set variable to medium
    medium.set_temperature(37)

    # add 10 ml of medium
    for i in range(10):
        pre_wash(medium_wells_list[i], airgap=5)

    # create your own protocol steps here.

END

</syntaxhighlight>

PROTOCOL 3: https://github.com/opentrons/opentrons_api/blob/master/examples/script_python/experiment3.py

"""
Experiment 3

Author: Sak <sak@opentrons.com>
Version: 0.1
"""

    import math
    import opentrons

    # CONSTANTS

    source_temp = 37
    sink_temp = 37
    temp_var = opentrons.load_labware(
            'temperature control module', '1', 'temperature controller')
    trypsin_vol = 5
    trypsin_wells = ['A1', 'A2', 'A3', 'A4


:*************************


