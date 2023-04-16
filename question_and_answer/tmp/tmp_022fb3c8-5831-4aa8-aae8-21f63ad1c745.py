from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '1')

p200 = instruments.Pipette(
    name='p200',
    trash_container=plate,
    tip_racks=[],
    min_volume=20,
    max_volume=200,
    axis="a",
)

# Define columns and wells to be used
wells = [well for row in plate.rows() for well in row]
PBS_wells = wells[0:3]
DMEM_wells = wells[3:]

# Define volumes
PBS_volume = 200  # uL
DMEM_volume = 500  # uL

# Exchanging media
robot.comment("Exchanging hMSC cell culture medium using PBS(-) and D-MEM")
for i in range(2):
    # Dispense PBS into wells
    p200.distribute(
        PBS_volume,
        PBS_wells,
        disposal_volume=20
    )
    robot.pause("Incubate for 5 minutes")
    # Remove PBS from wells
    p200.transfer(
        200,
        PBS_wells,
        plate['A1'].top(),
        disposal_volume=20,
        new_tip='always'
    )
    # Dispense DMEM into wells
    p200.distribute(
        DMEM_volume,
        DMEM_wells,
        disposal_volume=20
    )
    robot.pause("Incubate for 30 minutes")
    # Remove DMEM from wells
    p200.transfer(
        500,
        DMEM_wells,
        plate['A1'].top(),
        disposal_volume=20,
        new_tip='always'
    )
