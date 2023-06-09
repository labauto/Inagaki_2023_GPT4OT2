 import opentrons

def comment(comment):
 """
Function to print a comment
Example:
print(comment('This is a comment.'))
"""
return comment

def run_experiment(ctx):
 """
Function to run the experiment
"""
 # TODO: Replace with your own values
 cell_type = 'H1'
 media_type = 'DMEM'
 trypsin_type = 'PBS'
 # create variables
 cell_dish = ctx.load_object(cell_type+'_96_wellplate', 1)
 media_tube = ctx.load_object(media_type+'_15ml_tube', 2)
 trypsin_tube = ctx.load_object(trypsin_type+'_15ml_tube', 3)
 # create variables
 num_washes = 5
 num_minutes = 5
 # create variables
 num_colonies = 10
 # create variables
 trypsin_vol = 3
 media_vol = 10
 # create variables
 num_colonies_after = 10
 # create variables
 cell_vol = 2
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
 trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
 trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
 trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
 trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
 trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
 trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
trypsin_tube_location = 'right'
 media_tube_location = 'right'
 # create variables
trypsin_tube_location = 'top'
 media_tube_location = 'top'
 # create variables
trypsin_tube_location = 'bottom'
 media_tube_location = 'bottom'
 # create variables
trypsin_tube_location = 'front'
 media_tube_location = 'front'
 # create variables
trypsin_tube_location = 'back'
 media_tube_location = 'back'
 # create variables
trypsin_tube_location = 'left'
 media_tube_location = 'left'
 # create variables
trypsin_tube_location = 'right'
 media_tube_location =
