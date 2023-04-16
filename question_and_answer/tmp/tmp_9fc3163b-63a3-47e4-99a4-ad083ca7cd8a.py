import opentrons.execute
from opentrons import protocol_api

# Metadata (has to be placed in the main directory of the protocol api)
metadata = {
    'protocolName': 'Preparing Immunostained hMSC Cells',
    'author': 'Your Name',
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

    # Define labware
    plate_6_well = protocol.load_labware("corning_6_wellplate_16.8ml_flat", "11")
    reagent_rack = protocol.load_labware("opentrons_24_aluminumblock_generic_2ml_screwcap", "10")
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '7')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')

    # Define pipettes
    p50 = protocol.load_instrument("p50_single", "left", tip_racks=[tiprack_200])
    p300 = protocol.load_instrument("p300_single", "right", tip_racks=[tiprack_300])

    # Define reagents
    fixative_solution = reagent_rack.wells_by_name()['A1']
    permeabilization_solution = reagent_rack.wells_by_name()['B1']
    blocking_solution = reagent_rack.wells_by_name()['C1']
    primary_antibody_solution = reagent_rack.wells_by_name()['D1']
    secondary_antibody_solution = reagent_rack.wells_by_name()['A2']

    # Perform the experiment
    for i in range(1, 7):
        well = plate_6_well.wells_by_name()[f"A{i}"]

        # Fixation step
        p300.pick_up_tip()
        p300.aspirate(200, fixative_solution)
        p300.dispense(200, well)
        p300.blow_out(well.top())
        p300.drop_tip()

        protocol.delay(minutes=15)  # Fixation time (can be adjusted)

        # Washing steps (repeat 3 times)
        for wash_round in range(3):
            # Remove fixative solution
            p300.pick_up_tip()
            p300.aspirate(200, well)
            p300.dispense(200, fixative_solution)
            p300.blow_out(fixative_solution.top())
            p300.drop_tip()

            # Add permeabilization solution
            p300.pick_up_tip()
            p300.aspirate(200, permeabilization_solution)
            p300.dispense(200, well)
            p300.blow_out(well.top())
            p300.drop_tip()

            protocol.delay(minutes=5)   # Washing time (can be adjusted)

            # Remove permeabilization solution
            p300.pick_up_tip()
            p300.aspirate(200, well)
            p300.dispense(200, permeabilization_solution)
            p300.blow_out(permeabilization_solution.top())
            p300.drop_tip()

        # Blocking step
        p300.pick_up_tip()
        p300.aspirate(200, blocking_solution)
        p300.dispense(200, well)
        p300.blow_out(well.top())
        p300.drop_tip()

        protocol.delay(minutes=60)  # Blocking time (can be adjusted)

        # Primary antibody incubation
        p50.pick_up_tip()
        p50.aspirate(50, primary_antibody_solution)
        p50.dispense(50, well)
        p50.blow_out(well.top())
        p50.drop_tip()

        protocol.delay(minutes=120)  # Primary antibody incubation time (can be adjusted)

        # Secondary antibody incubation
        p50.pick_up_tip()
        p50.aspirate(50, secondary_antibody_solution)
        p50.dispense(50, well)
        p50.blow_out(well.top())
        p50.drop_tip()

        protocol.delay(minutes=120)  # Secondary antibody incubation time (can be adjusted)

        # Add your imaging step here if needed (e.g. loading samples into the imaging device)
