from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Your Name Here',
    'description': 'Protocol for exchanging hMSC cell culture medium with PBS(-) and D-MEM.',
    'apiLevel': '2.0'
}

def run(ctx: protocol_api.ProtocolContext):

    # Labware
    plate = ctx.load_labware('corning_6_wellplate_16.8_ml_flat', '1')

    tiprack_1 = ctx.load_labware('opentrons_96_tiprack_20ul', '2')
    tiprack_2 = ctx.load_labware('opentrons_96_tiprack_300ul', '3')

    # Instruments
    p20_single = ctx.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_1])
    p300_multi = ctx.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_2])

    # Reagents
    dmem = ctx.load_labware('cobra_12_reservoir_300ml', '4')['A1']
    pbs = ctx.load_labware('cobra_12_reservoir_300ml', '4')['A2']
    waste = ctx.load_labware('agilent_1_reservoir_290ml', '5')['A1']

    # Changing medium
    p300_multi.pick_up_tip()
    for col in plate.columns_by_name():
        p300_multi.aspirate(150, col[0])
        p300_multi.dispense(150, waste)
        p300_multi.drop_tip()
        p300_multi.pick_up_tip()
        
        pbs_loc = plate.columns_by_name()[col][0].bottom().move(
                types.Point(x=0, y=0, z=5))
        p20_single.pick_up_tip()
        p20_single.aspirate(5, pbs)
        p20_single.air_gap(5)
        p20_single.dispense(pbs_loc)
        p20_single.mix(1, 20, pbs_loc)
        p20_single.drop_tip()

        p300_multi.aspirate(150, plate.columns_by_name()[col][0])
        p300_multi.dispense(150, waste)
        p300_multi.aspirate(150, pbs_loc)
        p300_multi.dispense(150, plate.columns_by_name()[col][0])
                
        p20_single.pick_up_tip()
        dmem_loc = plate.columns_by_name()[col][0].bottom().move(
                types.Point(x=0, y=0, z=5))
        p20_single.aspirate(165, dmem)
        p20_single.air_gap(5)
        p20_single.dispense(dmem_loc)
        p20_single.mix(1, 20, dmem_loc)
        p20_single.drop_tip()
        
        p300_multi.pick_up_tip()
        p300_multi.aspirate(150, plate.columns_by_name()[col][0])
        p300_multi.dispense(150, waste)
        p300_multi.aspirate(150, dmem_loc)
        p300_multi.dispense(150, plate.columns_by_name()[col][0])
        p300_multi.drop_tip()
        
    ctx.comment('Protocol complete!')
