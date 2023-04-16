from opentrons import protocol_api

metadata = {
    'protocolName': 'iPS cell culture medium exchange',
    'author': 'Your Name',
    'description': 'Exchanging iPS cell culture medium using PBS(-) and D-MEM',
    'apiLevel': '2.3'
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Define the labware
    plates = [protocol.load_labware('corning_6_wellplate_16.8ml_flat', slot)
              for slot in ['1', '2', '3']]
    pbs = protocol.load_labware('opentrons_96_tiprack_10ul', '4')
    dmem = protocol.load_labware('opentrons_96_tiprack_300ul', '5')

    # Define the pipettes
    p10 = protocol.load_instrument('p10_single', 'left', tip_racks=[pbs])
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[dmem])

    # Perform the medium exchange
    for plate in plates:
        for well in plate.wells():
            # Aspirate 10 uL of medium from the well using p10
            p10.pick_up_tip()
            p10.aspirate(10, well.bottom(1))
            p10.drop_tip()
            
            # Dispense 10 uL of PBS into the well using p10
            p10.pick_up_tip()
            p10.dispense(10, well.bottom(1))
            p10.drop_tip()
            
            # Repeat aspirate and dispense steps for D-MEM
            p300.pick_up_tip()
            p300.aspirate(300, well.bottom(1))
            p300.drop_tip()
            
            p300.pick_up_tip()
            p300.dispense(300, well.bottom(1))
            p300.drop_tip()
            
    # End the protocol
    protocol.comment('Experiment complete!')
