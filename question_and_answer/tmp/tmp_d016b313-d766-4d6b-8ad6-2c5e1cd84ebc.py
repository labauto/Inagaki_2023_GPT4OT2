# Import required modules
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Immunostaining hMSC cells',
    'author': 'Your Name Here',
    'description': 'Prepare and immunostain hMSC cells in a 6-well plate to visualize lysosomes',
}

# protocol run function. the part after the colon lets your editor know
# what Python version to use.
def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8 ml', '1')

    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '2')

    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # Distribute fixative (4% paraformaldehyde) to each well
    p20.distribute(18, plate['A1'].bottom(2), [well.bottom(2) for well in plate.wells()])

    # Incubate for 10 minutes at room temperature
    protocol.delay(minutes=10)

    # Remove fixative and wash cells with PBS
    for well in plate.wells():
        # Discard supernatant
        p20.transfer(16, well.bottom(2), tiprack_20['A1'].bottom(2))
        # Wash cells with PBS
        p20.transfer(20, protocol.load_labware('nest_12_reservoir_15ml', '3')['A1'].bottom(2), well.bottom(2),
                     mix_before=(2, 15), new_tip='always')

    # Block non-specific binding with 1% BSA/PBS
    for well in plate.wells():
        p20.distribute(17, protocol.load_labware('nest_12_reservoir_15ml', '3')['A2'], well.bottom(2))

    # Incubate for 30 minutes at room temperature
    protocol.delay(minutes=30)

    # Remove BSA and add primary antibody (LAMP-1)
    for well in plate.wells():
        # Discard supernatant
        p20.transfer(20, well.bottom(2), tiprack_20['A1'].bottom(2))
        # Add primary antibody
        p20.transfer(20, protocol.load_labware('nest_12_reservoir_15ml', '3')['A3'], well.bottom(2), new_tip='always')

    # Incubate for 1 hour at room temperature
    protocol.delay(minutes=60)

    # Remove primary antibody and wash with PBS
    for well in plate.wells():
        # Discard supernatant
        p20.transfer(20, well.bottom(2), tiprack_20['A1'].bottom(2))
        # Wash cells with PBS
        p20.transfer(40, protocol.load_labware('nest_12_reservoir_15ml', '3')['A1'].bottom(2), well.bottom(2),
                     mix_before=(4, 15), new_tip='always')

    # Add secondary antibody
    for well in plate.wells():
        p20.transfer(20, protocol.load_labware('nest_12_reservoir_15ml', '3')['A4'], well.bottom(2), new_tip='always')

    # Incubate for 1 hour at room temperature
    protocol.delay(minutes=60)

    # Wash with PBS
    for well in plate.wells():
        p20.transfer(40, protocol.load_labware('nest_12_reservoir_15ml', '3')['A1'].bottom(2), well.bottom(2),
                     mix_before=(4, 15), new_tip='always')

    # Add DAPI (nuclear staining)
    for well in plate.wells():
        p20.transfer(20, protocol.load_labware('nest_12_reservoir_15ml', '3')['A5'], well.bottom(2), new_tip='always')
