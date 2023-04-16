from opentrons import simulate
protocol = simulate.get_protocol_api('2.9')

# Load labware
tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
source_tubes = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')

# Load pipettes
p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

# Reagent locations in source tubes
pbs_minus = source_tubes.wells_by_name()["A1"]
scm130 = source_tubes.wells_by_name()["A2"]

# Well group to represent the 6 wells of the plate
wells_6 = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
wells_with_cells = [six_well_plate.wells_by_name()[w] for w in wells_6]


# Helper function to mix content in wells
def mix(well, volume):
    p300.pick_up_tip()
    p300.mix(3, volume, well)
    p300.blow_out()
    p300.drop_tip()


# Remove cell culture medium and PBS wash
for well in wells_with_cells:
    p300.pick_up_tip()
    p300.aspirate(500, well)
    p300.dispense(500, pbs_minus)
    p300.drop_tip()

    p300.pick_up_tip()
    p300.transfer(500, pbs_minus, well, new_tip='never')
    p300.aspirate(500, well)
    p300.dispense(500, pbs_minus)
    p300.drop_tip()


# Add fresh SCM130
for well in wells_with_cells:
    p300.transfer(500, scm130, well)

# Mix the new medium and cells
for well in wells_with_cells:
    mix(well, 300)

protocol.home()
