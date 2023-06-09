# coding: utf-8
# author: <your name>
# description: Python script for wet experiments
# run module: <your module>
"""
"""
from opentrons import protocol_api

metadata = {
    'author': 'Chaitanya <protocols@call9smith.com>',
    'description': 'Simple example of a wet experiment.',
    'run_module': 'DsemtntsTests'
    }

def run(ctx):
    # normal protocol call
    # add 4-5 ml of PBS(-), mix for 5 seconds
    # add 5-7 ml of Trypsin to the cell culture dish
    if __name__ == '__main__':
        ctx.pause("Screwing Cover back to flask")
        # comment out these lines if you wish to allow user to enter values

    # modify this if your cell culture dish is not 6x10 cm
    cell_size = "10 cm"
    flask = ctx.load_module('labware:throat_96_ml', '1')
    tube = ctx.load_labware('nest_1_ml_generic_pcrform_1500ul', '2')
    pbs = tube.wells()[0].top(0.1)
    trypsin = flask.wells()[0].top(1)
    culture_medium = ctx.well_map.get(
        "cell_culture_well")

    def add(v_start_=-1, v_inc=-1):
        if float(v_start_) = -1:
            v_start_ = 0
        if float(v_inc) = -1:
            v_inc = 0.1
        if v_start_ < 0 or v_inc < 0:
            raise ProtocolException("Invalid argument")
        #
        return math.floor(v_start_) + v_inc * (v_start_+v_inc)
        # cell wash with PBS(-), 5 ml in tube
        add(5)
        # add Trypsin
        if v_start_ != -1:
            add(v_start_, v_inc)
        else:
            add(5, v_inc)
        # cell incubation for 5 minutes
        ctx.pause("Hitting Add>")
        for i in range(1, 5):
            ctx.delay(seconds=5)
        ctx.pause("Swiping card over reader")
        ctx.pause("Incubating cell cultures with Trypsin")
        add(10)
        culture_medium.engage_lid()
        ctx.comment("Remove all vortexing solution and medium")
        culture_medium.top(5)
        culture_medium.dish()
        ctx.pause("Airlifting medium to cell culture dish")
        airlift_medium = ctx.load_airlift(
                airlift_house.bic1_slant(timing.Second(), weight=20))
        for medium in airlift_medium.lower_half():
            add(medium*.9, v_inc)
        # add ltn_buffer
        ltn_buffer = ctx.loaded_libraries.get(
                'opentrons_9_reservoir_15ml_pcr_tecwyne')
        ltn_buffer.engage_lid()
        ltn_buffer.add_liquid(50.)
        ctx.comment("Finish protocol")
        ctx.comment("Remove airlifted solution")
        airlift_medium.drop_liquid(30)
        ctx.comment("Remove tubing and reclose tube rack")
        ctx.comment(
            '<info>Protocol complete, please remove the sample and screen</info>')
        ctx.comment("Screwing cover back on cell culture dish")

END

"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
 """


"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
 """
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
 """
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""


:*************************


import opentrons
import math

def execute_script(ctx):
 ###############
ctx.load_module('skipper_script_api')
metadata = ctx.load_meta_data('your_metadata')
user_script = [
 [
 [sl.PRINT, 'Please set the sample', f' {metadata['column_selection_index']}'],
 [sl.USER_INPUT],

],



:*************************


