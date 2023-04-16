Yes, add metadata specifying the API version to the protocol.

```
metadata = {
    "author": "Your Name",
    "apiLevel": "2.0"
}


def run(protocol):

    plate_osplus = protocol.load_labware("corning_96_wellplate_360ul_flat", 1)
    plate_osminus = protocol.load_labware("corning_96_wellplate_360ul_flat", 2)

    p1000 = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[
                                     labware.load('opentrons_96_tiprack_1000ul', slot) for slot in ['3']])

    # Transfer DMEM to all wells in the OS(-) plate
    for well in plate_osminus.wells():
        p1000.pick_up_tip()
        p1000.transfer(100, dmem, well.bottom(2), new_tip='never')
        p1000.drop_tip()

    # Transfer DMEM high glucose and supplements to all wells in the OS(+) plate
    for well in plate_osplus.wells():
        p1000.pick_up_tip()
        p1000.transfer(100, dmem_highglucose, well.bottom(2), new_tip='never')
        p1000.touch_tip()
        p1000.drop_tip()

    # Add osteoinduction supplements to all wells in the OS(+) plate
    for well in plate_osplus.wells():
        for reagent, vol in zip(os_supplements, supplement_volumes):
            p1000.pick_up_tip()
            p1000.transfer(vol, reagent, well.bottom(2), new_tip='never')
            p1000.touch_tip()
            p1000.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in plate_osminus.wells():
        p1000.pick_up_tip()
        p1000.transfer(100, cell_suspension, well.bottom(2), new_tip='never')
        p1000.mix(5, 500)
        p1000.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in plate_osplus.wells():
        p1000.pick_up_tip()
        p1000.transfer(100, cell_suspension, well.bottom(2), new_tip='never')
        p1000.mix(5, 500)
        p1000.drop_tip()
```


:*************************


