Sure, here's a Python script that does the experiment you described using the Opentrons machine:

```
from opentrons import labware, instruments

# load the labware (6-well plate and 96-well plate)
culture_plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
spheroid_plate = labware.load('corning_96_wellplate_360ul_flat', '2')

# define the wells
culture_wells = [well for well in culture_plate.wells()[:6]]
OSminus_wells = [well for well in spheroid_plate.wells()[:48]]
OSplus_wells = [well for well in spheroid_plate.wells()[48:]]

# define the pipettes
p1000 = instruments.P1000_Single(
    mount='left',
    tip_racks=[labware.load('opentrons_96_tiprack_1000ul', '3')]
)
p10 = instruments.P10_Single(
    mount='right',
    tip_racks=[labware.load('opentrons_96_tiprack_10ul', '4')]
)

# transfer 100 µl DMEM to all OS- wells
p1000.transfer(100, culture_wells, OSminus_wells)

# transfer 100 µl DMEM high glucose to all OS+ wells
p1000.transfer(100, culture_wells, OSplus_wells)

# add osteoinduction supplements to all OS+ wells
p10.distribute(
    [0.1, 1, 1],
    OSplus_wells,
    mix_before=(3, 10)
)

# transfer 100 µl hMSC cells to all OS- wells
p1000.transfer(100, [culture_wells[0]], OSminus_wells)

# transfer 100 µl hMSC cells to all OS+ wells
p1000.transfer(100, [culture_wells[0]], OSplus_wells)

# end
print("Experiment completed.")
```

In this script, we first load the labware (a 6-well plate for cell culture and a 96-well plate for spheroid formation). Then we define the wells we'll use in each plate (culture wells, OS-minus wells, and OS-plus wells). We also define the pipettes we'll use for the transfer (p1000 and p10).

Next, we run the experiment:

- First, we use p1000 to transfer 100 µl of DMEM to all the OS-minus wells.
- Then, we use p1000 to transfer 100 µl of DMEM high glucose to all the OS-plus wells.
- We use p10 to add osteoinduction supplements to all the OS-plus wells.
- We use p1000 to transfer 100 µl of hMSC cells to all the OS-minus wells.
- Finally, we use p1000 to transfer 100 µl of hMSC cells to all the OS-plus wells.

After all transfers are done, the script ends.


:*************************


