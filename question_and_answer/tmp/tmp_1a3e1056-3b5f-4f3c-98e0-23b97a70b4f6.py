
import opentrons

# robot setup
robot = opentrons.Robot()
robot.home()

# labware setup
tip_rack = robot.load_labware('opentrons_96_tiprack_1000ul', '1')
tubes = robot.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '6')
plate = robot.load_labware('biorad_96_wellplate_200ul_pcr', '7')

# pipette setup
pipette = robot.load_instrument( 'p300_multi', 'left', tip_racks=[tip_rack])

# seeding A549 cells
pipette.pick_up_tip(tip_rack.wells('A1'))
pipette.aspirate(60, tubes.wells('A1'))
pipette.dispense(60, plate.wells('A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'E1', 'E2', 'E3', 'E4', 'F1', 'F2', 'F3', 'F4', 'G1', 'G2', 'G3', 'G4', 'H1', 'H2', 'H3', 'H4'))
pipette.drop_tip()

# adding negative control medium
pipette.pick_up_tip(tip_rack.wells('A2'))
pipette.aspirate(60, tubes.wells('B2'))
pipette.dispense(60, plate.wells('A5', 'B5', 'C5'))
pipette.drop_tip()

# adding initial stocks
pipette.pick_up_tip(tip_rack.wells('A3'))
pipette.aspirate(35, tubes.wells('A1'))
pipette.dispense(35, tubes.wells('A2', 'A3', 'A4', 'A5', 'A6', 'B1'))
pipette.drop_tip()

# adding 4X concentrations
pipette.pick_up_tip(tip_rack.wells('A4'))
pipette.aspirate(100, tubes.wells('A2'))
pipette.dispense(100, tubes.wells('C1', 'C2', 'C3', 'C4', 'C5', 'C6'))
pipette.aspirate(100, tubes.wells('A3'))
pipette.dispense(100, tubes.wells('D1', 'D2', 'D3', 'D4', 'D5', 'D6'))
pipette.aspirate(100, tubes.wells('A4'))
pipette.dispense(100, tubes.wells('E1', 'E2', 'E3', 'E4', 'E5', 'E6'))
pipette.aspirate(100, tubes.wells('A5'))
pipette.dispense(100, tubes.wells('F1', 'F2', 'F3', 'F4', 'F5', 'F6'))
pipette.aspirate(100, tubes.wells('A6'))
pipette.dispense(100, tubes.wells('G1', 'G2', 'G3', 'G4', 'G5', 'G6'))
pipette.aspirate(100, tubes.wells('B1'))
pipette.dispense(100, tubes.wells('H1', 'H2', 'H3', 'H4', 'H5', 'H6'))
pipette.drop_tip()

# adding 2X concentrations
pipette.pick_up_tip(tip_rack.wells('A5'))
pipette.aspirate(100, tubes.wells('C1'))
pipette.dispense(100, tubes.wells('C1'))
pipette.aspirate(100, tubes.wells('C3'))
pipette.dispense(100, tubes.wells('C3'))
pipette.aspirate(100, tubes.wells('C5'))
pipette.dispense(100, tubes.wells('C5'))
pipette.aspirate(100, tubes.wells('D1'))
pipette.dispense(100, tubes.wells('D1'))
pipette.aspirate(100, tubes.wells('D3'))
pipette.dispense(100, tubes.wells('D3'))
pipette.aspirate(100, tubes.wells('D5'))
pipette.dispense(100, tubes.wells('D5'))
pipette.drop_tip()

# adding thapsigargin to 96 well plate
pipette.pick_up_tip(tip_rack.wells('A6'))
pipette.aspirate(60, tubes.wells('C1'))
pipette.dispense(60, plate.wells('A1', 'B1', 'C1'))
pipette.aspirate(60, tubes.wells('C2'))
pipette.dispense(60, plate.wells('A2', 'B2', 'C2'))
pipette.aspirate(60, tubes.wells('C3'))
pipette.dispense(60, plate.wells('A3', 'B3', 'C3'))
pipette.aspirate(60, tubes.wells('C4'))
pipette.dispense(60, plate.wells('A4', 'B4', 'C4'))
pipette.aspirate(60, tubes.wells('C5'))
pipette.dispense(60, plate.wells('A5', 'B5', 'C5'))
pipette.aspirate(60, tubes.wells('C6'))
pipette.dispense(60, plate.wells('A6', 'B6', 'C6'))
pipette.aspirate(60, tubes.wells('D1'))
pipette.dispense(60, plate.wells('D1', 'E1', 'F1'))
pipette.aspirate(60, tubes.wells('D2'))
pipette.dispense(60, plate.wells('D2', 'E2', 'F2'))
pipette.aspirate(60, tubes.wells('D3'))
pipette.dispense(60, plate.wells('D3', 'E3', 'F3'))
pipette.aspirate(60, tubes.wells('D4'))
pipette.dispense(60, plate.wells('D4', 'E4', 'F4'))
pipette.aspirate(60, tubes.wells('D5'))
pipette.dispense(60, plate.wells('D5', 'E5', 'F5'))
pipette.aspirate(60, tubes.wells('D6'))
pipette.dispense(60, plate.wells('D6', 'E6', 'F6'))
pipette.aspirate(60, tubes.wells('E1'))
pipette.dispense(60, plate.wells('G1', 'H1'))
pipette.aspirate(60, tubes.wells('E2'))
pipette.dispense(60, plate.wells('G2', 'H2'))
pipette.aspirate(60, tubes.wells('E3'))
pipette.dispense(60, plate.wells('G3', 'H3'))
pipette.aspirate(60, tubes.wells('E4'))
pipette.dispense(60, plate.wells('G4', 'H4'))
pipette.aspirate(60, tubes.wells('E5'))
pipette.dispense(60, plate.wells('G5', 'H5'))
pipette.aspirate(60, tubes.wells('E6'))
pipette.dispense(60, plate.wells('G6', 'H6'))
pipette.drop_tip()

# adding CellTox Green reagent
pipette.pick_up_tip(tip_rack.wells('A7'))
pipette.aspirate(15, tubes.wells('B2'))
pipette.dispense(15, plate.wells('A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5'))
pipette.drop_tip()

# orbital shaking and incubation
robot.pause()
robot.comment('Set the Heater Shaker to orbital shaking for 2 minutes at 500 rpm')
robot.comment('Once the orbital shaking of the heater shaker is complete, incubate the plate at RT for 15 min')
robot.resume()

# adding Cell Titer Glo 2.0 reagent
pipette.pick_up_tip(tip_rack.wells('A8'))
pipette.aspirate(80, tubes.wells('B1'))
pipette.dispense(80, plate.wells('A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1


:*************************


