from opentrons import simulate
protocol = simulate.get_protocol_api('2.11')

# Labware
tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
cell_plate = protocol.load_labware('corning_6_wellplate_3500ul_flat', '2')
reagent_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')

# Pipettes
pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

# Reagents
lysosome_stain = reagent_rack.wells_by_name()['A1']
fixation_solution = reagent_rack.wells_by_name()['A2']
blocking_solution = reagent_rack.wells_by_name()['A3']

# Perform the experiment
# Add lysosome stain to hMSC cells in each well
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(10, lysosome_stain)
    pipette.dispense(10, well)
    pipette.drop_tip()

# Incubate for a desired amount of time (1 hour as an example)
protocol.delay(minutes=60)

# Remove lysosome stain and wash with fixation solution
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(350, well)
    pipette.dispense(350, lysosome_stain)
    pipette.aspirate(350, fixation_solution)
    pipette.dispense(350, well)
    pipette.drop_tip()

# Incubate for 15 minutes in fixation solution
protocol.delay(minutes=15)

# Wash with blocking solution
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(350, well)
    pipette.dispense(350, fixation_solution)
    pipette.aspirate(350, blocking_solution)
    pipette.dispense(350, well)
    pipette.drop_tip()

# Incubate for another hour in blocking solution
protocol.delay(minutes=60)

# Dispose remaining liquids and remove labware

protocol.home()

print("Experiment completed!")
