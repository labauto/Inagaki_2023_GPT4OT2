from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Make hMSC spheroids with different conditions in 96 well plates',
    'author': 'Name <email@example.com>',
    'description': 'Make hMSC spheroids with different conditions in 96 well plates',
    'apiLevel': '2.10'
}

# Protocol run function. The argument 'ctx' stands for the context
def run(ctx: protocol_api.ProtocolContext):
    
    # Labware
    os_minus_plate = ctx.load_labware('corning_96_wellplate_360ul_flat', '1')
    os_plus_plate = ctx.load_labware('corning_96_wellplate_360ul_flat', '2')
    source_plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '4')
    tiprack_300 = ctx.load_labware('opentrons_96_tiprack_300ul', '7')

    # Pipettes
    p300 = ctx.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])
    
    # Step 1
    def step1():
        os_minus_wells = [well for well in os_minus_plate.wells() if not well.has_tip]
        os_minus_dests = os_minus_wells[:96]
        p300.distribute(100, source_plate.wells()[0], os_minus_dests)
        
    # Step 2
    def step2():
        os_plus_wells = [well for well in os_plus_plate.wells() if not well.has_tip]
        os_plus_dests = os_plus_wells[:96]
        p300.distribute(100, source_plate.wells()[1], os_plus_dests)

    # Step 3
    def step3():
        os_plus_wells = [well for well in os_plus_plate.wells() if not well.has_tip]
        os_plus_dests = os_plus_wells[:96]
        p300.distribute(
            0.1,
            source_plate.wells()[2],
            os_plus_dests,
            mix_before=(3, 100),
            disposal_volume=0
        )
        p300.distribute(
            1,
            source_plate.wells()[3],
            os_plus_dests,
            mix_before=(3, 100),
            disposal_volume=0
        )
        p300.distribute(
            1,
            source_plate.wells()[4],
            os_plus_dests,
            mix_before=(3, 100),
            disposal_volume=0
        )

    # Step 4
    def step4():
        os_minus_wells = [well for well in os_minus_plate.wells() if not well.has_tip]
        os_minus_dests = os_minus_wells[:96]
        p300.distribute(100, source_plate.wells()[0], os_minus_dests)

    # Step 5
    def step5():
        os_plus_wells = [well for well in os_plus_plate.wells() if not well.has_tip]
        os_plus_dests = os_plus_wells[:96]
        p300.distribute(100, source_plate.wells()[0], os_plus_dests)

    # Run the protocol by calling each step function
    step1()
    step2()
    step3()
    step4()
    step5()

