# Import necessary libraries
from opentrons import robot, containers, instruments

# Labware and Pipettes
plate = containers.load("96-flat", "2")
stocks_rack = containers.load("tube-rack-2ml", "7")
dilution1_rack = containers.load("tube-rack-2ml", "6")
dilution2_rack = containers.load("tube-rack-2ml", "5")
tip_rack_20ul = containers.load("tiprack-10ul", "10")
tip_rack_200ul = containers.load("tiprack-200ul", "4")
reagents_rack = containers.load("tube-rack-50ml", "3")

p20 = instruments.Pipette(
    axis="b",
    name="p20",
    min_volume=1,
    max_volume=20,
    channels=1,
    tip_racks=[tip_rack_20ul],
    trash_container=robot.fixed_trash,
)

p200 = instruments.Pipette(
    axis="a",
    name="p200",
    min_volume=20,
    max_volume=200,
    channels=1,
    tip_racks=[tip_rack_200ul],
    trash_container=robot.fixed_trash,
)

# Custom functions


def mix_tube(volume, times, pipette, source):
    for _ in range(times):
        pipette.aspirate(volume, source)
        pipette.dispense(source)


# Constants
control_rows = ["A", "B", "C"]
concentrations = [
    ("D", 0.39),
    ("E", 0.39),
    ("F", 0.39),
    ("G", 0.39),
    ("H", 0.39),
    ("A", 500),
    ("B", 500),
    ("C", 500),
    ("D", 500),
    ("E", 500),
    ("F", 500),
]

# Seeding, addition of thapsigargin, and incubation
for row, conc in concentrations:
    for well in plate.rows(row):
        p200.pick_up_tip()
        p200.transfer(60, dilution1_rack.wells("C1"), well.top())
        p200.drop_tip()

# Addition of CellTox Green reagent
for well in plate.wells():
    p20.pick_up_tip()
    p20.transfer(15, reagents_rack.wells("B2"), well.top(), mix_before=(3, 15), new_tip="never")
    p20.drop_tip()

# Shaking and incubation
robot.comment("Shaking for 2 minutes at 500 rpm.")
robot.comment("Incubating at room temperature for 15 minutes.")

# Addition of Cell Titer Glo 2.0 reagent
for well in plate.wells():
    p200.pick_up_tip()
    p200.transfer(80, reagents_rack.wells("B1"), well.top(), mix_before=(3, 80), new_tip="never")
    p200.drop_tip()

# Shaking and incubation
robot.comment("Shaking for 2 minutes at 500 rpm.")
robot.comment("Incubating at room temperature for 10 minutes.")

# Plate reading to be done using microplate reader
robot.comment("Remove the plate from heater shaker and read the plate for luminescence.")
