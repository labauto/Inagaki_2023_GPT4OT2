# -*- coding: utf-8 -*-

#
# Greets fellow opentronsian and author:
# Albert Wang <wangyan.wang@gmail.com>
# Date: 2019年1月
#
# Description: Cell medium change
#
import opentrons
mp="DatasetMaster"


def run_script(ctx):

"""
Your Python code goes here

"""
try:
# get cm11
c11=ctx.load_geometry(mp+"_1_111",
pos=vector2d(.14, .85),
name="Cell culture 11")
except Exception as ex:
print(ex)
except KeyError as ex:
print(ex)
v=20
L1=1
t=5
try:
v=int(v)
except Exception as ex:
print(ex)


try:
t=int(t)
except Exception as ex:
print(ex)
vals=[2, 3, 20]# resample of previous sizes in mm^3
for v in vals:
d=ctx.load_geometry(mp+"_50ml_dispenser",
position=(2, 3, v))
d.front.distribute(
(vals[len(vals)-1][2]*5,
vals[len(vals)-1][3]*5,
vals[len(vals)-1][v]*5),
discards=True)
reps=(2, 3, 20)# resample of previous sizes in ml^3
for rep in reps:
d2=ctx.load_geometry(mp+"_90mm_cell_culture_plate",
position=(15, 31, rep))
d1=ctx.load_geometry(mp+"_90mm_cell_culture_plate",
position=(15, 31, rep+1))
newD1=d1.reparent(d2, corner_radius='touch')
newD1.bottom.stir(speed=10)
cm1=d1
cm2=d2
cm3=d1.translate((v+20, 0, 0))
t1=float(cm3.volume())
setval(cm1, t1-(t*24), t1-(t*48), exps=cyan.EXPR_operators.mod(t1, 24))
setval(cm2, t1-(t*48), t1-(t*48), exps=cyan.EXPR_operators.mod(t1, 48))
setval(cm3, t1-(t*48), t1-(t*48), exp=(t1*72))
names=[rep+" media", rep+" trypsin", rep+" DMEM"]
for val in names:
d21=ctx.load_geometry(mp+"_50ml_dispenser",
position=(3, 3, val))
d21.front.distribute(
(vals[len(vals)-1][0]*11,
vals[len(vals)-1][1]*11,
vals[len(vals)-1][val]*11),
discards=True)
elems=list(names)
d21.finish()
d1.front.reset_ hydrostatic_ balance()
fittings=set(['blowout', 'Nickman 121', '2x 7', '3'])
types=list(fittings.keys())
for f, t in zip(fittings, types):
d21=ctx.load_geometries(mp+"_50ml_dispenser",
os.path.split(mp)[0]+f+"_50ml_dispenser")
d1.front.fit_filter(f, t)
d21.finish()
elif f.upper() == "CAPPUCCINO SUPPORT":
d1.front.remove_filter()
d11=ctx.load_geometry(mp+"_11_cell_culture_dish",
position=(0, 0, "M11")).front()
cells11=d11.accept_objects(type="CellFinder11.CellMarkerBT-11",
radius=21)
if (not cells11) or (not len(cells11)) == 0:
error=missed_cells(11)*"`Note: The cells have been moved\
to the media dispenser."
print(error)
elif len(cells11) < 2:
error=low_cells(11)
print(error)
else:
whole11=[ctx.load_geometry(mp+"_100ml_cb_boat",
position=cell.geom.bounding_box) for cell in cells11]
d21=ctx.load_geometry(mp+"_50ml_dispenser",
position=(3, 3, 11))
# Add trypsin to beaker
trypsin11=d21.load_media(temp_min=-20,
name="Trypsin")
trypsin11.set_property("boillines"='none')
d11.front.include(whole11,
d1.front.pick_up_ objects(val_type=trypsin11))
for switch in d1.switches():
switch.state_tickets.resolve();
d11.bottom.distribute(
[(0.11*12,
mirror=True),
(0.11*12,
mirror=False),
(0.11*12,
mirror=False)],
discards=True)
trypsin11.reset_next_in_(d11)
setval(d21, 0.27*6, 0.27*6, exp=(0.27*6*60))
for switch in d1.switches():
switch.state_tickets.resolve();
delay11=ctx.load_geometry(mp+"_50ml_dispenser",
position=(27, 3, 11))
delay11.front.remove_filter()
for x in range(3):
delay11.bottom.distribute(
(1*12,
mirror=True),
(1*12,
mirror=False),
(1*12,
mirror=False))
delay11.bottom.lift(60)
delay11.finish()
d1.move(axes=['y', 'front'],
_avoid_sets=set(['z', 'move_apart'])*set(['z', 'move_together'])*set(['front', 'move_together'])*
_pause=(v, rep+1)*60*1,
name="`Moving the media to the media dispenser'"+"`."
d1.set_location(dict(x=3, y=5, z=20))
e=["Media", "Debris", "Media", "Trypsin", "Media"]
elems=set(e)
for name in elems:
cell=set(cell.shape()[len(elems)-1]
for cell in c11.cells()).intersection(set(elems))
if len(cell) > 3:
print("WARNING: "+name+" has over 3 colors")
delay11=ctx.load_geometry(mp+"_50ml_dispenser",
position=(27, 3, name))
delay11.front.remove_filter()
delay11.bottom.distribute(
(1*12,
mirror=True),
(1*12,
mirror=False),
(1*12,
mirror=False))
delay11.bottom.lift(60)
delay11.finish()
d1.move(axes=['y', 'front'],
_pause=(v, rep+1)*60*1,
name="`Moving the media to the media dispenser'"+"`."
d1.set_location(dict(x=3, y=5, z=20))
bck=ctx.load_geometry(mp+"_


:*************************


"""https://raw.githubusercontent.com/opentrons/opentrons_api/master/examples/python/cell_medium_change.py
"""
import subprocess
from opentrons import types

metadata = """
Description: Cell medium change
Requires: Three O-TRON modules
Optionally takes in a parameter named 'show_console', set to "false" (default) to
disable printing a prefix before lines in the script and ending it with ">>>"
"""
UP_SE = types.ModuleType.from_type(types.ModuleType.UP_SE)
UP_MM = types.ModuleType.from_type(types.ModuleType.UP_MM)
UP_HL = types.ModuleType.from_type(types.ModuleType.UP_HL)

def run_in_tenntent(): 
 def run_message(message, level="info"):
 def shell_check(name, pwd, cwd, print_message):
 if pwd == cwd:
 if name == "":"" and "export TERM=xterm" in cwd:
 elif name == "":
 elif name:
 subprocess.check_call(["xterm", "-title", "Python run", "-e",
"print(\"Welcome to the OPENTrons Python run${name}\")"
],"xterm")
if print_message:
 for line in message.splitlines():
 print line, """END"""
_ = run_message
def set_mesh(driver, motor_name, num_motors, dimensions, ply):
 """
Transforms the dimensions of a mesh to be compatible with a different
size/type of robot's robot module
"""
['xmin', 'ymin', 'zmin'] = [
float(re.search(r".*\d.*", v)
 if v else None
 for r in re.findall(r"\d.*")
 if v is None
 if v
)

for v in dimensions

]
z_len = elif ply == "fiber" else float(":")
motor_center = float(round(
(dim / float(motor_name)) * z_len
if ply == "manual"

)
for dim in dimensions[2:4]
if ply == "fiber"
if ply == "manual"
)
new_dimensions = [
float(a[:2] if len(a) > 2 else a[1:]),
float(a[:2] if len(a) > 2 else a[1:]),
float(a[:2] if len(a) > 2 else a[1:]),
]
N = {}
for i, meas in enumerate(new_dimensions):
N[i+3] = int(round(meas)) if meas else int(round(
(meas / float(motor_center)) * int(motor_center)
if ply == "manual"
)
for meas in new_dimensions
if ply == "manual"
)
return N
def run_cython(mm, cython_fn):
 """
A helper function to run Cython files
"""
try:
 mm.stops()
 the_mod = mm.modules.next()
 if isinstance(the_mod, UP_MM):
 cython_fn = (the_mod.name + ".pyx")
 if isinstance(the_mod, UP_HL):
 cython_fn = (the_mod.name + ".pyx_helper")
 mm.pause(seconds=1.0)
 mm.sets([0, y,
1, z, 0,
2, 0, 3, 0,
4, 0, 5, 0,
6, 0, 0, 0,
7, 8, 0, 0,
12, 0, 0, 0,
29, 0, 0, 0,
37, 0, 0, 0,
38, 0, 0, 0,
]])
 mm.move_arm(
"arm_0",
{'set_origin_for_type': 'modulenear',
'grippertype': 'opteron_1'})
 f = cymodule(cython_fn, mm)
 mm.pause(seconds=2.0)
 mm.sets([0, y,
1, z, 0,
2, 0, 3, 0,
4, 0, 5, 0,
6, 0, 0, 0,
7, 0, 8, 0,
12, 0, 0, 0,
29, 0, 0, 0,
37, 0, 0, 0,
38, 0, 0, 0,
]])
 f()
 except Exception as ex:
 logging.debug(ex)
def run_python(mm, steps, show_console=False):
 """
A helper function for running an experiment
"""
def run_in_tenntent():
 if show_console:
 run_message(
"""Welcome to the OPENTrons Python run{steps[:2].capitalize()}\""")
 set_mesh(mm, 'motor_center', mm.modules.next().motor.num,
 steps[3:8][1:])
 mm.pause(seconds=3)
 mm.set_pose([
type(mm.links.arm_center_link(name='a2').length*mm.radius
for radius in steps[18:20]
])
)
 mm.move_arm(
"arm_0",
{'set_origin_for_type': 'modulenear',
'grippertype': 'opteron_1'})
 f = mm.modules.next().function(
steps[:-2]
)()
 mm.sets([0, y,
1, z, 0,
2, 0, 3, 0,
4, 0, 5, 0,
6, 0, 0, 0,
7, 0, 8, 0,
12, 0, 0, 0,
29, 0, 0, 0,
37, 0, 0, 0,
38, 0, 0, 0,
]])
 mm.pause(seconds=1)
 mm.sets([0, y,
1, z, 0,
2, 0, 3, 0,
4, 0, 5, 0,
6, 0, 0, 0,
7, 0, 8, 0,
12, 0, 0, 0,
29, 0, 0, 0,
37, 0, 0, 0,
38, 0, 0, 0,
]])
 f()

mm = UP_MM(mount_points={'bottom': 'slots_perp_bottom'})
 steps = [
"""
\r"""
"""
"""]*2 + ['']
set_te = types.ModuleType(
'''.
import opentrons.hardware.cython.module as ctRow
import types

ROOTS = """
rot_matrix_params = [
list(row) for row in ctRow.rot_matrix(
rot_hz=0.5,
piv_to=-1.5,
piv_from=-1.5,
roll_centers=())]

SPRING_MOTION_RANGE = 7
"""
r"""
"""
t"""
"""
where = types.Struct(
'
cyl_height: float,
ring_radius: float,
travel_speed: float,
spring_friction_coefficient: float,
is_variable_spring_travel: bool
)
"""
def cython(mm, cython_fn,
syntax="line_length 100",
ext_values={}):
 """
A helper function to run Cython files
"""

try:
 mm.stops()
 the_mod = mm.modules.next()
 if isinstance(the_mod, UP_MM):
 cython_fn = (the_mod.name + ".pyx")
 mm.pause( seconds=2 )
 mm.sets ([0, y,


:*************************


