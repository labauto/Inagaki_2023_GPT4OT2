from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name <your.name@example.com>',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.10'
}

def run(ctx: protocol_api.ProtocolContext):
    # Labware
    plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = ctx.load_labware('opentrons_96_tiprack_300ul', '4')

    # Pipettes
    p300 = ctx.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    # Reagents
    pbs_tube = ctx.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
    pbs = pbs_tube['A3']
    dmem_tube = ctx.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')
    dmem = dmem_tube['A1']

    # Change media
    p300.pick_up_tip()
    for well_idx in range(6):
        well = plate.wells()[well_idx]
        p300.aspirate(150, well)
        p300.dispense(150, pbs)
        for i in range(2):
            p300.mix(5, 200, pbs)
        p300.aspirate(150, pbs)
        p300.dispense(150, dmem)
        p300.blow_out()
    p300.drop_tip()
