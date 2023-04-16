from opentrons import simulate
metadata = {
    'apiLevel': '2.0'
}

protocol = simulate.get_protocol_api('2.0')
protocol.home()

# Labware
tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
trough = protocol.load_labware('agilent_12_reservoir_15000ul', 2)
plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)

# Pipette
p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])

# Reagents
pbs_minus = trough.wells_by_name()['A1']
scm130 = trough.wells_by_name()['A2']

# Wells in the 6-well plate
wells_to_fill = plate_6_well.wells()

# Exchange media in 6-well plate
for well in wells_to_fill:
    # Remove 50% of the medium with PBS(-)
    p300.pick_up_tip()
    p300.aspirate(5_000, pbs_minus)  # Adjust the volume as needed
    p300.dispense(5_000, well)
    p300.drop_tip()

    # Add new SCM130 media
    p300.pick_up_tip()
    p300.aspirate(5_000, scm130)  # Adjust the volume as needed
    p300.dispense(5_000, well)
    p300.drop_tip()

# Finish the experiment
protocol.comment("Experiment complete!")
