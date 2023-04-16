# Import the Opentrons module and define our protocol
from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining Protocol',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained hMSC cells for visualization of lysosomes',
    'source': 'GitHub',
    'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):

    # Define our labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    pbs = protocol.load_labware('nest_1.5ml_snap_cap_tube', '3')
    cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')
    antibody_1 = pbs.columns()[0][0]
    antibody_2 = pbs.columns()[1][0]
    antibody_3 = pbs.columns()[2][0]

    # Define our pipettes
    pipette_300 = protocol.load_instrument('p300_multi_gen2', 'left')

    # Start the experiment

    # Add 200 uL of PBS to each well of the 6-well plate
    for well_index in range(6):
        pipette_300.pick_up_tip(tiprack_300.wells()[well_index])
        pipette_300.aspirate(200, pbs)
        pipette_300.dispense(200, cell_plate.wells()[well_index])
        pipette_300.drop_tip()

    # Add primary antibody to each well of the 6-well plate and incubate
    for well_index in range(6):
        pipette_300.pick_up_tip(tiprack_300.wells()[well_index])
        pipette_300.aspirate(50, antibody_1)
        pipette_300.dispense(50, cell_plate.wells()[well_index])
        pipette_300.mix(3, 100, cell_plate.wells()[well_index])
        pipette_300.incubate(30, 37)
        pipette_300.drop_tip()

    # Wash with PBS
    for wash_index in range(3):
        for well_index in range(3):
            pipette_300.pick_up_tip(tiprack_300.wells()[(wash_index * 3) + well_index])
            pipette_300.aspirate(200, pbs)
            pipette_300.dispense(200, cell_plate.wells()[(wash_index * 2) + well_index])
            pipette_300.drop_tip()

    # Add secondary antibody to each well of the 6-well plate and incubate
    for well_index in range(6):
        pipette_300.pick_up_tip(tiprack_300.wells()[well_index])
        pipette_300.aspirate(50, antibody_2)
        pipette_300.dispense(50, cell_plate.wells()[well_index])
        pipette_300.mix(3, 100, cell_plate.wells()[well_index])
        pipette_300.incubate(30, 37)
        pipette_300.drop_tip()

    # Wash with PBS again
    for wash_index in range(3):
        for well_index in range(3):
            pipette_300.pick_up_tip(tiprack_300.wells()[(wash_index * 3) + well_index])
            pipette_300.aspirate(200, pbs)
            pipette_300.dispense(200, cell_plate.wells()[(wash_index * 2) + well_index])
            pipette_300.drop_tip()

    # Stain with DAPI
    for well_index in range(6):
        pipette_300.pick_up_tip(tiprack_300.wells()[well_index])
        pipette_300.aspirate(50, antibody_3)
        pipette_300.dispense(50, cell_plate.wells()[well_index])
        pipette_300.mix(3, 100, cell_plate.wells()[well_index])
        pipette_300.incubate(30, 37)
        pipette_300.drop_tip()

    # End the experiment
    protocol.comment('Immunostaining complete.')
