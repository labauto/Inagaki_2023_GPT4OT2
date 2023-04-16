metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Your Name',
    'description': 'Protocol for creating hMSC spheroids in 96 well plates.',
    'apiLevel': '2.10'
}

def transfer_medium(pipette, source, dest):
    """Transfer 100 µl of medium to each well specified in the destination."""
    pipette.transfer(100, source, dest, new_tip='always')

def add_osteo_supplements(pipette, dex_source, aa_source, bgp_source, dest):
    """Add 0.1 µl of Dex, 1 µl of AA, and 1 µl of BGP to each specified well."""
    pipette.transfer(0.1, dex_source, dest, new_tip='once')
    pipette.transfer(1, aa_source, dest, new_tip='once')
    pipette.transfer(1, bgp_source, dest, new_tip='once')

def transfer_cells(pipette, source, dest):
    """Transfer 100 µl of hMSC cells to each well specified in the destination."""
    pipette.transfer(100, source, dest, new_tip='always')

def run(protocol):
    # Load labware
    medium_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    cell_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    osteo_supplements = protocol.load_labware('nest_12_reservoir_15ml', '4')

    # Define pipettes
    p50_single = protocol.load_instrument('p50_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_filtertiprack_20ul', '5')])

    # Transfer medium to each well of both plates
    transfer_medium(p50_single, medium_plate.wells(), cell_plate.wells())
    transfer_medium(p50_single, medium_plate.wells_by_name()['A1'], cell_plate.wells_by_name()['A1'])

    # Add osteoinduction supplements
    add_osteo_supplements(p50_single, osteo_supplements.wells_by_name()['A1'],
                          osteo_supplements.wells_by_name()['A2'],
                          osteo_supplements.wells_by_name()['A3'], cell_plate.wells_by_name()['A1'])

    # Transfer hMSC cells to each well of both plates
    cell_source = protocol.load_labware('thermofisher_96_wellplate_280ul', '3')
    transfer_cells(p50_single, cell_source.columns()[0][0], cell_plate.wells())
    transfer_cells(p50_single, cell_source.columns()[0][0], cell_plate.wells_by_name()['A1'])
