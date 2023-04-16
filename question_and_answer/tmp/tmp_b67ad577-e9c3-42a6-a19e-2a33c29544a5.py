import opentrons.execute
from opentrons.protocol_api import ProtocolContext, labware
from opentrons.types import Point

def run(protocol: ProtocolContext):
    # Let's define the main function 'run' for the protocol.
    
    # Load the labware
    # Replace 'corning_6_wellplate_16.8ml_flat' with specific labware
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1) # Load the 6 well plate
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2) # Load 300µL tiprack for immunostaining

    # Define pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Protocol
    # Load the reagents, adapt slot number accordingly
    reagent_plate = protocol.load_labware('corning_24_wellplate_3.4ml_flat', 3)

    lysosome_stain = reagent_plate.wells_by_name()['A1'] # Lysosome stain
    fixative = reagent_plate.wells_by_name()['B1'] # Fixative
    wash_buffer = reagent_plate.wells_by_name()['C1'] # Wash buffer

    # Immunostaining
    for well in well_plate.wells():
        # Lysosome staining
        pipette.pick_up_tip()
        pipette.aspirate(100, lysosome_stain) # Adjust the volume based on your experimental conditions
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.mix(5, 100) # Mix 5 times
        pipette.drop_tip()

    # Incubate at 37°C for 1 hour (as an example)
    protocol.delay(minutes=60)

    for well in well_plate.wells():
        # Fix cells
        pipette.pick_up_tip()
        pipette.aspirate(100, fixative) # Adjust the volume based on your experimental conditions
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.mix(5, 100) # Mix 5 times
        pipette.drop_tip()

    # Incubate at 37°C for 15 minutes (as an example)
    protocol.delay(minutes=15)

    for well in well_plate.wells():
        # Washing
        pipette.pick_up_tip()
        pipette.aspirate(100, wash_buffer) # Adjust the volume based on your experimental conditions
        pipette.dispense(100, well)
        pipette.blow_out()
        pipette.mix(5, 100) # Mix 5 times
        pipette.drop_tip()

if __name__ == "__main__":
    import sys
    from opentrons import simulate, execute
    protocol = simulate.get_protocol_api("2.10")
    run(protocol)

