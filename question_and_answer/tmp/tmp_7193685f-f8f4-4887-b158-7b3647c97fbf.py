import opentrons as ot
from opentrons import protocol_api

metadata = {
    'protocolName': 'HMSC_Medium_Exchange',
    'description': 'Exchange hMSC Cell Culture Medium using PBS(-) and D-MEM',
    'author': 'USERNAME',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware setup
    tips_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    tips_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips_1000])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips_300])
    
    plate_6 = protocol.load_labware('nest_wellplate_6_reservoir_36ml_reduced_evaporation', '3')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml','4')
    
    # Reagent locations
    pbs_minus = reservoir.wells('A1')
    dmem = reservoir.wells('A2')
    
    # Pipetting logic
    for well in plate_6.wells():
        # Remove hMSC culture medium from each well.
        p1000.pick_up_tip()
        p1000.aspirate(900, well)
        p1000.dispense(900, pbs_minus)
        p1000.drop_tip()

        # Perform PBS(-) washing.
        p1000.pick_up_tip()
        p1000.aspirate(900, pbs_minus)
        p1000.dispense(900, well)
        p1000.drop_tip()

        # Mix the well by pipetting up and down with PBS(-).
        p300.pick_up_tip()
        p300.aspirate(250, well)
        p300.dispense(250, well)
        p300.mix(5, 250, well)
        p300.drop_tip()

        # Remove PBS(-) from the well.
        p1000.pick_up_tip()
        p1000.aspirate(900, well)
        p1000.dispense(900, pbs_minus)
        p1000.drop_tip()

        # Dispense fresh D-MEM into each well.
        p1000.pick_up_tip()
        p1000.aspirate(900, dmem)
        p1000.dispense(900, well)
        p1000.drop_tip()
