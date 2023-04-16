# Import necessary modules
from opentrons import labware, instruments, protocol_api

# Define metadata
metadata = {
    'protocolName': 'Immunostaining of hMSC cells for lysosome visualization',
    'author': 'Your Name Here',
    'description': 'Prepare immunostained hMSC cells to visualize lysosomes.',
    'apiLevel': '2.0'
}

# Define protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '2')
    p300_tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Load instruments
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[p300_tiprack])

    # Define variables
    buffer_volume = 15.6  # uL
    antibody_volume = 3.9  # uL
    sample_volume = 1.56  # uL
    wash_volume = 31.2  # uL

    # Define reagents
    buffer = plate.columns_by_name()['1'][0]
    antibody = plate.columns_by_name()['2'][0]
    sample = plate.columns_by_name()['3'][0]

    # Distribute buffer
    p300.pick_up_tip()
    for well in buffer:
        p300.aspirate(buffer_volume, buffer)
        p300.dispense(buffer_volume, well.top())
        p300.blow_out()
    p300.drop_tip()

    # Distribute antibody
    p20.pick_up_tip()
    for well in antibody:
        p20.aspirate(antibody_volume, antibody)
        p20.dispense(antibody_volume, well.top())
        p20.blow_out()
    p20.drop_tip()

    # Incubate for 20 minutes
    protocol.delay(minutes=20)

    # Add sample and wash
    for well in sample:
        p20.pick_up_tip()
        p20.aspirate(sample_volume, sample)
        p20.dispense(sample_volume, well.top())
        p20.mix(5, 10)
        p20.blow_out()
        p20.drop_tip()

        p300.pick_up_tip()
        p300.aspirate(wash_volume, buffer)
        p300.dispense(wash_volume, well.top())
        p300.blow_out()
        p300.drop_tip()

    # Air dry for 10 minutes
    protocol.delay(minutes=10)

    # End of protocol
    protocol.comment('Immunostaining protocol complete')
