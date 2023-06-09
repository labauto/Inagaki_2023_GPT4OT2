obs = [
{ 'question' : 'What is the density of XXX?' ,
'type' : 'float_input' ,
'name' : 'density' ,
'min' : 0,
'max' : 1.095
},
{ 'question' : 'What is the volume of XXX?' ,
'type' : 'float_input' ,
'name' : 'volume' ,
'min' : 0,
'max' : 50
},

{ 'question' : 'What is the radius of XXX?' ,
'type' : 'float_input' ,
'name' : 'radius' ,
'min' : 1,
'max' : 7}
],
'opentrons_version' : '2.2.0'

def run_script ( script , input_variables ):


def run_experiment ( steps ) :


def do_step ( num , output , next_step , max_len ):

print ( num )

print ( output )

print ( next_step )

print ( "Max. lenght of next_step = " + str ( max_len ))

while True :

try :
 print ( "Wash cell culture dish with 2ml PBS(-)." )
Max_len = float ( num ) + float ( next_step [ "max_len" ]) if next_step [ "max_len" ] else num

except ValueError :
print ( "Wrong input of num, see console." )
print ( "" )
aspirin = [

{ 'name' : 'Aspirin',
'name_alt' : 'Aspirin',
'formula' : 'C9H8O4',
'note' : '',
'id' : 'aspirin' ,
'nameJson' : """\
F: "Aspirin",
"""
}
]
x = 1
for Y , AA in aspirin :
print ( Y )
for i in range ( Y ) :
if i == x :
continue
print ( AA [ 'name' ])
x += 1
def print_stock_amount ( stock ) :
if stock == 0 :
print ( "None" )
return
total_amount = float ( stock ) / 10.0
remaining_amount = stock - total_amount
return
result = \"\"
if int ( num ) <= int ( volume ):
total_volume = round ( int ( num ) / int ( volume ), 6 ) # this will be the input
m1 = int ( volume )
elif int ( num ) <= int ( total_volume ):
m1 = int ( num )
m2 = int ( volume )
print_stock_amount ( vol1 )
print_stock_amount ( vol2 )
print_stock_amount ( vol3 )
i = 0
for i in range ( len ( steps )):
i += 1
try :
if m1 > m2 :
volume = m2
else :
volume = m1
except :
print ( "Please enter number within measurement size." )
if m1 > m2 :
set_step = do_step if num >= m1 - m2 else \
do_step if num >= m1 else \
do_step ()
elif m2 > m1 :
set_step = do_step if num >= m1 - m2 else \
do_step if num >= m2 else \
do_step ()
else :
set_step = do_step ()
def run_experiment_with_cells ( cell_type ) :
ops_env = OpenTRONSEnvironment ( profile = 'Celdef Profile' ,
opentrons_version = '2.2.0' )
cell_culture_set1 = ops_env . acquire_segment ( \
'CellCulture_60ml_Dish_900ml_S_SC-300CS' , '1' )
cell_culture_set2 = ops_env . acquire_segment ( \
'CellCulture_60ml_Dish_900ml_S_SC-300CS' , '2' )
user_input_vals = ops_env . parse_input_variables ( \
'density,radius,volume' ,
{ 'density' : cell_type . ESSENTIAL_GRAMMES ,
'radius' : cell_type . ESSENTIAL_CENTIMETER ,
'volume' : cell_type . ESSENTIAL_CENTIMETER })
new_medium = ''
for e in cell_culture_set1 . wells ()[: 3 ]:
add_medium ( int ( str ( e [ "radius" ])), \
int ( str ( e [ "density" ])),
new_medium ,
int ( str ( e [ "volume" ])))
cell_type . drop_media ( 'DMEM' )
for e in cell_culture_set2 . wells ()[: 3 ]:
add_medium ( int ( str ( e [ "radius" ])), \
int ( str ( e [ "density" ])),
new_medium ,
int ( str ( e [ "volume" ])))
if int ( volume ) < 10 :
print_stock_amount ( vol1 )
print_stock_amount ( vol2 )
print_stock_amount ( vol3 )
cooling_medium = ''
for e in cell_culture_set2 . wells ()[: 3 ]:
add_medium ( int ( str ( e [ "radius" ])), \
int ( str ( e [ "density" ])),
cooling_medium ,
int ( str ( e [ "volume" ])))
edgex = 5
right = 40
left = 5
for step in steps [: 5 ]:
try_aw = int ( step [ "radius" ])
radius = int ( step [ "radius" ]) if try_aw < radius \
else try_aw
set_step_vol = int ( step [ "left_vol" ]) * 10 if try_aw < radius \
else int ( step [ "left_vol" ])
vol = int ( step [ "volume" ]) * 10 if try_aw < radius \
else int ( step [ "volume" ])
set_step_vol = vol if vol > set_step_vol \
else set_step_vol
m2 = int (( radius - try_aw ) / 3 ) + 1
m1 = int (( try_aw - radius ) / 3 ) + 1
fudge = 0
while not fudge and m1 > m2 :
if fudge :
yield set_step ()
def add_medium ( r , vol , new_medium , volume ) :
try :
t = r + vol

except ValueError :
t = r + vol1
x = opentrons_env . quan ( t , vol )
y = x / vol1
if x != y :
new_medium . append ( "=" * len (( '{}{} mL' . format ( t , y ))))
for m in new_medium :
if m :
print_stock_amount ( 10 )
def run_experiment_with_cells_wip = run_experiment ( run_experiment_with_cells ( "ATCC-30-2" ))
def run_experiment_without_cells ( cell_type ) :
ops_env = OpenTRONSEnvironment ( profile = 'Celdef Profile' ,
opentrons_version = '2.2.0' )
cell_culture_set = ops_env . acquire_segment ( \
'CellCulture_60ml_Dish_900ml_S_SC-300CS' , '1' )
user_input_vals = ops_env . parse_input_variables ( \
'density,radius,volume' ,
{ 'density' : cell_type . ESSENTIAL_GRAMMES ,
'radius' : cell_type . ESSENTIAL_CENTIMETER ,
'volume' : cell_type . ESSENTIAL_CENTIMETER })
new_medium = ''
for e in cell_culture_set . wells ()[: 3 ]:
add


:*************************


modulename = 'test_module_name'


def run(ctx):

"""
Function runs the opentrons experiment
"""
import pandas as pd, re

try:
import pprint
except ImportError:
pprint = None

def verify_setting(setting):
 """Function Verifies that the given setting is within a desired range. If not,
prints error message and exits"""
if setting < recommended_setting or setting > max_setting:
 msg = 'Enter value between %s and %s' % ( recommended_setting, max_setting )
 raise Exception( msg )


def prompt_user(question, title='', allow_short=False):
 """Prompts user for input with title, converts input to int, and
if converting to int with empty input returns what user entered"""
# let user enter a number, or skip question
while True:
try:
keyword = str(input(question+' [Yes/No] > '))
if allow_short:
if len(keyword) < 1:
raise Exception('Answer must be 1 or more characters')
if len(keyword) > 1:
keyword = keyword.lower()
if keyword == 'yes' or keyword == 'no':
break
except (KeyboardInterrupt):
raise Exception(
'Client exited before providing input')
except ValueError:
msg = 'Enter a number only (1 or 0) not "%s"' % keyword
raise Exception( msg )


def setup_variables(context):
 """
Functions prepare variables/objects for use in user functions
"""
# set default values
dry_sample_vol = 20
wet_sample_vol = 15
media_vol = 10
dry_tube_label = 'Dry Sample'
wet_tube_label = 'Wet Sample'
media_tube_label = 'Cell media'


def run_experiment(ts.values()):
 """
Functions runs the experiment using Step Functions"""
context = {}
reactants = [ctx.posedata.open_container(
name=dry_tube_label, ml_present=dry_sample_vol,
type='tuberrosa')]
reagents = [ctx.posedata.open_container(
name=wet_tube_label, ml_present=wet_sample_vol,
type='tuberrosa')]
miscs = [ctx.load_module(
'detek_modulenet', '2').load_module(
'detek_96_wellplate', '1').load_module(
'misc_200ul_tiprack_100', '4')]


steps = [
ts.step(
name_prefix='Step',
block=lambda _: run_experiment(ts.values()),
handlers=[
(key, value)
for key, value in
zip(
['Button A', 'Stop Experiment',
'Button B', 'Proceed to Next Step',
'Button C', 'Reject this Step',
''],
['Execute', 'Skip', 'Pause', 'Exit'][value])])]


function = ts.function(
'detek_create_plate',
order_by=['location', 'name'],
parent=miscs,
nested_functions=[verify_setting])
if context.key_pressed == 'code':
print(function.call_steps[0]['comment'])
ts_variables = context.load_module('opentrons', 'type33').variables()
remove_tube(by_name=ts_variables.get('media_location'))
v_media = ts.float_number(media_vol, precision=2)
remake_plate()
add_samples()
v_cells = ts.float_number(media_vol, precision=2)
pause_experiment(comment='Remove used media tube')
v_media = ts.float_number(media_vol, precision=2)
set_temperature(22)
platedata = ctx.load_module('dektacel_95_wellplate_1200ul', '3')
txnset = [col for col in platedata.columns()[:2] if col][:2]
txns = [txnset[:ts.input_number(int(v_cells),
required=True,
min=1,
max=3)]
for _ in range(ts.input_number(2,
min=1,
max=5))]


pause_experiment(comment='Final media addition')
if txns:
txn = txns[0]
else:
txn = []
for r in reagents:
remove_tube(by_name=r.name)
defer pause_experiment(comment='Return tubes')
if not txn:
defer pause_experiment(comment='Enter a tube name')
rxn = reagents.list.find(
name.startswith(txn.name))
if not rxn:
ts.comment('Enter a container name to relocate tube to')
raise Exception('No tube named %s found in experiment' % txn.name)
remake_plate()
wipe_dish(method='sponge', by_name={rxn.name})
rxn.location = txn.name
txn.location = ''
]


def perform_step(proc):
"""
Functions performs the Step of experiment, returns
variables of next step"""
step_data = {
'comment': 'Cell medium change',
'variables': [v_cells, v_media, txn
]
}
ts.comment(step_data['comment'])
prompt_user(['Add %s medium to the plate',
step_data['variables'][0]])
if len(ctx.loaded_modules) > 1 and step_data['variables'][2]:
result = ctx.loaded_modules[-1].evaluate(
lambda: verify_setting(str(step_data['variables'][2])),
comment=step_data['comment'])
if result:
raise Exception(result)
pause_experiment('Remove used media tube and waste')
if not txn:
ts.comment('Enter a tube name to relocate tube')
raise Exception('No tube named %s found in experiment' %
txn.location)
media = [r.vol() for r in media]
prompt_user([
'Add %s medium to the plate, starting with the first well',
step_data['variables'][0]])
dwell = ts.block(
to_pause_experiment,
pass_seconds=10)
repeat_adding = ts.while_condition(
lambda: ctx.loaded_modules.count(
lled_container.name.lower() == txn.name.lower()) > 0,
dwell=(seconds, dwell_max=10)
)
txn.set_location('media')
pause=pause_experiment('Discard tip, return to Experiment Module')
pause_experiment('Return tubes and wipe dishes')
for r in media:
pause(seconds=10)
tubes_in_position = int(re.search('(\d+)', r.name)[1])
# determine if at this step to repeat addition
last_tube_position = ctx.loaded_modules[-1].columns()[0][
length-1]
repeat_at = (length - (
len(tmp_.locations) - 1)) % length - 1
# repeat_tube_name = "Tubes added - ".join([s.name for s
in r.located_containers()[:int(pause_at)]])
# dup_tube = ctx.loaded_modules.loaded_object(dup_tube_name)


if (repeat_at > 1 and len(txn) > 0):
#if result:
# pause_at_txn = ts.input(
# check_missing=False,
# check_too_large=False,
# prompt='Where to place tube next


:*************************


