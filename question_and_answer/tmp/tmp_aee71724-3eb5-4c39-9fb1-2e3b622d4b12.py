Sure, here is a Python script that automates the experiment steps you outlined using Opentrons robot:

``` python
from opentrons import protocol_api
import math

metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Measurement of viability and cytotoxicity of an adherent cell line, A549 cells, treated with thapsigargin',
    'apiLevel': '2.5'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware and tiprack definition
    tc_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_1.5ml_snapcap', '6')
    medium_control_well = tc_plate.wells_by_name()['A5']
    reagent_tubes = tube_rack.columns_by_name()['1']
    drug_tubes = tube_rack.columns_by_name()['7']

    # Pipette definition
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left')

    # Helper functions
    
    def mix_tube_contents(tube, vol):
        p300_multi.pick_up_tip()
        p300_multi.mix(3, vol, tube)
        p300_multi.blow_out()
        p300_multi.drop_tip()

    def add_drug_concentration_to_plate(concentration, column_index, cell_volume):
        # dilute thapsigargin 4x
        medium_volume = 100
        thaps_dil_values = [1.56, 3.12, 6.24, 12.52, 25, 50, 100, 200, 400, 800, 1600, 2000]
        for thaps_vol, dil in zip(thaps_dil_values, drug_tubes[column_index].wells()):
            # add diluent
            p300_multi.pick_up_tip()
            p300_multi.aspirate(medium_volume, reagent_tubes[0])
            p300_multi.dispense(medium_volume, dil)
            p300_multi.mix(3, medium_volume, dil)
            p300_multi.blow_out()
            p300_multi.drop_tip()
            # add thapsigargin
            p300_multi.pick_up_tip()
            p300_multi.mix(3, thaps_vol, dil)
            p300_multi.aspirate(cell_volume, dil)
            p300_multi.dispense(cell_volume, dil)
            p300_multi.blow_out()
            p300_multi.drop_tip()

        # make 2x dilution
        for row, well in enumerate(tc_plate.columns_by_name()[str(column_index+1)]):
            p300_multi.pick_up_tip()
            if row <=2:
                p300_multi.aspirate(cell_volume*2, medium_control_well)
            else:
                p300_multi.aspirate(cell_volume*2, tc_plate.columns_by_name()[str(column_index+1)][3])
            p300_multi.dispense(cell_volume*2, well)
            mix_tube_contents(drug_tubes[column_index].wells_by_name()['A1'], vol=50)
            p300_multi.aspirate(cell_volume, drug_tubes[column_index].wells_by_name()[str(math.ceil((row+1)/3))])
            p300_multi.dispense(cell_volume, well)
            mix_tube_contents(drug_tubes[column_index].wells_by_name()[str(math.ceil((row+1)/3))], vol=50)

    
    # Step 1: Cell Count
    p300_multi.pick_up_tip()
    p300_multi.mix(3, 20, tube_rack.columns()[0])
    p300_multi.blow_out()
    p300_multi.drop_tip()
    
    # Step 2: Cell Seeding
    cell_volume = 60
    p300_multi.pick_up_tip()
    for well in tc_plate.wells():
        p300_multi.aspirate(cell_volume, tube_rack.columns_by_name()['6'][0])
        p300_multi.dispense(cell_volume, well)
    p300_multi.blow_out()
    p300_multi.drop_tip()

    # Step 3 to 9: Preparing and Adding drug concentrations to the plate
    add_drug_concentration_to_plate(1, 0, cell_volume) # Column 1 contains control cells
    add_drug_concentration_to_plate(2, 1, cell_volume)
    add_drug_concentration_to_plate(3, 2, cell_volume)
    add_drug_concentration_to_plate(4, 3, cell_volume)
    add_drug_concentration_to_plate(5, 4, cell_volume)

    # Step 10: Adding CellTox Green
    p300_multi.pick_up_tip()
    for col in tc_plate.columns()[:6]:
        for well in col[:4]:
            p300_multi.aspirate(15, reagent_tubes[1])
            p300_multi.dispense(15, well)
        p300_multi.aspirate(15, reagent_tubes[1])
        p300_multi.dispense(15, well)
    p300_multi.drop_tip()

    protocol.heated_lid.set_temperature(37)
    protocol.set_rail_lights(True)

    # Step 11: Orbital shaking for 2 minutes at 500 rpm
    protocol.set_rail_lights(True)
    protocol.set_rail_lights(lights_on=False)
    protocol.set_rail_lights(lights_on=True)
    protocol.pause('Orbital shake Heater/Shaker for 2 minutes at 500 rpm, then continue after the orbital shaking is complete.')
    
    # Step 12: Incubating plate at RT for 15 minutes
    protocol.set_rail_lights(lights_on=False)
    protocol.pause('Incubate plate at RT for 15 minutes, then continue after the incubation is complete.')
    
    # Step 13: Reading fluorescence
    # Assuming the reader is connected and a protocol is already set up there
    protocol.pause('Place the plate on the reader and continue after taking the fluorescence reading.')

    # Step 14 & 15: Adding and Reading Luminescence
    p300_multi.pick_up_tip()
    for col in tc_plate.columns()[:6]:
        for well in col[:4]:
            p300_multi.aspirate(80, reagent_tubes[0])
            p300_multi.dispense(80, well)
        p300_multi.aspirate(80, reagent_tubes[0])
        p300_multi.dispense(80, well)
    p300_multi.drop_tip()

    # Step 16: Orbital shaking for 2 minutes at 500 rpm
    protocol.set_rail_lights(True)
    protocol.set_rail_lights(lights_on=False)
    protocol.set_rail_lights(lights_on=True)
    protocol.pause('Orbital shake Heater/Shaker for 2 minutes at 500 rpm, then continue after the orbital shaking is complete.')
    
    # Step 17: Incubating plate at RT for 10 minutes
    protocol.set_rail_lights(lights_on=False)
    protocol.pause('Incubate plate at RT for 10 minutes, then continue after the incubation is complete.')
    
    # Step 18: Reading luminescence
    # Assuming the reader is connected and a protocol is already set up there
    protocol.pause('Place the plate on the reader and continue after taking the luminescence reading.')
```

The code is divided into several functions to make it more modular and easier to understand.


:*************************


