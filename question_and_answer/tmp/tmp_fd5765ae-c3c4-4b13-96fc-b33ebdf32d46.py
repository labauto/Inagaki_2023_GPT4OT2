from opentrons import labware, instruments

# Load the 6 well plate for cell culture
culture_plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
# Load the 96 well flat bottom plate for spheroids formation
spheroid_plate = labware.load('96-well-plate-flat', '2')
# Define the tips to use
tiprack_200 = labware.load('tiprack-200ul', '3')

# Define the pipette
pipette = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_200],
    aspirate_flow_rate=50,
    dispense_flow_rate=50,
    aspirate_speed=50,
    dispense_speed=50
)

# Transfer 100ul of medium (DMEM) to each well of 96 well plate (OS-)
pipette.pick_up_tip()
for well in spheroid_plate.wells():
    pipette.transfer(100, culture_plate.wells(0), well, new_tip='never')
pipette.drop_tip()

# Transfer 100ul of medium (DMEM high glucose) to each well of 96 well plate (OS+)
pipette.pick_up_tip()
for well in spheroid_plate.wells():
    pipette.transfer(100, culture_plate.wells(0), well, new_tip='never')
pipette.drop_tip()

# Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid),
# and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
pipette.pick_up_tip()
for well in spheroid_plate.columns_by_name()['2'][::2]:
    pipette.transfer(0.1, culture_plate.wells(1), well, new_tip='never')
    pipette.transfer(1, culture_plate.wells(2), well, new_tip='never')
    pipette.transfer(1, culture_plate.wells(3), well, new_tip='never')
pipette.drop_tip()

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
pipette.pick_up_tip()
for well in spheroid_plate.wells():
    pipette.transfer(100, culture_plate.wells(4), well, new_tip='never')
pipette.drop_tip()

# Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
pipette.pick_up_tip()
for well in spheroid_plate.wells():
    pipette.transfer(100, culture_plate.wells(4), well, new_tip='never')
pipette.drop_tip()

# End of script
print('Experiment completed!')
