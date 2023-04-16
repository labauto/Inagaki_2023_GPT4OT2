from opentrons import labware, instruments, modules, robot

# Define custom labware
tipracks = [labware.load('opentrons-tiprack-300ul', slot) for slot in ['1', '2', '3']]
tuberack_15ml = labware.load('opentrons-tuberack-15ml', '6')
plate_96_tc = labware.load('96-well-flat', '4')

# Define custom modules
tempdeck = modules.load('tempdeck', '7')
tempdeck.set_temperature(25)
tempplate = labware.load('96-well-PCR-flat', '7', share=True)

# Define pipettes
p300 = instruments.P300_Single(
    mount='left',
    tip_racks=tipracks)

# Define functions
def add_cells(volume):
    tube = tuberack_15ml.wells()[0]
    p300.pick_up_tip()

    for well in plate_96_tc.wells():
        p300.transfer(volume, tube, well, new_tip='never')

    p300.drop_tip()

def add_drug(concentration):
    concentration_4x = concentration * 4

    # Prepare drug dilution series
    slots = ['A', 'B', 'C', 'D']
    tubes = [tuberack_15ml.wells_by_name()[f"{slot}1"] for slot in slots]
    dilutions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    concentrations = [c * concentration_4x / d for d in dilutions for c in (1, 2)]

    # Add drug to dilution series
    for tube, conc in zip(tubes, concentrations):
        p300.pick_up_tip()
        p300.mix(3, 200, tube)
        p300.aspirate(20, tube)
        p300.dispense(20, tube)
        p300.transfer(20, tube, tube.bottom(2), new_tip='never')
        p300.pick_up_tip()
        p300.mix(3, 50, tube)
        p300.aspirate(25, tube)
        p300.dispense(25, tube)
        p300.transfer(25, tube, tempplate.cols_by_name()[f"{tube.get_name()[-1]}"], new_tip='never')
        p300.drop_tip()

    # Add drug to plate
    cols = plate_96_tc.cols_by_name()
    conc_cols = ['A', 'B', 'C', 'D', 'E', 'F']
    for col, conc_col in zip(cols, conc_cols):
        p300.transfer(25, tempplate.cols_by_name()[conc_col], col, mix_before=(3, 50), new_tip='always')

# Define variables
NUM_CELLS = 8000
VOLUME_PER_WELL = 60
THAPSIGARGIN_CONCENTRATION = 1  # in mM

# Set up robot
robot.home()

# Clean the robot with 70 % ethanol and turn on the HEPA filter
robot._driver.enable_button()
robot.pause("Please clean the robot with 70% ethanol and turn on the HEPA filter at low fan speed. Press resume when done.")

# Add cells to the plate
add_cells(NUM_CELLS * VOLUME_PER_WELL / 1000)

# Add thapsigargin to the plate
add_drug(THAPSIGARGIN_CONCENTRATION)

# Measure cell viability
p300.pick_up_tip()
for row in plate_96_tc.rows()[:4]:
    p300.transfer(15, tempdeck.wells()[0], row, new_tip='never')
p300.drop_tip()

robot.pause("Please incubate the plate at RT for 15 min. Press resume when done.")

robot.home()

for row in plate_96_tc.rows()[:4]:
    p300.pick_up_tip()
    p300.transfer(80, tempdeck.wells()[1], row, new_tip='never')
    p300.mix(3, 50, row)
    p300.transfer(80, row, tempdeck.wells()[1], new_tip='never')
    p300.drop_tip()

robot.pause("Please incubate the plate at RT for 10 min. Press resume when done.")

robot.home()

luminescence_data = []
for row in plate_96_tc.rows()[:4]:
    luminescence_data.append(p300.transfer(20, tempdeck.wells()[1], row, new_tip='always'))

for data in luminescence_data:
    robot.pause(f"Luminescence value: {data}")

robot.home()
