 #import OpenTrons
from opentrons import simulate

# Check simulator
simulate.get_protocol_api('2.1')

# Wash the cell culture dish with PBS(-)
pipette.pick_up_tip()
for _ in range(5):
    pipette.aspirate(2, PBS___Tube)
    pipette.dispense(2, Cell_Culture_Dish)
    pipette.blow_out()
pipette.drop_tip()

#add trypsin solution to the cell culture dish
pipette.pick_up_tip()
pipette.aspirate(3, Trypsin_Tube)
pipette.dispense(3, Cell_Culture_Dish)
pipette.blow_out()
pipette.drop_tip()

# Incubate for 5 minutes
# No code needed for incubation

#Add 10 ml of cell culture medium
pipette.pick_up_tip()
pipette.aspirate(10, Cell_Culture_Medium_Tube)
pipette.dispense(10, Cell_Culture_Dish)
pipette.blow_out()
pipette.drop_tip()

# Finish the Experiment
#No code needed to finish the experiment
