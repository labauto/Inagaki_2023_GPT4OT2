Sure, here's a Python script that should achieve what you're looking for using the Opentrons machine:

```
from opentrons import protocol_api

# set up the Opentrons API
metadata = {'apiLevel': '2.10'}
protocol = protocol_api.ProtocolContext(metadata=metadata)

# define the plate positions
plate_96_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # OS- plate
plate_96_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', 4) # OS+ plate
plate_6_hmsc = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 2) # hMSC plate


# transfer DMEM to each well of OS- plate
for well in plate_96_os_minus.wells():
    protocol.transfer(100, plate_6_hmsc.wells()[0], well)

# transfer DMEM high glucose to each well of OS+ plate, then add osteoinduction supplements
for well in plate_96_os_plus.wells():
    protocol.transfer(100, plate_6_hmsc.wells()[0], well.top())
    protocol.transfer(0.1, protocol.load_labware('eppendorf_1.5ml_snapcap', 5).wells()[0], well, new_tip='always')
    protocol.transfer(1, protocol.load_labware('eppendorf_1.5ml_snapcap', 5).wells()[1], well, new_tip='always')
    protocol.transfer(1, protocol.load_labware('eppendorf_1.5ml_snapcap', 5).wells()[2], well, new_tip='always')

# transfer hMSC cells to each well of both plates
for well in plate_96_os_minus.wells() + plate_96_os_plus.wells():
    protocol.transfer(100, plate_6_hmsc.wells()[1], well, mix_before=(3, 50))

# end the protocol
protocol.comment("Protocol complete.")
``` 

Note that the above code assumes that the hMSC plate contains DMEM in the first well and the hMSC cells in the second well (positions 0 and 1, respectively), and that the three osteoinduction supplements (Dex, AA and BGP) are in the first, second and third wells of an Eppendorf 1.5mL snapcap tube, respectively (positions 0, 1 and 2, respectively). You may need to adjust these positions to match your specific experimental setup.


:*************************


