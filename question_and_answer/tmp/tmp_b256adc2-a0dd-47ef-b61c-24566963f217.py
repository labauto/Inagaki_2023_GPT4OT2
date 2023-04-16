from opentrons import labware

# Load labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')

# Define wells
lysosome_stain = plate['C1']
