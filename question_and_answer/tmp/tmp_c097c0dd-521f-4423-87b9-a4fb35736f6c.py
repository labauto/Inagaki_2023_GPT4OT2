from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    p300_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2)
    pbs_reservoir = protocol.load_labware('nest_12_reservoir_15ml', 3, "PBS(-) reservoir")
    dmem_reservoir = protocol.load_labware('nest_12_reservoir_15ml', 4, "D-MEM reservoir")
    
    # Pipette
    p300_single = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[p300_tip_rack])

    # Reagent positions
    pbs = pbs_reservoir['A1']
    dmem = dmem_reservoir['A1']

    # Exchange medium
    for well in six_well_plate.wells():
        p300_single.pick_up_tip()
        p300_single.aspirate(300, well)
        p300_single.dispense(300, pbs.top())
        p300_single.drop_tip()

        p300_single.pick_up_tip()
        p300_single.aspirate(300, well)
        p300_single.dispense(300, pbs.top())
        p300_single.drop_tip()

        p300_single.pick_up_tip()
        p300_single.aspirate(300, pbs)
        p300_single.dispense(300, well)
        p300_single.drop_tip()

        p300_single.pick_up_tip()
        p300_single.aspirate(300, dmem)
        p300_single.dispense(300, well)
        p300_single.drop_tip()
