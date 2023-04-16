import opentrons.protocol_api as papi

metadata = {
    'protocolName': 'Cell culture medium exchange',
    'author': 'Your Name',
    'description': 'This protocol exchanges iPS cell culture medium using PBS(-) and SCM130',
    'apiLevel': '2.10'
}


def run(ctx: papi.ProtocolContext):

    # Load labware
    plate = ctx.load_labware('corning_6_wellplate_16.4ml_flat', 2)
    tiprack_200ul = ctx.load_labware('opentrons_96_tiprack_300ul', 4)

    # Load pipettes
    p300 = ctx.load_instrument('p300_single', 'left', tip_racks=[tiprack_200ul])

    # Tip counter and tip usage tracking
    tip_count = 0
    max_tip_count = len(tiprack_200ul.rows()[0]) * 12
    tip_log = {rack: [False for _ in range(12)] for rack in tiprack_200ul.rows()}

    def pick_up_tip():
        nonlocal tip_count

        if tip_count == max_tip_count:
            raise Exception("Ran out of tips!")

        for rack in tiprack_200ul.rows():
            if False in tip_log[rack]:
                next_tip = rack[tip_log[rack].index(False)]
                tip_log[rack][next_tip.index] = True
                p300.pick_up_tip(next_tip)
                tip_count += 1
                return

    def return_tip():
        nonlocal tip_count

        p300.return_tip()
        tip_count -= 1
        for rack in tiprack_200ul.rows():
            if p300.current_tip() in rack:
                tip_log[rack][p300.current_tip().index] = False
                return

    # Define liquids to use
    pbs = ctx.load_labware('nest_1_reservoir_195ml', 1).wells()[0]
    scm130 = ctx.load_labware('nest_1_reservoir_195ml', 1).wells()[1]

    # Protocol
    # Add 300ul of PBS to each well using a new tip
    pick_up_tip()
    for well in plate.wells():
        p300.aspirate(300, pbs)
        p300.dispense(300, well)
    return_tip()

    # Exchange medium with 200ul of scm130 twice
    for i in range(2):
        for well in plate.wells():
            # Discard 200ul of the existing medium
            p300.aspirate(200, well)
            p300.dispense(200, pbs)
            p300.aspirate(200, pbs)
            # Add 200ul of scm130
            p300.dispense(200, scm130)
        # Pause 2 hours for cells to grow in the new medium
        ctx.delay(minutes=120)
