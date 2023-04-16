import opentrons
from opentrons import protocol_api

metadata = {
    "apiLevel": "2.10"
}

# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    # Define labware and reagents
    plate = protocol.load_labware("corning_6_wellplate_16.8ml_flat", 1)
    tiprack_20ul = protocol.load_labware("opentrons_96_tiprack_20ul", 2)
    tuberculin_tips = protocol.load_labware("opentrons_96_filtertiprack_10ul", 3)
    media_tube = protocol.load_labware("opentrons_24_tuberack_generic_2ml_screwcap", 4)
    
    # Define pipettes
    p20 = protocol.load_instrument("p20_single_gen2", "right", tip_racks=[tiprack_20ul])
    p10 = protocol.load_instrument("p10_single", "left", tip_racks=[tuberculin_tips])

    # Add reagents to appropriate wells
    wells_to_fill = plate.wells_by_name()
    cells = media_tube.wells_by_name()["A1"]  # well containing cells
    l_medium = media_tube.wells_by_name()["A2"]  # well containing culture medium
    lysotracker = media_tube.wells_by_name()["A3"]  # well containing LysoTracker dye

    # Prepare immunostained hMSC cells to visualize lysosomes
    for well_name in ["A1", "A2", "A3", "B1", "B2", "B3"]:
        p20.pick_up_tip()
        p20.aspirate(10, cells)
        p20.dispense(10, wells_to_fill[well_name])
        p20.drop_tip()

        p20.pick_up_tip()
        p20.aspirate(500, l_medium)
        p20.dispense(500, wells_to_fill[well_name])
        p20.drop_tip()

        p10.pick_up_tip()
        p10.aspirate(1, lysotracker)
        p10.dispense(1, wells_to_fill[well_name])
        p10.drop_tip()

        # Incubate at 37C for 1h
        # Opentrons do not have any incubation function, you can either manually incubate the plate
        # or integrate the incubation function with other automated laboratory equipment.
    protocol.comment("Incubate plate at 37°C for 1h.")
        

# Run the protocol
if __name__ == '__main__':
    from opentrons import simulate
    import sys

    protocol = simulate.get_protocol_api('2.10')
    run(protocol)
    for line in protocol.commands():
        print(line)
