Certainly! Here is an updated Python script for exchanging hMSC cell culture medium using PBS(-) and SCM130 using an Opentrons robot that shouldn't give you the errors you've encountered:

```
metadata = {
    'protocolName': 'MSC medium exchange',
    'author': 'Your name here',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and SCM130',
}

# Define labware
plate = opentrons.labware.load('6-well-plate', '1')
tiprack = opentrons.labware.load('tiprack-200ul', '2')
reservoir = opentrons.labware.load('96-flat','3')

# Define pipettes
pipette = opentrons.instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack])

# Define well locations
well_locs = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']

# Define pbs_col
pbs_col = 0

# Perform medium exchange
pipette.pick_up_tip()

for well_loc in well_locs:
    well = plate[well_loc]
    
    # Aspirate 900 ul of old medium
    pipette.aspirate(900, well.bottom(2))

    # Dispense 900 ul of PBS(-)
    pipette.dispense(900, reservoir.wells()[pbs_col].bottom(1))

    # Aspirate 900 ul of PBS(-)
    pipette.aspirate(900, reservoir.wells()[pbs_col].bottom(2))
    
    # Dispense 900 ul of new medium
    pipette.dispense(900, well.bottom(1))
    
    # Move to the next well
    pipette.move_to(well.top(1))
    
pipette.drop_tip()
```


Please note that you may need to adjust some of the labware names or other parameters to match your specific setup. Let me know if you have any further questions or issues!


:*************************


