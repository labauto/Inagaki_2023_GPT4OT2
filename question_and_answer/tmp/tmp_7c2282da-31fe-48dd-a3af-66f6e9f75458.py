from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'iPSC Culture Medium Exchange',
    'author': 'Your Name Here',
    'description': 'Protocol to exchange iPSC culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # define pipettes
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', slot) for slot in ['5']])
    
    # define labware
    plate = protocol.load_labware('corning_6_wellplate_16.1ml_flat', '1')
    dmem_well = plate.wells_by_name()['A1']
    pbs_well = plate.wells_by_name()['A2']
    
    # define transfer volumes
    pbs_vol = 300
    dmem_vol = 200
    
    # exchange medium in wells
    for well in plate.wells()[2:]:
        p300.pick_up_tip()
        p300.aspirate(pbs_vol, pbs_well)
        p300.dispense(pbs_vol, well)
        p300.drop_tip()
        
        p300.pick_up_tip()
        p300.aspirate(dmem_vol, dmem_well)
        p300.dispense(dmem_vol, well)
        p300.blow_out()
        p300.drop_tip()
