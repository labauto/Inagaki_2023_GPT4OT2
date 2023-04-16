from opentrons import protocol_api

metadata = {
    'protocolName': 'MSC Spheroid Culture',
    'author': 'Your Name <your.name@example.com>',
    'description': 'Automated MSC spheroid culture with two conditions, OS+ and OS-',
    'apiLevel': '2.0'
}


# Define the protocol
def run(protocol: protocol_api.ProtocolContext):
    # Load the labware
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8_ml_flat', '2')
    tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Load the pipettes
    pipette_300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300ul])

    # Define the transfer volumes
    medium_volume = 100  # uL
    supplement_volume = 0.1  # uL
    ascorbic_acid_volume = 1  # uL
    b_glycerophosphate_volume = 1  # uL

    # Define the source wells
    medium_source = plate_6_well.wells_by_name()['A1']
    supplement_source = plate_6_well.wells_by_name()['A2']
    ascorbic_acid_source = plate_6_well.wells_by_name()['A3']
    b_glycerophosphate_source = plate_6_well.wells_by_name()['A4']
    cell_source = plate_6_well.wells_by_name()['A5']

    # Distribute medium to all wells in the 96-well plates
    pipette_300.distribute(medium_volume, medium_source, plate_96_well.wells())

    # Add supplements to the OS+ wells
    pipette_300.transfer(
        supplement_volume,
        supplement_source,
        plate_96_well.rows_by_name()['A'][0:2],
        mix_before=(3, medium_volume/2),
        new_tip='always'
    )

    pipette_300.transfer(
        ascorbic_acid_volume,
        ascorbic_acid_source,
        plate_96_well.rows_by_name()['A'][0:2],
        mix_before=(3, medium_volume/2)
    )

    pipette_300.transfer(
        b_glycerophosphate_volume,
        b_glycerophosphate_source,
        plate_96_well.rows_by_name()['A'][0:2],
        mix_before=(3, medium_volume/2)
    )

    # Add cells to both plates
    pipette_300.transfer(
        medium_volume,
        cell_source,
        plate_96_well.wells(),
        mix_before=(3, medium_volume/2),
        new_tip='always'
    )
