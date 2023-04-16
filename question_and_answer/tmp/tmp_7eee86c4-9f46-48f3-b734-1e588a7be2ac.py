from opentrons import labware, instruments, robot

# Load labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
tip_rack = labware.load('opentrons_96_tiprack_1000ul', '2')

# Load pipette
pipette = instruments.P1000_Single(mount='left', tip_racks=[tip_rack])

# Define cleanup function
def cleanup():
    pipette.drop_tip(tip_rack.columns()[0])


# Wash plate with PBS(-)
pipette.pick_up_tip()
for well in plate.wells():
    pipette.transfer(1000, pipette.trash_container.top(), well, new_tip='never')
    for i in range(5):
        pipette.aspirate(1000, well)
        pipette.dispense(1000, well)
pipette.drop_tip()

# Add trypsin solution and wait 5 minutes
pipette.pick_up_tip()
for well in plate.wells():
    pipette.aspirate(1000, well)
    pipette.dispense(1000, pipette.trash_container.top())
pipette.drop_tip()
robot.pause('Incubate the cells for 5 minutes before resuming.')

# Add cell culture medium
pipette.pick_up_tip()
for well in plate.wells():
    pipette.aspirate(1000, pipette.trash_container.top())
    pipette.dispense(1000, well)
pipette.drop_tip()

# Finish and clean up
cleanup()
