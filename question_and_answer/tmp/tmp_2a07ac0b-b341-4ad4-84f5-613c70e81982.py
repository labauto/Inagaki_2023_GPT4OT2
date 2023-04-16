from opentrons import robot, instruments, containers

# Setup Robot
robot.connect()

# Setup Containers
six_well_plate = containers.load('6-Well Plate', 'A1')
dmem = containers.load('Tuberack-50ml-Falcon', 'A2', 'DMEM')
pbs_minus = containers.load('Tuberack-50ml-Falcon', 'A3', 'PBS-minus')
trash = containers.load('trash-box', 'B2', 'Trash')

# Setup Pipettes
p200 = instruments.Pipette(
    axis='a',
    max_volume=200,
    min_volume=20,
    trash_container=trash,
    tip_racks=[container.load('tiprack-200ul')]
)

# Exchange Medium Protocol
p200.pick_up_tip()
p200.transfer(200, dmem, six_well_plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='never')
p200.drop_tip()

p200.pick_up_tip()
p200.transfer(200, pbs_minus, six_well_plate.wells('A1', 'A2', 'A3', 'B1', 'B2', 'B3'), new_tip='never')
p200.drop_tip()

# Disconnect Robot
robot.disconnect()


:*************************


