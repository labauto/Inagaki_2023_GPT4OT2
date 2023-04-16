metadata = {
    'protocolName': 'My Protocol',
    'author': 'Your Name',
    'description': 'A description of my protocol',
    'apiLevel': '2.10'
}

def run(protocol):
    # Load labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    trypsin = plate['A1']
    medium = plate['A2']

    # Load pipette
    pipette = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack])

    # Wash the plate with PBS(-)
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, well)
        pipette.dispense(1000, well)
        pipette.mix(5, 1000, well)
        pipette.drop_tip()

    # Add trypsin and wait
    pipette.pick_up_tip()
    pipette.transfer(1000, trypsin, plate.wells(), blow_out=True, new_tip='never')
    protocol.delay(minutes=5)
    pipette.drop_tip()

    # Add medium
    pipette.pick_up_tip()
    pipette.transfer(1000, medium, plate.wells(), blow_out=True, new_tip='always')
    pipette.drop_tip()
