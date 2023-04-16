# Import the required modules
from opentrons import labware, instruments, robot

# Define the labware
plate = labware.load('6-well-plate', 'C2')
tiprack = labware.load('opentrons_96_tiprack_300ul', 'B2')

# Define the pipette and tiprack
p300 = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack]
)

# Define the volumes and movements for the transfer
total_volume = 200  # uL
pbs_volume = 100  # uL
dmem_volume = 100  # uL

# Define the locations for the PBS and D-MEM
pbs_location = 'A1'
dmem_location = 'A2'

# Loop through each well in the plate and perform the exchange
for well in plate.wells():
    # Aspirate the current medium from the well
    p300.aspirate(total_volume, well)

    # Dispense the PBS into the well
    p300.dispense(pbs_volume, robot.deck[pbs_location])
    p300.mix(5, pbs_volume, well)  # Mix the medium for 5 times

    # Aspirate the PBS from the well
    p300.aspirate(pbs_volume, well)

    # Dispense the D-MEM into the well
    p300.dispense(dmem_volume, robot.deck[dmem_location])
    p300.mix(5, dmem_volume, well)  # Mix the medium for 5 times

    # Aspirate the D-MEM from the well
    p300.aspirate(dmem_volume, well)
  
    # Dispense the exchanged medium back into the well
    p300.dispense(total_volume, well)
