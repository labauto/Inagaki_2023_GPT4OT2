# Import Opentrons Library and define protocol
from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your Name',
    'description': 'Automated hMSC spheroid culture using Opentrons',
    'apiLevel': '2.2'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define deck placement for 6-well plate, 96-well plate, and tip rack
    wellplate_6 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    wellplate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '6')

    # Define pipette and its volume range
    pipette = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack_200])
    pipette.flow_rate.aspirate = 150
    pipette.flow_rate.dispense = 300
    pipette.flow_rate.blow_out = 300
    pipette.volume = 100

    # Define source and destination wells for medium, hMSC, and supplements
    medium_src = wellplate_6['A1']
    hMSC_src = wellplate_6['B1']
    medium_dest_os_minus = wellplate_96.rows()[0]
    medium_dest_os_plus = wellplate_96.rows()[1]
    supplement_dest = wellplate_96.rows()[1][:3]

    # Start transfer of medium and supplements
    pipette.pick_up_tip()

    # Transfer medium to OS- wells
    for row in medium_dest_os_minus:
        pipette.aspirate(100, medium_src)
        pipette.dispense(100, row)
        pipette.blow_out()

    # Transfer medium to OS+ wells and add supplements
    for row in medium_dest_os_plus:
        pipette.aspirate(100, medium_src)
        pipette.dispense(100, row)
        pipette.blow_out()

        # Add supplements to OS+ wells
        for supplement in supplement_dest:
            pipette.aspirate(1, supplement)
            pipette.dispense(1, row)
            pipette.blow_out()

    # Transfer hMSC cells to OS- and OS+ wells
    for row in medium_dest_os_minus + medium_dest_os_plus:
        pipette.aspirate(100, hMSC_src)
        pipette.dispense(100, row)
        pipette.blow_out()

    # End of the protocol
    pipette.drop_tip()
