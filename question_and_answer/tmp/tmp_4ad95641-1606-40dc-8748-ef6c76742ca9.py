
from opentrons import devices, protocol_api

# variables
num_washes = 5
pbs_volume = 2
trypsin_volume = 3
medium_volume = 10

# create labware
trough = devices.container_type.DiTi(
    'trough-12row',
    'trough_12row',
    'My trough 12row'
)

cell_culture_dish = devices.container_type.WellPlate90(
    '96-PCR-flat',
    'cell_culture_dish',
    'Cell Culture Dish (90 mm)'
)

# create tips
p1000_tiprack = devices.tip_racks.find_by_name('Tip Rack 1000 µL')

# pipette
p1000 = devices.pipette.Pipette(
    axis='a',
    max_volume=1000,
    min_volume=0.2,
    tip_racks=[p1000_tiprack]
)

# Start the protocol
def run_custom_protocol():
    # wash the cell culture dish with PBS(-)
    for i in range(num_washes):
        p1000.pick_up_tip()
        p1000.aspirate(pbs_volume, trough.wells('A1'))
        p1000.dispense(pbs_volume, cell_culture_dish.wells('A1'))
        p1000.drop_tip()
        p1000.mix(pbs_volume, cell_culture_dish.wells('A1'), rate=5)
        p1000.blow_out()

    # add trypsin solution
    p1000.pick_up_tip()
    p1000.aspirate(trypsin_volume, trough.wells('A1'))
    p1000.dispense(trypsin_volume, cell_culture_dish.wells('A1'))
    p1000.drop_tip()
    p1000.delay(minutes=5)

    # add cell culture medium
    p1000.pick_up_tip()
    p1000.aspirate(medium_volume, trough.wells('A1'))
    p1000.dispense(medium_volume, cell_culture_dish.wells('A1'))
    p1000.drop_tip()

    # finish the experiment
    print("Experiment finished successfully!")

# run the protocol
run_custom_protocol()


:*************************


from opentrons import robot

robot.reset()

# Create the labware
cell_culture_dish = robot.load_labware('corning_96_wellplate_360ul_flat', '1')
tube_50ml = robot.load_labware('tube_50ml', '2')

# Create the pipettes
pipette = robot.load_instrument('p300_single', 'left', tip_racks=[])

# Protocol Steps
pipette.pick_up_tip()

for _ in range(5):
    # Dispense 2 ml of PBS(-)
    pipette.aspirate(2, tube_50ml.wells('A1'))
    # Wash cell culture dish
    pipette.dispense(2, cell_culture_dish.wells('A1'))
    # Pipette up and down
    pipette.mix(5, 150)

# Add 3 ml of trypsin solution (0.25%) to the cell culture dish
pipette.aspirate(3, tube_50ml.wells('A1'))
pipette.dispense(3, cell_culture_dish.wells('A1')) 

# Wait for 5 minutes
robot.pause('5:00') 

# Add 10 mL of cell culture medium (DMEM)
pipette.aspirate(10, tube_50ml.wells('A1'))
pipette.dispense(10, cell_culture_dish.wells('A1'))

# Finish the experiment
robot.home()


:*************************


