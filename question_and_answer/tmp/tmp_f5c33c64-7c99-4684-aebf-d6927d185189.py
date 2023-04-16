Sure! Here's a Python script that should automate the experiment using the specified labware and pipette:

```
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Cell Culture Experiment',
    'author': 'Your Name Here',
    'description': 'Automating Cell Culture Experiment using Opentrons',
    'apiLevel': '2.10'
}

# function to create tip rack and pipette
def create_pipette(pipette_type:str, tip_rack_type:str, tip_slots:list) -> protocol_api:
    # create tip racks
    tip_racks = [protocol.load_labware(tip_rack_type, slot) for slot in tip_slots]
    # create pipette
    pipette = protocol.load_instrument(pipette_type, 'right', tip_racks=tip_racks)
    return pipette

# protocol
def run(protocol: protocol_api.ProtocolContext):
    # labware
    p1000_tip_racks_slots = ['1', '2', '3', '4']
    p1000_tip_racks_type = 'opentrons_96_tiprack_1000ul'
    trypsin_well = 'B2'
    dmem_well = 'A1'
    wash_wells = ['A2', 'B1', 'C1', 'C2', 'D1', 'D2']
    plate_type = 'corning_6_wellplate_16.8ml_flat'
    plate = protocol.load_labware(plate_type, '5')
    # pipettes
    p1000 = create_pipette('p1000_single', p1000_tip_racks_type, p1000_tip_racks_slots)
    # washing 6 well plate
    p1000.pick_up_tip()
    for well in wash_wells:
        p1000.transfer(1000, plate[well], p1000.trash_container.top(), new_tip='never')
        p1000.transfer(1000, plate[well], p1000.trash_container.top(), new_tip='never')
    p1000.drop_tip()
    # adding trypsin
    p1000.pick_up_tip()
    p1000.transfer(1000, plate[trypsin_well], p1000.trash_container.top(), new_tip='never')
    p1000.transfer(1000, plate[trypsin_well], p1000.trash_container.top(), new_tip='never')
    p1000.return_tip()
    protocol.delay(minutes=5)
    # adding DMEM
    p1000.pick_up_tip()
    p1000.transfer(1000, plate[dmem_well], p1000.trash_container.top(), new_tip='never')
    p1000.transfer(1000, plate[dmem_well], p1000.trash_container.top(), new_tip='never')
    p1000.drop_tip()
```
Some notes on the script:
- The script uses the Opentrons API to create labware and pipettes, aspirating and dispensing liquids, and to delay the protocol. 
- The function `create_pipette` is created to avoid redundant code for loading tips and pipettes for different pipette types. 
- The specified labware and pipette are declared in the protocol as variables. 
- The script has comments that explain the functionality of the different steps, including adding trypsin and DMEM, and aspirating and dispensing the washing solution into the 6-well plate.
- The script should automatically dispose of tips. However, be aware of the maximum volume of the pipette when aspirating or dispensing liquids. 

Hope that helps! Let me know if you have any other questions.


:*************************


