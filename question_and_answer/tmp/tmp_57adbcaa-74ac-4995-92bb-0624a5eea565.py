from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Immunostained hMSC Cells',
    'author': 'Your Name',
    'description': 'Protocol to prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.0'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # load tiprack
    tiprack = protocol.load_labware('opentrons_96_tiprack_10ul', '2')

    # load pipette
    pipette = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack])

    # define sample locations and volumes
    samples = {
        'A1': 2,
        'A2': 2,
        'A3': 2,
        'A4': 2,
        'A5': 2,
        'A6': 2
    }
    
    # distribute antibodies
    pipette.pick_up_tip()
    for well, vol in samples.items():
        pipette.aspirate(vol, source=plate[well])
        pipette.dispense(vol, plate[well])
    pipette.drop_tip()
    
    # incubate
    protocol.delay(minutes=30)
    
    # wash cells
    pipette.pick_up_tip()
    for well in samples.keys():
        pipette.aspirate(6, source=plate[well])
        pipette.dispense(6, protocol.load_labware('nest_12_reservoir_15ml').wells()[0])
    pipette.drop_tip()
    
    # visualize lysosomes
    pipette.pick_up_tip()
    for well in samples.keys():
        pipette.aspirate(2, source=plate[well])
        pipette.dispense(2, plate[well])
    pipette.drop_tip()
