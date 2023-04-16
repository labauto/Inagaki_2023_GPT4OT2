from opentrons import labware, instruments, robot

# Load the labware
tiprack_1000 = labware.load('opentrons_1000ul_tiprack', '1')
plate_6_well =  labware.load('corning_6_wellplate_16.8ml_flat', '4')
tube_rack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '5')

# Load the pipette
pipette = instruments.P1000_Single(mount='left', tip_racks=[tiprack_1000])

# Define the protocol steps
def run_protocol():
    # Wash the 6 well plate with PBS(-) by pipetting up and down 5 times. For each well use 1 ml of PBS(-).
    for well in plate_6_well.wells():
        pipette.pick_up_tip()
        pipette.mix(5, 1000, tube_rack.wells(0))
        pipette.aspirate(1000, tube_rack.wells(0))
        pipette.dispense(1000, well)
        pipette.mix(5, 1000, well)
        pipette.drop_tip()

    # After washing, add 1 ml of trypsin solution (0.25%) to the cell culture dish and wait for 5 minutes.
    pipette.pick_up_tip()
    pipette.aspirate(1000, tube_rack.wells(1))
    pipette.dispense(1000, plate_6_well.wells('A1'))
    pipette.mix(5, 1000, plate_6_well.wells('A1'))
    pipette.drop_tip()

    robot.pause(minutes=5)

    # Then, add 1 mL of cell culture medium (DMEM) to the 6 well plate.
    for well in plate_6_well.wells():
        pipette.pick_up_tip()
        pipette.aspirate(1000, tube_rack.wells(2))
        pipette.dispense(1000, well)
        pipette.mix(5, 1000, well)
        pipette.drop_tip()

# Run the protocol
run_protocol()
