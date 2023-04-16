from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Immunostaining for Lysosomes on hMSCs',
    'author': 'Your Name',
    'description': 'Automate immunostaining process for hMSCs to visualize lysosomes',
    'apiLevel': '2.5'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p1000_tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')
    trough = protocol.load_labware('nest_12_reservoir_15ml', '4')

    # pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[p1000_tiprack])

    # reagents
    blocking_buffer = trough['A1']
    primary_antibody = trough['A2']
    secondary_antibody = trough['A3']
    mounting_medium = trough['A4']
    wash_buffer = trough['A5']

    # variables
    plate_wells = plate_6_well.wells()
    num_sample_wells = 6
    blocking_time = 10  # in minutes
    primary_antibody_time = 2  # in hours
    secondary_antibody_time = 1  # in hour
    buffer_volume = 150  # in ul
    plate_well_volume = 1000  # in ul

    # distribute blocking buffer
    p300.pick_up_tip()
    for well in plate_wells:
        p300.aspirate(buffer_volume, blocking_buffer)
        p300.dispense(buffer_volume, well)
    p300.drop_tip()

    # incubate cells with blocking buffer
    protocol.delay(minutes=blocking_time)

    # wash cells with wash buffer
    p1000.pick_up_tip()
    for well in plate_wells:
        p1000.aspirate(buffer_volume, wash_buffer)
        p1000.dispense(buffer_volume, well)
    p1000.drop_tip()

    # prepare primary antibody solution
    p1000.pick_up_tip()
    buffer_to_antibody_ratio = 4
    primary_antibody_volume = num_sample_wells * buffer_volume / buffer_to_antibody_ratio
    p1000.aspirate(primary_antibody_volume, primary_antibody)
    p1000.dispense(primary_antibody_volume, trough['A6'])
    p1000.drop_tip()

    # distribute primary antibody solution to wells
    p300.pick_up_tip()
    for well in plate_wells:
        p300.aspirate(buffer_volume, trough['A6'])
        p300.dispense(buffer_volume, well)
    p300.drop_tip()

    # incubate cells with primary antibody solution
    protocol.delay(hours=primary_antibody_time)

    # wash cells with wash buffer
    p1000.pick_up_tip()
    for well in plate_wells:
        p1000.aspirate(buffer_volume, wash_buffer)
        p1000.dispense(buffer_volume, well)
    p1000.drop_tip()

    # prepare secondary antibody solution
    p1000.pick_up_tip()
    secondary_antibody_volume = num_sample_wells * buffer_volume / buffer_to_antibody_ratio
    p1000.aspirate(secondary_antibody_volume, secondary_antibody)
    p1000.dispense(secondary_antibody_volume, trough['A7'])
    p1000.drop_tip()

    # distribute secondary antibody solution to wells
    p300.pick_up_tip()
    for well in plate_wells:
        p300.aspirate(buffer_volume, trough['A7'])
        p300.dispense(buffer_volume, well)
    p300.drop_tip()

    # incubate cells with secondary antibody solution
    protocol.delay(hours=secondary_antibody_time)

    # wash cells with wash buffer
    p1000.pick_up_tip()
    for well in plate_wells:
        p1000.aspirate(buffer_volume, wash_buffer)
        p1000.dispense(buffer_volume, well)
    p1000.drop_tip()

    # mount coverslips with mounting medium
    for well in plate_wells:
        p1000.pick_up_tip()
        p1000.aspirate(50, mounting_medium)
        p1000.move_to(well.top(-10))
        protocol.delay(seconds=5)
        p1000.dispense(50, well.top(-10))
        protocol.delay(minutes=5)
        p1000.drop_tip()

