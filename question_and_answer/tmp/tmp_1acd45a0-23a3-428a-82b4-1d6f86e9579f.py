from opentrons import labware, instruments

# Load the labware
tiprack = labware.load('opentrons_96_tiprack_1000ul', '1')
trypsin_tuberack = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '2')
cell_plate = labware.load('corning_6_wellplate_16.8ml_flat', '3')
trash = labware.load('point', '4')  # Use a different slot for the trash

# Load the pipette
pipette = instruments.P1000_Single(mount='right', tip_racks=[tiprack])

# Wash the plate with PBS(-)
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(1000, trypsin_tuberack.wells('A1').bottom(2))
    pipette.dispense(1000, well.bottom(2))
    pipette.mix(5, 1000)
    pipette.blow_out(well.top())
    pipette.drop_tip(trash)

# Add trypsin solution and wait 5 minutes
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(1000, trypsin_tuberack.wells('A2').bottom(2))
    pipette.dispense(1000, well.bottom(2))
    pipette.mix(5, 1000)
    pipette.blow_out(well.top())
    pipette.drop_tip()

# Add cell culture medium
for well in cell_plate.wells():
    pipette.pick_up_tip()
    pipette.aspirate(1000, trypsin_tuberack.wells('A3').bottom(2))
    pipette.dispense(1000, well.bottom(2))
    pipette.mix(5, 1000)
    pipette.blow_out(well.top())
    pipette.drop_tip(trash)
