 #!/usr/bin/env python

import opentrons

def run_script(ctx):
 """
Function to run the script.
"""
 # get parameter values from the command line
 # for more information, see https://www.opentrons.com/api/parameters
 # p50 = float(ctx.get_value('p50', '5.0'));
 # wash = int(ctx.get_value('wash', 1))
 # trypsin = int(ctx.get_value('trypsin', 1))
 # medium = int(ctx.get_value('medium', 1))
 # num_tubes = int(ctx.get_value('num_tubes', 1))
 # tube_size = ctx.get_value('tube_size', '10ul')
 # airgap = float(ctx.get_value('airgap', 5))
 # num_cols = int(ctx.get_value('num_cols', 1))
 # col_size = ctx.get_value('col_size', '100ul')
 # num_rows = int(ctx.get_value('num_rows', 1))
 # row_size = ctx.get_value('row_size', '100ul')
 # airgap2 = float(ctx.get_value('airgap2', 5))
 # airgap3 = float(ctx.get_value('airgap3', 5))
 # airgap4 = float(ctx.get_value('airgap4', 5))
 # airgap5 = float(ctx.get_value('airgap5', 5))
 # airgap6 = float(ctx.get_value('airgap6', 5))
 # airgap7 = float(ctx.get_value('airgap7', 5))
 # airgap8 = float(ctx.get_value('airgap8', 5))
 # airgap9 = float(ctx.get_value('airgap9', 5))
 # airgap10 = float(ctx.get_value('airgap10', 5))
 # airgap11 = float(ctx.get_value('airgap11', 5))
 # airgap12 = float(ctx.get_value('airgap12', 5))
 # airgap13 = float(ctx.get_value('airgap13', 5))
 # airgap14 = float(ctx.get_value('airgap14', 5))
 # airgap15 = float(ctx.get_value('airgap15', 5))
 # airgap16 = float(ctx.get_value('airgap16', 5))
 # airgap17 = float(ctx.get_value('airgap17', 5))
 # airgap18 = float(ctx.get_value('airgap18', 5))
 # airgap19 = float(ctx.get_value('airgap19', 5))
 # airgap20 = float(ctx.get_value('airgap20', 5))
 # airgap21 = float(ctx.get_value('airgap21', 5))
 # airgap22 = float(ctx.get_value('airgap22', 5))
 # airgap23 = float(ctx.get_value('airgap23', 5))
 # airgap24 = float(ctx.get_value('airgap24', 5))
 # airgap25 = float(ctx.get_value('airgap25', 5))
 # airgap26 = float(ctx.get_value('airgap26', 5))
 # airgap27 = float(ctx.get_value('airgap27', 5))
 # airgap28 = float(ctx.get_value('airgap28', 5))
 # airgap29 = float(ctx.get_value('airgap29', 5))
 # airgap30 = float(ctx.get_value('airgap30', 5))
 # airgap31 = float(ctx.get_value('airgap31', 5))
 # airgap32 = float(ctx.get_value('airgap32', 5))
 # airgap33 = float(ctx.get_value('airgap33', 5))
 # airgap34 = float(ctx.get_value('airgap34', 5))
 # airgap35 = float(ctx.get_value('airgap35', 5))
 # airgap36 = float(ctx.get_value('airgap36', 5))
 # airgap37 = float(ctx.get_value('airgap37', 5))
 # airgap38 = float(ctx.get_value('airgap38', 5))
 # airgap39 = float(ctx.get_value('airgap39', 5))
# num_volumes = int(ctx.get_value('num_volumes', 1))

 def run():

 """Function to run the experiment."""

    ctx = opentrons.load_library("python").context()

    if not hasattr(ctx, 'load-tube-rack'):        raise Exception("Please load the Tube Rack module first")

    tube1, tube2, tube3, tube4, tube5, tube6, tube7, tube8, tube9, tube10, tube11, tube12, tube13, tube14, tube15, tube16, tube17, tube18, tube19, tube20, tube21, tube22, tube23, tube24, tube25, tube26, tube27, tube28, tube29, tube30, tube31, tube32, tube33, tube34, tube35, tube36, tube37, tube38, tube39, tube40, tube41, tube42, tube43, tube44, tube45, tube46, tube47, tube48, tube49, tube50

    ctx.comment("Washing the cell culture dish with PBS(-).")

    ctx.comment("Adding 3 ml of trypsin solution to the cell culture dish.")

    ctx.comment("Incubating for 5 minutes.")

    ctx.comment("Adding 10 mL of cell culture medium to the cell culture dish.")

    ctx.comment("Finishing the experiment.")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

    ctx.comment("")

	 run()

	 return run()

	 if __name__ == "__main__":
run()

	END

	"""End of Script"""

	"""End of File"""


