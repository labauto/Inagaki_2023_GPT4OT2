# Import required modules from Opentrons SDK
from opentrons import protocol_api

# Metadata
metadata = {'apiLevel': '2.2'}

# Initialize protocol
def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '4')

    # Load pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])

    # Define reagent volumes
    wash_volume = 80
    antibody_volume = 20

    # Define transfer parameters
    wash_wells = [1, 3, 5]
    antibody_wells = [2, 4, 6]

    # Define source and destination wells
    wash_source = plate.wells_by_name()['A1']
    antibody_source = plate.wells_by_name()['B1']

    # Wash steps
    for well in wash_wells:
        wash_destination = plate.wells()[well]
        p20.pick_up_tip()
        p20.transfer(wash_volume, wash_source, wash_destination, new_tip='never')
        p20.drop_tip()

    # Antibody steps
    for well in antibody_wells:
        antibody_destination = plate.wells()[well]
        p20.pick_up_tip()
        p20.transfer(antibody_volume, antibody_source, antibody_destination, new_tip='never')
        p20.mix(2, 10, antibody_destination)
        p20.drop_tip()
