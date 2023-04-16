import opentrons.protocol_api as api

metadata = {
    'apiLevel': '2.0',
    'author': 'Your Name',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes in a 6 well plate.'
}

def run(protocol: api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_1,tiprack_2])

    # Reagents
    pbs = protocol.load_labware('usascientific_12_reservoir_22ml', '4') # slot name may differ

    # Commands
    # Resuspend cells
    p300.pick_up_tip()
    p300.aspirate(250, pbs['A1'])
    p300.dispense(250, plate['A1'])
    p300.mix(10, 200, plate['A1'])
    p300.drop_tip()

    # Fix cells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs['A2'])
        p300.dispense(100, well)
        p300.mix(10, 200, well)
        p300.drop_tip()

    # Permeabilize cells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs['A3'])
        p300.dispense(100, well)
        p300.mix(10, 200, well)
        p300.drop_tip()

    # Block cells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs['A4'])
        p300.dispense(100, well)
        p300.mix(10, 200, well)
        p300.drop_tip()

    # Stain cells for Lysosomes
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs['A5'])
        p300.dispense(100, well)
        p300.mix(10, 200, well)
        p300.drop_tip()

    # Wash cells
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(100, pbs['A6'])
        p300.dispense(100, well)
        p300.mix(10, 200, well)
        p300.drop_tip()
