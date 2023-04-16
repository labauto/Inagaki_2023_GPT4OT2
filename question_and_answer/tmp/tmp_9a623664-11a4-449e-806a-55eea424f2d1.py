# Import modules
from opentrons import labware, instruments, robot

# Define labware
plate_6_well = labware.load("corning_6_wellplate_16.8ml_flat", "1")
pipette = instruments.P1000_Single(mount="right")

# Define reagents and volumes
wash_vol = 1000  # uL
trypsin_vol = 1000  # uL
medium_vol = 1000  # uL

# Define protocol
def run_protocol():
    # Step 1
    pipette.pick_up_tip()
    for well in plate_6_well.wells():
        pipette.aspirate(wash_vol, well)
        for _ in range(5):
            pipette.dispense(800, well)
            pipette.aspirate(800, well)
    pipette.drop_tip()

    # Step 2
    pipette.pick_up_tip()
    for well in plate_6_well.wells():
        pipette.transfer(
            trypsin_vol, well.bottom(1), well.bottom(2), new_tip="never"
        )
    robot.pause(300)

    # Step 3
    pipette.pick_up_tip()
    for well in plate_6_well.wells():
        pipette.transfer(
            medium_vol, well.bottom(1), well.bottom(2), new_tip="never"
        )
    pipette.drop_tip()

# Run protocol
run_protocol()
