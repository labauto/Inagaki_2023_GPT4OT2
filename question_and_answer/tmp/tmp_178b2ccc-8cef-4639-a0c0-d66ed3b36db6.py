
import opentrons 

# initiate robot
robot = opentrons.Robot()

# clean the inside of the robot with 70 % ethanol
robot.home()
robot.clear_commands()

# turn on the HEPA filter at low fan speed for about an hour 
robot.commands.set_flow_rate(aspirate=20, dispense=20, blow_out=50)
robot.commands.set_fan_speed('low')

# seed A549 cells
# take a 24–48 hours old T-75 flask of A549 cells
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=200, location='T-75 flask of A549 cells')
robot.commands.dispense(volume=200, location='96 well plate')
robot.commands.blow_out()

# take a cell count using the automated Countess 3 machine
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=20, location='Countess 3 machine')
robot.commands.dispense(volume=20, location='96 well plate')
robot.commands.blow_out()

# adjust the cell volume in 10% Ham’s F12K medium
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=60, location='10% Ham’s F12K medium')
robot.commands.dispense(volume=60, location='96 well plate')
robot.commands.blow_out()

# dispense the cell suspension into ten 1.5mL snap-capped tubes
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=225, location='cell suspension')
robot.commands.dispense(volume=225, location='1.5mL snap-capped tubes')
robot.commands.blow_out()

# dilutions of the drug (thapsigargin)on the second day
# prepare the initial stocks ranging from 10nM to 100microM
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=35, location='initial stocks')
robot.commands.dispense(volume=35, location='A1 in slot 7')
robot.commands.blow_out()

# prepare dilutions of various concentrations of thapsigargin
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=100, location='4X concentrations')
robot.commands.dispense(volume=100, location='C1 to C6 and D1 to D6')
robot.commands.blow_out()

# prepare 2X concentrations of thapsigargin
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=100, location='4X concentration')
robot.commands.dispense(volume=100, location='C1 to C3, C5 to D6')
robot.commands.blow_out()

# add the equal volume of 2X thapsigargin to each well of 96 well plate
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=100, location='2X thapsigargin')
robot.commands.dispense(volume=100, location='96 well plate')
robot.commands.blow_out()

# add CellTox Green reagent from B2 of the Opentrons 10 tube rack
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=15, location='CellTox Green reagent')
robot.commands.dispense(volume=15, location='A1 of 96 well plate')
robot.commands.blow_out()

# set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm
robot.commands.set_shaker_speed('orbital', rpm=500)
robot.commands.shaker_for(duration=120)

# incubate the plate at RT for 15 min
robot.commands.set_temperature(20)
robot.commands.wait_for_temperature(target_temperature=20, timeout=900)

# read the fluorescence at 485 nm excitation and 520 nm emission
robot.commands.read_fluorescence(excitation_wavelength=485, emission_wavelength=520)

# add 80microL of Cell Titer Glo 2.0 reagent from B1 of the Opentrons 10 tube rack
robot.commands.pick_up_tip()
robot.commands.aspirate(volume=80, location='Cell Titer Glo 2.0 reagent')
robot.commands.dispense(volume=80, location='A1 of 96 well plate')
robot.commands.blow_out()

# set the Heater shaker to orbital shaking at 500 rpm for 2 minutes
robot.commands.set_shaker_speed('orbital', rpm=500)
robot.commands.shaker_for(duration=120)

# incubate at RT for 10 minutes
robot.commands.set_temperature(20)
robot.commands.wait_for_temperature(target_temperature=20, timeout=600)

# read the plate for luminescence
robot.commands.read_luminescence()

# end robot.
robot.home()
robot.clear_commands()


:*************************


