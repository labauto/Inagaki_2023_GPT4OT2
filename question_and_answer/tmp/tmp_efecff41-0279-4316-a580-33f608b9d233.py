from opentrons import robot, containers, instruments

# define the containers and instruments we will use
plate = containers.load("6-well", "A1")
pbs = containers.load("trough-12row", "B1")
dmem = containers.load("trough-12row", "C1")
pipette = instruments.P300_Single(mount="left")

# aspirate PBS(-).
pipette.pick_up_tip()
pipette.aspirate(200,pbs)

# dispense PBS(-).
for well in plate.wells():
    pipette.dispense(200, well)

# aspirate D-MEM.
pipette.aspirate(200, dmem)

# dispense D-MEM.
for well in plate.wells():
    pipette.dispense(200, well)

# drop tip.
pipette.drop_tip()


:*************************


