Sure, here is a Python script that uses the Opentrons machine to exchange the hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate:

``` python
# Import the necessary Opentrons modules
from opentrons import labware, instruments, robot

# Load the 6 well plate into the robot
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')

# Load the pipette and set the volume range
pipette = instruments.P300_Single(
    mount='left',
    tip_racks=[labware.load("opentrons_96_tiprack_300ul", '2')],
    aspirate_flow_rate=50,
    dispense_flow_rate=50,
    tip_pick_up_height=10,
    tip_drop_height=13,
    tip_pick_up_distance=1
)
pipette.volume_range = (30, 300)

# Define the coordinates where the pipette should aspirate the PBS(-) and D-MEM from, in the same well order
aspirate_locations = [(2.5, 2.5), (2.5, 7.5)]

# Define the coordinates where the pipette should dispense the PBS(-) and D-MEM into, in the same well order
dispense_locations = [(2.5, 1.5), (2.5, 6.5)]

# Define the volumes of PBS(-) and D-MEM to dispense into the wells
volumes = [200, 300]

# Define the number of times to exchange the medium in each well
num_exchanges = 2

# Iterate over each well in the plate
for well_idx, well in enumerate(plate.wells()):
    # Get the aspirate and dispense coordinates for the current well
    aspirate_coord = aspirate_locations[well_idx % 2]
    dispense_coord = dispense_locations[well_idx % 2]
    
    # Perform the specified number of medium exchanges for the current well
    for i in range(num_exchanges):
        # Aspirate the PBS(-) from the aspirate coordinate
        pipette.aspirate(volumes[0], well.bottom().move_to(*aspirate_coord))
        
        # Dispense the PBS(-) into the well at the dispense coordinate
        pipette.dispense(volumes[0], well.bottom().move_to(*dispense_coord))
        
        # Aspirate the PBS(-) and D-MEM mixture from the well at the aspirate coordinate
        pipette.aspirate(volumes[1], well.bottom().move_to(*aspirate_coord))
        
        # Dispense the D-MEM into the well at the dispense coordinate to complete the medium exchange
        pipette.dispense(volumes[1], well.bottom().move_to(*dispense_coord))
```

You would need to connect to the Opentrons machine through the Opentrons app and run this script on the app's scripting page. Note that this script is written for the Corning 6 well plate, so you may need to adjust some coordinates or use different labware for your specific experiment.


:*************************


