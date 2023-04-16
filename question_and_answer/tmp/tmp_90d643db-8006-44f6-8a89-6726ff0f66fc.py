import opentrons.protocol_api as protocol_api

metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):

    #load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')

    #load pipette
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[tiprack])

    #wash 6 well plate
    for i in range(6):
        p1000.pick_up_tip()
        p1000.aspirate(1000, plate['A'+str(i+1)])
        for j in range(5):
            p1000.dispense(1000, plate['A'+str(i+1)])
            p1000.aspirate(1000, plate['A'+str(i+1)])
        p1000.drop_tip()

    #add trypsin solution to the 6 well plate and wait
    for i in range(6):
        p1000.pick_up_tip()
        p1000.aspirate(1000, plate['A'+str(i+1)])
        p1000.dispense(1000, "your trypsin solution location in labware")
        protocol.delay(minutes=5)
        p1000.drop_tip()

    #add 1 mL of cell culture medium to the 6 well plate
    for i in range(6):
        p1000.pick_up_tip()
        p1000.aspirate(1000, "your cell culture medium location in labware")
        p1000.dispense(1000, plate['A'+str(i+1)])
        p1000.drop_tip()
