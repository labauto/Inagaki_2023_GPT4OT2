from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'hMSC cell culture medium exchange',
    'author': 'Your Name',
    'description': 'Opentrons robot script for hMSC cell culture medium exchange in a 6-well plate',
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware and pipettes
    try:
        tiprack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', '1')
    except FileNotFoundError:
        tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    plate_6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    pipette = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_200])

    # Reagents and wells
    pbs_minus = reservoir.wells_by_name()['A1']
    d_mem = reservoir.wells_by_name()['A2']

    # Perform medium exchange
    for well in plate_6well.wells():
        pipette.pick_up_tip()
        pipette.transfer(300, well, pbs_minus, mix_after=(3, 300))
        pipette.blow_out(pbs_minus.top())
        pipette.aspirate(200, pbs_minus)
        pipette.drop_tip()

        pipette.pick_up_tip()
        pipette.transfer(300, well, d_mem, mix_after=(3, 300))
        pipette.blow_out(d_mem.top())
        pipette.aspirate(200, d_mem)
        pipette.drop_tip()
