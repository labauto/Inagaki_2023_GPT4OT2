from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostained hMSC cells visualization of lysosomes',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '2')

    # Pipettes
    pipette = protocol.load_instrument('p20_single_gen2', 'left')

    # Reagents
    antibody_solution = 'Aonexis stain Dilution 1'

    # Mixing reagents
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.mix(2, 20, well)
        pipette.aspirate(10, well.bottom(3))
        pipette.dispense(10, well)
        pipette.mix(4, 20, well)
        protocol.delay(seconds=10)
        pipette.aspirate(10, well.bottom(3))
        pipette.dispense(10, well)
        pipette.mix(4, 20, well)
        pipette.drop_tip()

    # Adding antibody solution
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.mix(2, 10, well)
        pipette.aspirate(8, well.bottom(1.5))
        pipette.dispense(8, well)
        pipette.aspirate(2, well.bottom(1.5))
        pipette.dispense(2, well)
        pipette.mix(4, 10, well)
        pipette.aspirate(4, well.bottom(1.5))
        pipette.dispense(4, well)
        pipette.drop_tip()

    protocol.comment('Incubating for 10 minutes at room temperature')

    # Removing antibody solution
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(20, well.bottom(1.5))
        pipette.drop_tip()

    # Washing with PBS
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(100, plate[well].bottom(1))
        pipette.dispense(150, plate[well].bottom(4))
        pipette.aspirate(150, plate[well].bottom(1))
        pipette.dispense(150, plate[well].bottom(4))
        pipette.aspirate(150, plate[well].bottom(1))
        pipette.dispense(150, plate[well].bottom(4))
        pipette.aspirate(150, plate[well].bottom(1))
        pipette.drop_tip()

    # Fixation with paraformaldehyde
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(250, plate[well].bottom(5))
        pipette.dispense(250, plate[well].bottom(3))
        pipette.aspirate(250, plate[well].bottom(5))
        pipette.dispense(250, plate[well].bottom(3))
        pipette.aspirate(250, plate[well].bottom(5))
        pipette.dispense(250, plate[well].bottom(3))
        pipette.drop_tip()

    protocol.comment('Fixating for 20 minutes at room temperature')

    # Removal of paraformaldehyde
    for well in plate.wells():
        pipette.pick_up_tip()
        pipette.aspirate(200, plate[well].bottom(4.5))
        pipette.drop_tip()
    
    protocol.comment('Sample ready for confocal microscopy')
