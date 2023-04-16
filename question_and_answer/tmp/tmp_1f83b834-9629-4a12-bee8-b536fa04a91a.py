from opentrons import robot, containers, instruments

# Deck layout
plate = containers.load('6-well-plate', '2')
tips = containers.load('tiprack-200ul', '1')
pbs_reservoir = containers.load('trough-12row', '3', 'PBS(-)')
dmem_reservoir = containers.load('trough-12row', '4', 'D-MEM')
liquid_waste_reservoir = containers.load('trough-12row', '5', 'liquid_waste')

# Pipette setup
pipette_200 = instruments.Pipette(
    axis='b',
    max_volume=200,
    min_volume=20,
    tip_racks=[tips],
    channels=1,
)

def exchange_medium():
    # Exchange medium with PBS(-)
    for well in plate.wells():
        pipette_200.pick_up_tip()
        pipette_200.transfer(1000, pbs_reservoir['A1'], well, new_tip='never')
        pipette_200.mix(3, 200, well)
        pipette_200.transfer(1000, well, liquid_waste_reservoir['A1'], new_tip='never')
        pipette_200.drop_tip()

    # Perform a second wash with PBS(-)
    for well in plate.wells():
        pipette_200.pick_up_tip()
        pipette_200.transfer(1000, pbs_reservoir['A1'], well, new_tip='never')
        pipette_200.mix(3, 200, well)
        pipette_200.transfer(1000, well, liquid_waste_reservoir['A1'], new_tip='never')
        pipette_200.drop_tip()

    # Add D-MEM to each well
    for well in plate.wells():
        pipette_200.pick_up_tip()
        pipette_200.transfer(2000, dmem_reservoir['A1'], well, new_tip='never')
        pipette_200.drop_tip()

# Execute the protocol
exchange_medium()
robot.run()
