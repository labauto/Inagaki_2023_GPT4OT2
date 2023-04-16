metadata = {
    'protocolName': 'Medium Exchange',
    'author': 'Your Name',
    'description': 'Exchange medium in 6-well plate using Opentrons',
    'apiLevel': '2.9'
}
    
def run(ctx):

    # Load Protocol Steps
    tips = [ctx.load_labware('opentrons_96_tiprack_20ul', slot) for slot in ['1', '4']]
    medium_reservoir = ctx.load_labware("usascientific_6_reservoir_15mL", '2')
    pbs_reservoir = ctx.load_labware("usascientific_6_reservoir_15mL", '3')
    plate = ctx.load_labware("corning_6_wellplate_16.8ml_flat", '5')

    # Retrieve Pipettes
    p20 = ctx.load_instrument('p20_single_gen2', 'right', tip_racks=tips)

    # Transfer out used cell culture medium
    used_medium_well_xf = [(idx, idx) for idx in range(0,6)]
    p20.pick_up_tip(tips[0].well('A1'))
    for (source, dest) in used_medium_well_xf:
        p20.transfer(
            10,
            plate.wells(source).bottom().move(types.Point(x=0,y=0,z=-1.5)),
            medium_reservoir.wells(dest).bottom().move(types.Point(x=0,y=0,z=1)),
            new_tip='never'
        )
    p20.drop_tip()

    # Rinse cells once with 150ul PBS (-), adding PBS into the wells of culture plate.
    p20.pick_up_tip(tips[1].well('H1'))
    for i in range(0,6):
        p20.transfer(
            20,
            pbs_reservoir.wells(0),
            plate.wells(i),
            mix_before=(3, 10),
            new_tip='never'
        )

    # Remove the PBS
    for i in range(0,6):
        p20.transfer(
            20,
            plate.wells(i).bottom().move(types.Point(x=0, y=0, z=2)),
            pbs_reservoir.wells(0).bottom(),
            air_gap=2,
            new_tip='never'
        )
    p20.drop_tip()

    # Add new 100ul of culture medium
    medium_well_xf = [(idx+6, idx) for idx in range(0,6)]
    p20.pick_up_tip(tips[0].well('A1'))
    for (source, dest) in medium_well_xf:
        p20.transfer(
            10,
            medium_reservoir.wells(source).bottom(),
            plate.wells(dest).bottom().move(types.Point(x=0,y=0,z=-1.5)),
            new_tip='never'
        )
    p20.drop_tip()
