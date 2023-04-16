metadata = {
    'protocolName': 'My Experiment',
    'author': 'Your name',
    'description': 'A protocol to wash a 6 well plate and add trypsin and cell culture medium'
}

# Labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')
tiprack = labware.load('opentrons_96_tiprack_1000ul', '2')

# Pipettes
p1000 = instruments.P1000_Single(mount='right', tip_racks=[tiprack])

# Add 1 ml of PBS(-) to each well and then remove it
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, well)
    p1000.dispense(1000, waste_reservoir)
    p1000.drop_tip()

# Add 1 ml of trypsin (0.25%) to each well and wait for 5 minutes
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, trypsin_reservoir)
    p1000.dispense(1000, well)
    p1000.mix(10, 1000, well)
    p1000.drop_tip()

# Add 1 ml of DMEM to each well and finish the run
for well in plate.wells():
    p1000.pick_up_tip()
    p1000.aspirate(1000, dmem_reservoir)
    p1000.dispense(1000, well)
    p1000.mix(10, 1000, well)
    p1000.drop_tip()
