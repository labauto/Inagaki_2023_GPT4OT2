# Import modules
from opentrons import protocol_api

# Metadata
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'hMSC spheroids experiment',
    'author': 'Your Name',
    'description': 'Create hMSC spheroids in 96-well plate using Opentrons',
    'source': ''
}

# Protocol run function
def run(protocol: protocol_api.ProtocolContext):
  
    # Load Labware
    dmem_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1, 'DMEM Plate')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 2, 'OS- Plate')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 3, 'OS+ Plate')
  
    # Load Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_200ul', 5)])
  
    # Transfer DMEM medium to each well of the "OS-" plate
    for well in os_minus_plate.wells():
        p300.transfer(100, dmem_plate.wells()[0], well, mix_before=(3, 100), new_tip='always')
  
    # Transfer DMEM + osteoinduction supplements to each well of the "OS+" plate
    for well in os_plus_plate.wells():
        p300.pick_up_tip()
        p300.transfer(100, dmem_plate.wells()[0], well, mix_before=(3, 100), new_tip='never')
        p300.transfer(0.1, protocol.load_labware('opentrons_96_wellplate_100ul', 4).rows()[0][0], well, new_tip='never')
        p300.transfer(1, protocol.load_labware('opentrons_96_wellplate_100ul', 4).rows()[0][1], well, new_tip='never')
        p300.transfer(1, protocol.load_labware('opentrons_96_wellplate_100ul', 4).rows()[0][2], well, new_tip='never')
        p300.drop_tip()
  
    # Transfer hMSC cells to each well of both plates
    for well in os_minus_plate.wells() + os_plus_plate.wells():
        p300.transfer(100, protocol.load_labware('corning_96_wellplate_360ul_flat', 6).wells()[0], well, mix_before=(3, 100), new_tip='always')

    # End of protocol
