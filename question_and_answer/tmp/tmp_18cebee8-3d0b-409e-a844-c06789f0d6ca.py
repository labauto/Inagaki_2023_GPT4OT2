!pip install opentrons

from opentrons import simulate, protocol_api

metadata = {
    'protocolName': 'iPS cell staining',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained iPS cells to visualize E-Cadherin in a 6-well plate',
}

# Create a `ProtocolContext` for simulation
ctx = simulate.get_protocol_api('2.5')

# Set up the pipettes
pipette = ctx.load_instrument('p300_single', 'right')

# Set up the labware
plate = ctx.load_labware('corning_6_wellplate_16.8ml_flat', '2')

# Define the starting well
start_well = 'A1'

# Define the volumes for each step
fix_volume = 200
wash_volume = 500
block_volume = 100
primary_volume = 50
secondary_volume = 50

# Define the reagents
fix_solution = ctx.load_labware(
    'opentrons_6_tuberack_falcon_50ml_conical', '1').wells()[0]
wash_solution = ctx.load_labware(
    'opentrons_6_tuberack_falcon_50ml_conical', '1').wells()[1]
block_solution = ctx.load_labware(
    'opentrons_6_tuberack_falcon_50ml_conical', '1').wells()[2]
primary_antibody = ctx.load_labware(
    'opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3').wells()[0]
secondary_antibody = ctx.load_labware(
    'opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3').wells()[1]

# Define the movement functions
def mix_and_dispense(pipette, volume, source, dest):
    pipette.mix(3, 200, source)
    pipette.transfer(volume, source, dest, new_tip='always',
                      mix_after=(3, 100))

def incubate(duration):
    ctx.delay(minutes=duration)

# Start the protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Add fix solution
    pipette.pick_up_tip()
    mix_and_dispense(pipette, fix_volume, fix_solution, plate[start_well])
    pipette.drop_tip()

    # Incubate for 10 minutes
    incubate(10)
    
    # Wash with wash solution
    for well in plate.wells():
        pipette.pick_up_tip()
        mix_and_dispense(pipette, wash_volume, wash_solution, well)
        pipette.drop_tip()

    # Block with block solution
    pipette.pick_up_tip()
    mix_and_dispense(pipette, block_volume, block_solution, plate[start_well])
    pipette.drop_tip()

    # Primary antibody incubation
    pipette.pick_up_tip()
    mix_and_dispense(pipette, primary_volume, primary_antibody, plate[start_well])
    incubate(60)
    pipette.drop_tip()

    # Secondary antibody incubation
    pipette.pick_up_tip()
    mix_and_dispense(pipette, secondary_volume, secondary_antibody, plate[start_well])
    incubate(60)
    pipette.drop_tip()

# Run the protocol
run(ctx)
