import opentrons.protocols
from opentrons import labware, instruments, robot

metadata = {'apiLevel': '2.8'}

def run(protocol):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')

    # Load pipette
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1000])

    # Define samples
    wells = plate.wells()[0:4]

    # Add reagent to wells
    for well in wells:
        p1000.pick_up_tip()
        p1000.mix(2, 800, well) # aspirate and dispense 800 ul twice
        p1000.air_gap(20) # add a 20 ul air gap
        p1000.drop_tip()

    # Wait 10 minutes for reagent incubation
    protocol.delay(minutes=10)

    # Wash wells
    for well in wells:
        p1000.pick_up_tip()
        p1000.aspirate(1000, well) # aspirate reagent
        p1000.air_gap(20) # add a 20 ul air gap
        p1000.dispense(1020, well.top().move(-1*robot._deck['A']['labware'][0].parameters['depth'])) # dispense wash buffer
        p1000.blow_out() # dispense any remaining fluid
        p1000.drop_tip()
