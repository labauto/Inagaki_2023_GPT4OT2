from opentrons import labware, instruments
from opentrons.util import environment

# Check if running in simulation and choose corresponding API version
if environment.is_api_version_2():
    from opentrons.protocol_api.labware import OutdatedApiVersionError

# Load custom labware
custom_plate = labware.load('6-well-plate_SAMPLE', '2')

# Initialise pipette
p300 = instruments.P300_Single(mount='right')

# Define volume parameters
dmem_vol = 250
pbs_vol = 1000

# Define well locations
DMEM_well = custom_plate.wells('A1')
PBS_well = custom_plate.wells('B1')

# Protocol
def run(protocol_context):

    # Aspirate DMEM medium from well A1
    p300.aspirate(dmem_vol, DMEM_well)

    # Dispense DMEM medium into waste
    p300.dispense(dmem_vol)

    # Repeat aspirate/dispense with PBS medium
    p300.aspirate(pbs_vol, PBS_well)
    p300.dispense(pbs_vol)
