from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Exchange hMSC Cell Culture Medium'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    pbs = protocol.load_labware('nest_12_reservoir_15ml', '2')
    d_mem = protocol.load_labware('nest_12_reservoir_15ml', '3')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipette
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Protocol
    for well in plate.wells():
        # Exchange medium with PBS(-)
        p1000.pick_up_tip()
        p1000.aspirate(1000, pbs['A1'])
        p1000.dispense(1000, well)
        p1000.aspirate(1000, well)
        p1000.dispense(1000, pbs['A1'])
        p1000.drop_tip()

        # Exchange medium with D-MEM
        p1000.pick_up_tip()
        p1000.aspirate(1000, d_mem['A1'])
        p1000.dispense(1000, well)
        p1000.aspirate(1000, well)
        p1000.dispense(1000, d_mem['A1'])
        p1000.drop_tip()
