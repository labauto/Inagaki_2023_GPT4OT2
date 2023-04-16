metadata = {'apiLevel': '2.7'}
metadata = {'apiLevel': '2.7'}

# Load the necessary labware
tiprack = labware.load('opentrons_96_tiprack_1000ul', '10')
medium = labware.load('corning_6_wellplate_16.8ml_flat', '2')
trypsin = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '1')

# Load the pipette
pipette = instruments.P1000_Single(
    mount='left',
    tip_racks=[tiprack],
    aspirate_flow_rate=300,
    dispense_flow_rate=300,
    blow_out_flow_rate=500,
)

# Define the volumes to use
PBS = 1000
trypsin_vol = 1000
medium_vol = 1000

# Wash the plate with PBS(-) 5 times
for well in medium.wells():
    pipette.pick_up_tip()
    pipette.aspirate(PBS, trypsin.wells()[0].top())
    pipette.dispense(PBS, well)
    pipette.mix(5, 1000, well)
    pipette.blow_out(well.top())
    pipette.drop_tip()

# Add trypsin and wait
for well in medium.wells():
    pipette.pick_up_tip()
    pipette.aspirate(trypsin_vol, trypsin.wells()[0].bottom())
    pipette.dispense(trypsin_vol, well)
    pipette.mix(10, trypsin_vol, well)
    pipette.blow_out(well.top())
    pipette.drop_tip()

protocol.pause("Make sure to wait for 5 minutes after adding trypsin to the wells.")

# After 5 minutes add DMEM
for well in medium.wells():
    pipette.pick_up_tip()
    pipette.aspirate(medium_vol, medium.wells()[0].bottom())
    pipette.dispense(medium_vol, well)
    pipette.blow_out(well.top())
    pipette.drop_tip()

