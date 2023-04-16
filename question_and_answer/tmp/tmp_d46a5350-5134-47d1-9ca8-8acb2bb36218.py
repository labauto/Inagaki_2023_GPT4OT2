from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'hMSC cell culture medium exchange',
    'author': 'Your Name',
    'description': 'Automated medium exchange for hMSC cell culture plates'
}

# define protocol
def run(protocol: protocol_api.ProtocolContext):

    # load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # load pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tip_rack])

    # exchange medium with PBS(-) in every well
    for well_num in range(1, 7):
        # aspirate old medium
        pipette.aspirate(250, plate['A'+str(well_num)].bottom(2))
        protocol.delay(minutes=2)
        # dispense PBS(-)
        pipette.dispense(250, plate['A'+str(well_num)].bottom(2))
        protocol.delay(minutes=3)
        # aspirate PBS(-)
        pipette.aspirate(250, plate['A'+str(well_num)].bottom(2))
        protocol.delay(minutes=2)
        # dispense DMEM
        pipette.dispense(250, plate['A'+str(well_num)].bottom(2))
        protocol.delay(minutes=3)

    # finish protocol
    pipette.drop_tip()
