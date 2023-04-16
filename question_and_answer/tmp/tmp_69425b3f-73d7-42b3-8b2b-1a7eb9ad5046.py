from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def wash_with_pbs(protocol):
    p1000 = protocol.load_instrument('p1000_single', 'left')
    p1000_tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 2)
    p1000.pick_up_tip(p1000_tips['A1'])
    
    pbs_tube = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    pbs = pbs_tube['A1']
    
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    for well in plate:
        for _ in range(5):
            p1000.aspirate(1000, pbs)
            p1000.dispense(1000, well)
            
    p1000.drop_tip()

def add_trypsin(protocol):
    p1000 = protocol.load_instrument('p1000_single', 'left')
    p1000_tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 2)
    p1000.pick_up_tip(p1000_tips['B1'])
    
    trypsin_tube = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    trypsin = trypsin_tube['A2']
    
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    for well in plate:
        p1000.aspirate(1000, trypsin)
        p1000.dispense(1000, well)
            
    p1000.drop_tip()

def add_dmem(protocol):
    p1000 = protocol.load_instrument('p1000_single', 'left')
    p1000_tips = protocol.load_labware('opentrons_96_tiprack_1000ul', 2)
    p1000.pick_up_tip(p1000_tips['C1'])
    
    dmem_tube = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    dmem = dmem_tube['A3']
    
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

    for well in plate:
        p1000.aspirate(1000, dmem)
        p1000.dispense(1000, well)
            
    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    wash_with_pbs(protocol)
    protocol.delay(minutes=5)
    add_trypsin(protocol)
    protocol.delay(minutes=5)
    add_dmem(protocol)
    protocol.comment("Experiment finished!")
