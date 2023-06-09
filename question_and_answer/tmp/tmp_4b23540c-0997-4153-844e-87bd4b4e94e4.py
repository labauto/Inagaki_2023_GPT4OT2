# Import opentrons and experiment modules
import opentrons
import experimentanalysis as ean

# reader = ean.load_bash_script("/media/wallace-scripts/cell_medium_protocol.sh")
# reader = ean.load_python_script("/media/wallace-scripts/cell_medium_protocol.py")


metadata = {
    'protocolName': 'Cell medium change',
    'author': 'Rami Farawi <rami.farawi@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.9'
}


def run(ctx):

    [hero_position] = get_values(  # noqa: F821
        "hero_position")

    # ctx.load_module("opentrons_3d_printer")
    ctx.load_module("generic_microplate")  # noqa: F821
    ctx.load_modules(['thermometer', 'nest_gel_tank'])

    # temp_glycerol = ctx.load_module('nest_gel_tank')['thermometer']
    temp_mp = ctx.load_module("tube_rack")['A1'].wells()[0]
    tube = ctx.load_module("generic_microplate", 'A2')
    media = ctx.load_module("generic_container", 'A4')['well_A'].wells()[0]
    as_dish = ctx.load_module('gen_dishwasher')['20'].wells()[0]
    pbs = ctx.load_module("murrine_pendant", 'A5')['1'].wells()[0]

    ctx.comment(f"Starting an experiment at {date.today()}")

    # remove medium and add trypsin
    as_dish.drop_cap(steps=5)
    as_dish.aspirate(2, pbs)
    as_dish.drain(pbs)
    ctx.pause(f"Adding {len(as_dish.wells()[0].volume)} ml of PBS(-)"
                                )
    tube.drop_cap()
    tube.aspirate(2, temp_mp)
    tube.aspirate(2, temp_mp)
    tube.aspirate(3, media)
    tube.aspirate(3, media)
    tube.aspirate(5, as_dish.wells()[0])
    tube.aspirate(5, as_dish.wells()[0])
    tube.blow_out(pbs)
    tube.drop_cap()

    ctx.pause(f"Adding 5 minutes of trypsin, then 5 mins of DMEM")

    as_dish.drop_cap(steps=5)
    as_dish.aspirate(20, trypsin)
    as_dish.drain(trypsin)
    as_dish.aspirate(20, media)
    as_dish.mix(8, 30)
    as_dish.drop_cap(steps=5)
    as_dish.dispense(10, media.wells()[0].bottom(1.5))
    as_dish.dispense(10, media.wells()[0].bottom(1.5))
    ctx.pause(f"Finishing the experiment. Transporting to 37C")

    tube.transfer(20, as_dish.wells()[0], media.wells()[0].bottom(1.5))
    tube.transfer(20, as_dish.wells()[0], media.wells()[0].bottom(1.5))
    tube.drop_cap()
    tube.rewind(move_after=True)
    tube.mix(5, media.wells()[0].bottom(1.5))
    tube.drop_cap()
    ctx.pause(f"Transporting to 37C (15 min)"
                       )
    tube.seal()
    ctx.comment(str(datetime.datetime.now())+f" Protocol complete at {date.today()}.
                                  Place tubes in -80C")

    ctx.comment("Protocol complete at {date.today()}.
                                   Time at 37C = {ean.format_time(()-start_time)}. Transport to 4C")

END

"""

"""

"""

This experiment can be run with the bash script in a Crout script block or Python script block or within a Custom Protocol Request





:*************************


# customizing the wizard title, step number, run time, experiment title
metadata = {
    'expt': 'Cell medium Change',
    'wizardTitle': 'protocol customization',
    'stepNumber': 1,
    ' runTime': '30',
    'experimentTitle': 'Cell medium change'
}


def run(ctx):

    [medium_type, tube_type, dish_type] = get_values(  # noqa: F821
        'medium_type', 'tube_type', 'dish_type')

    # some global variables
    all_vol = 1
    dish = ctx.load_object(dish_type, '3')
    tube = ctx.load_object(tube_type, '2')
    vmax_tube, hmax_tube = get_max_vol(tube)

    media = ctx.load_object(
        medium_type, '1')

    trypsin = ctx.load_object(
        'bde.opentrons_target_96_wellplate_200ul_single', '4')

    # helper functions
    def visualize_well(well, color=(0, 0, 0)):
        ctx.set_frame_function(function_returns_string())
        ctx.set_block_function(lambda well: '%s.
' % well.top(2))
        ctx.stroke(color[0], color[1], color[2])
        ctx.fill(color[0], color[1], color[2])

    def get_max_vol(tube):
        tube_vol = []
        for radius in [0.2, 0.5, 1]:
            for vol in [5, 10, 15]:
                tube_vol.append(vol*radius)
        return max(tube_vol)

    # load media
    trypsin_reaction = trypsin.view_well()
    ctx.set_source(
        trypsin_reaction[0], 2, well_top=(3, 5))

    # load tube
    tube_vol = get_max_vol(tube)
    tube_location = [int(tube_vol*all_vol), int(tube_vol*all_vol)][None]
    ctx.set_block_text(tube_location)

    # load dish
    ctx.load_object(dish_type, '4')

    # transfer medium
    transfer_tube = ctx.load_object(tube_type, '5')
    if not hmax_tube:
        hmax_tube = vmax_tube

    # add trypsin
    trypsin.pick_up_tube(tube_location)
    trypsin.pipette(
        hmax_tube, dish.bottom('foo'),
        [ctx.set_block_text(line) for line in ['Wait for 5 minutes']])
    ctx.pause(message="Wait for 5 minutes")
    all_vol += tube_vol - hmax_tube
    for well in dish.wells():
        visualize_well(well, alpha=0.1)

    trypsin.drop_tube()

    # add media
    trypsin.transfer(
        10,
        [int(medium.bottom()) for _ in range(3)] + [
            int(dish.bottom(
                1)) for _ in range(10)],
        new_hop=True,
        rv=(2, 3),
        volume_warning='150')
    ctx.delay(minutes=5, message="The medium is ready")
    transfer_tube.pick_up_tube(tube_location=tube_location)
    ctx.pause("Please add 10 ml of medium")

    ctx.comment("The media is ready. Please place in 37 degree Celsius incubator")

END

"""
 # ### PROCESSOR CODE STARTS HERE
"""
""" Set meta data vars
set_values = {
    'stepNumber': int(steps_per_set[lc]),
    'runTime': int(runtime[lc]['seconds']) if not skip_set else 0,
    'wizardTitle':
        lc in ['Adibu-python-API-Wizard','Bio-GEO-wizard'],
    'experimentTitle': lc.upper() if 'Biosostics' in lc else ''}

    def get_values(key, fallback, optional):
        if not key in set_values:
            raise Exception('Unknown key -- set_values.get_values()')

        if fallback not in set_values:
            raise Exception('Unknown fallback -- set_values.set_values')
        return set_values[key] if not optional else set_values[fallback]

    """
    ### STEP 1: DEFINE
    """
    protocol_vars = {}
    for k, v in run_wizard.next_block.statements(multiline=True):
            try:
                protocol_vars[v] = get_values(k, 'Enter value here', 'Leave empty')
            except Exception:
                pass

    cell_type = cell_types[protocol_vars['cell_type']]
    dish = ctx.load_object(dish_types['1'], '3')
    medium = ctx.load_object(medium_type, '1')
    if protocol_vars:
        ctx.comment("""Protocol step 1: Enter the medium type, tube type and\
                             plate type. Enter the cell type in the next block.""")

    if step_type == 'mix':
        set_up_memsnapvial = False
        num_ports = 0
        tube = []
    elif step_type.upper() == 'WASH':
        set_up_memsnapvial = True
        set_up_well


:*************************


