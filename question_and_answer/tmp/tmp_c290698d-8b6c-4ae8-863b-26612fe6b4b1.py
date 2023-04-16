from opentrons import labware, instruments, robot

# Define labware
plate = labware.load('corning_6_wellplate_16.8ml_flat', '2')
tiprack = labware.load('opentrons_96_tiprack_300ul', '4')
reservoir = labware.load('nest_12_reservoir_15ml', '5')

# Define pipette
pipette = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack]
)

# Define reagents
scm130 = reservoir['A1']
pbs_minus = reservoir['A2']

# Define protocol
def run_protocol():
    # 1. Aspirate 200 uL of PBS(-) from the reservoir and dispense it into each well of the plate
    for well in plate:
        pipette.pick_up_tip()
        pipette.aspirate(200, pbs_minus)
        pipette.dispense(200, well)
        pipette.drop_tip()

    # 2. Wait for 5 mins
    robot.comment('Waiting for 5 minutes...')
    robot.pause(300)

    # 3. Aspirate 300 uL of SCM130 from the reservoir and dispense it into each well of the plate
    for well in plate:
        pipette.pick_up_tip()
        pipette.aspirate(300, scm130)
        pipette.dispense(300, well)
        pipette.drop_tip()

run_protocol()
