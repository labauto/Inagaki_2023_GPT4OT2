Below is a Python script that uses the Opentrons API to perform the experiment you have described:

```
!pip install opentrons
from opentrons import protocol_api

metadata = {
    'protocolName': 'A549 Viability Cytotoxicity Assay with Thapsigargin',
    'author': 'Your Name',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tip_rack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '10')
    tip_rack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '5')
    cell_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '3', 'cell plate')
    heater_shaker = protocol.load_module('Temperature Module', '1')
    temp_plate = heater_shaker.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tip_rack_20])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tip_rack_200])

    # Reagents
    hams_f12k_medium = tube_rack.wells_by_name()['A5']
    celltiter_glo = tube_rack.wells_by_name()['B1']
    celltox_green = tube_rack.wells_by_name()['B2']
    thapsigargin_stock = tube_rack.wells_by_name()['A1']

    # Aliquot A549 cells into 96-well plate
    for well in cell_plate.wells():
        p200.pick_up_tip()
        p200.aspirate(60, hams_f12k_medium)
        p200.dispense(60, well)
        p200.mix(3, 30)
        p200.drop_tip()

    # Dilute Thapsigargin
    dilutions = []  # Save the positions of the diluted samples for later use

    # ...Insert Thapsigargin dilution code here...

    # Add Thapsigargin to cell plate
    for well, thapsigargin in zip(cell_plate.wells(), dilutions):
        p200.pick_up_tip()
        p200.aspirate(30, thapsigargin)
        p200.dispense(30, well)
        p200.mix(3, 30)
        p200.drop_tip()

    # Incubate for 72 hours (simulate with a delay here)
    protocol.delay(minutes=15)  # Adjust this value to simulate 72 hours

    # Add CellTox Green to cell plate
    for well in cell_plate.wells():
        p20.pick_up_tip()
        p20.aspirate(15, celltox_green)
        p20.dispense(15, well)
        p20.mix(3, 10)
        p20.drop_tip()

    # Orbital shaking and incubation
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)
    protocol.delay(minutes=15)

    # Read fluorescence (placeholder, replace with actual plate reader commands)
    print("Reading fluorescence...")

    # Add CellTiter Glo to cell plate
    for well in cell_plate.wells():
        p200.pick_up_tip()
        p200.aspirate(80, celltiter_glo)
        p200.dispense(80, well)
        p200.mix(3, 40)
        p200.drop_tip()

    # Orbital shaking and incubation
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.set_speed(0)
    protocol.delay(minutes=10)

    # Read luminescence (placeholder, replace with actual plate reader commands)
    print("Reading luminescence...")
```

Note: This script assumes that you have already prepared the Thapsigargin samples in their respective tubes. You'll need to replace the placeholder print statements for reading fluorescence and luminescence with appropriate commands that interface with the Biotek microplate reader. Please make sure to adapt and test this script for your specific environment and hardware setup.


:*************************


