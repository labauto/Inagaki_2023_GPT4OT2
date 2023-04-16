Sure, here's an example Python script for exchanging hMSC cell culture medium using PBS(-) and SCM130 using an Opentrons robot:

``` python
# Import Opentrons API
from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('6-well-plate', '1')  # Load 6 well plate

# Define instruments
p300 = instruments.P300_Single(mount="left", tip_racks=[labware.load('opentrons_96_tiprack_300ul', '3')])  # Load P300 pipette

# Define liquids
pbs = labware.load('pcr-strip-tall', '4')  # Load PCR strip for PBS(-)
scm130 = labware.load('pcr-strip-tall', '5')  # Load PCR strip for SCM130

# Define protocol
def run():
    # Define variables
    vol_to_dispense = 200  # volume to dispense for each well
    num_wells = 6  # number of wells with cells

    # Display protocol
    print('Prepare to exchange hMSC cell culture medium using PBS(-) and SCM130')
    print('Number of wells:', num_wells)
    print('Volume to dispense:', vol_to_dispense)

    # Dispense PBS(-) for each well
    for well in plate.wells()[:num_wells]:
        p300.pick_up_tip()  # Pick up tip
        p300.aspirate(vol_to_dispense, pbs[0])  # Aspirate PBS(-)
        p300.dispense(vol_to_dispense, well)  # Dispense PBS(-)
        p300.drop_tip()  # Drop tip

    # Wait 5 minutes for PBS(-) to work on cells
    robot.comment("Waiting for 5 minutes...")
    robot.pause(300)

    # Remove PBS(-) from each well
    for well in plate.wells()[:num_wells]:
        p300.pick_up_tip()  # Pick up tip
        p300.aspirate(vol_to_dispense, well)  # Aspirate PBS(-)
        p300.dispense(vol_to_dispense, pbs[0])  # Dispense PBS(-) back to its container
        p300.drop_tip()  # Drop tip

    # Dispense SCM130 for each well
    for well in plate.wells()[:num_wells]:
        p300.pick_up_tip()  # Pick up tip
        p300.aspirate(vol_to_dispense, scm130[0])  # Aspirate SCM130
        p300.dispense(vol_to_dispense, well)  # Dispense SCM130
        p300.drop_tip()  # Drop tip

    # Protocol complete
    print("Protocol complete!")
```

This script should be optimized for your specific equipment, so make sure to adjust it as necessary.


:*************************


