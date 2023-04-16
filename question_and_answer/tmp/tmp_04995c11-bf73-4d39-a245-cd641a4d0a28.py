# Import necessary Opentrons modules
from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('6-well-plate', '2')
tiprack = labware.load('tiprack-200ul', '1')

# Define pipettes
pipette = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack],
)

# Define reagents
lysosome_stain = plate.wells('A1')
primary_antibody = plate.wells('B1')
secondary_antibody = plate.wells('C1')
mounting_media = plate.wells('D1')

# Define cells
cells = [well for well in plate.wells() if well != lysosome_stain
                                               and well != primary_antibody
                                               and well != secondary_antibody
                                               and well != mounting_media]

# Distribute lysosome stain to cells
pipette.pick_up_tip()
pipette.aspirate(150, lysosome_stain)
for cell in cells:
    pipette.dispense(30, cell)
    pipette.mix(3, 50)
    pipette.blow_out()
pipette.drop_tip()

# Add primary antibody to cells
pipette.pick_up_tip()
pipette.aspirate(50, primary_antibody)
for cell in cells:
    pipette.dispense(30, cell)
    pipette.mix(3, 50)
pipette.drop_tip()

# Incubate cells with primary antibody
robot.pause("Incubate cells with primary antibody for 30 minutes.")

# Remove primary antibody from cells
for cell in cells:
    pipette.aspirate(30, cell)
    pipette.blow_out()

# Wash cells with PBS
pipette.pick_up_tip()
for i in range(3):
    for cell in cells:
        pipette.aspirate(130, cell)
        pipette.dispense(130, cell)
    pipette.aspirate(130, mounting_media)
    pipette.dispense(130, mounting_media)
pipette.drop_tip()

# Add secondary antibody to cells
pipette.pick_up_tip()
pipette.aspirate(50, secondary_antibody)
for cell in cells:
    pipette.dispense(30, cell)
    pipette.mix(3, 50)
pipette.drop_tip()

# Incubate cells with secondary antibody
robot.pause("Incubate cells with secondary antibody for 30 minutes.")

# Remove secondary antibody from cells
for cell in cells:
    pipette.aspirate(30, cell)
    pipette.blow_out()

# Wash cells with PBS
pipette.pick_up_tip()
for i in range(3):
    for cell in cells:
        pipette.aspirate(130, cell)
        pipette.dispense(130, cell)
    pipette.aspirate(130, mounting_media)
    pipette.dispense(130, mounting_media)
pipette.drop_tip()

# Add mounting media to cells
pipette.pick_up_tip()
for cell in cells:
    pipette.aspirate(150, mounting_media)
    pipette.dispense(150, cell)
pipette.drop_tip()

# Incubate cells with mounting media
robot.pause("Incubate cells with mounting media for 30 minutes.")

# Done!
