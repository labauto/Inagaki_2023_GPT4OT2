Sure, here's a Python script that does the experiment you described. The script assumes that the Opentrons machine is connected and set up correctly:

```
from opentrons import robot, instruments

# Define constants
WELL_PLATE_96 = '96-well-plate'
WELL_PLATE_6 = '6-well-plate'
VOL_MEDIUM = 100  # µl
VOL_SUBSTANCES = 0.1, 1, 1  # Dexamethasone, Ascorbic acid, beta-glycerophosphate
VOL_CELLS = 100  # µl
NUM_CELLS = 2500  # cells/100 µl

def transfer_medium(dispense_plate, volume):
    # Transfer medium to each well of dispense_plate
    pipette.distribute(volume, medium_source.bottom(), [well.bottom() for well in dispense_plate.wells()])

def add_substances(dispense_plate, substances, volume):
    # Add substances to each well of dispense_plate
    pipette.distribute(volume, [substance_source.bottom() for substance_source in substances], [well.bottom() for well in dispense_plate.wells()])

def transfer_cells(dispense_plate, volume, num_cells):
    # Transfer cells to each well of dispense_plate
    pipette.distribute(volume, cell_source.bottom(), [well.bottom() for well in dispense_plate.wells()], new_tip='always')
    # Calculate the volume of cells to pipette based on num_cells, and pipette that amount
    for well in dispense_plate.wells():
        if well.volume > 0:
            num_cells_pipetted = round(well.volume / VOL_CELLS * NUM_CELLS)
            if num_cells_pipetted > num_cells:
                pipette.aspirate(well.volume - volume, well.bottom())
                pipette.dispense(well.volume - volume, waste)
                num_cells_pipetted = num_cells
            else:
                volume_to_pipette = num_cells / NUM_CELLS * VOL_CELLS
                pipette.aspirate(volume_to_pipette, cell_source.bottom())
                pipette.dispense(volume_to_pipette, well.bottom())
            num_cells -= num_cells_pipetted

def main():
    # Set up robot and labware
    robot.disconnect()
    robot.connect()
    robot.home()
    medium_source = instruments.Slot(1).from_labware(WellPlate_6)
    substance_sources = [instrumets.Slot(i).from_labware(WellPlate_6, index=2+j) for j in range(3)]
    cell_source = instruments.Slot(4).from_labware(WellPlate_6)
    waste = instruments.Slot(12).from_labware('trough-12row', well='A12')
    os_minus_dispense_plate = instruments.Slot(7).from_labware(WELL_PLATE_96)
    os_plus_dispense_plate = instruments.Slot(8).from_labware(WELL_PLATE_96)

    # Set up pipette
    pipette = instruments.P1000_Single(
        tip_racks=[instruments.Slot(5).from_labware('opentrons-tiprack-1000ul', label='tiprack-1000-1')],
        trash_container=waste,
        aspirate_flow_rate=300,
        dispense_flow_rate=300,
        tip_pick_up_distance=5,
        tip_drop_distance=2
    )

    # Perform the experiment
    transfer_medium(os_minus_dispense_plate, VOL_MEDIUM)
    transfer_medium(os_plus_dispense_plate, VOL_MEDIUM)
    add_substances(os_plus_dispense_plate, substance_sources, VOL_SUBSTANCES)
    transfer_cells(os_minus_dispense_plate, VOL_CELLS, NUM_CELLS)
    transfer_cells(os_plus_dispense_plate, VOL_CELLS, NUM_CELLS)

    # Disconnect robot
    robot.disconnect()


if __name__ == '__main__':
    main()
```

This script defines several functions that perform each step of the experiment, such as `transfer_medium` and `add_substances`. These functions take as input the destination plate (either the OS- or OS+ plate), the volume of liquid to dispense, and any additional substances to add to the OS+ plate. The function `transfer_cells` takes an additional input, `num_cells`, which specifies the number of cells to transfer for each well.

The `main` function sets up the robot and labware, defines the pipette, and calls the helper functions in order to perform the experiment. Finally, it disconnects the robot.

Note that the script is written for the Opentrons OT-2 and may need to be adapted for a different robot model.


:*************************


