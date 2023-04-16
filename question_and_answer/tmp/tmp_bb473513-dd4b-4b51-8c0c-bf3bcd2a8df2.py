# Import the Opentrons API v2 library
import opentrons.protocol_api as api

# metadata
metadata = {
    'protocolName': 'Cell Culture Medium Exchange',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and SCM130. The cell is cultured in 6 well plate.',
    'apiLevel': '2.0'
}

# protocol run function
def run(protocol: api.ProtocolContext):
    
    # Load labware
    culture_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    p300_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')

    # Load pipette
    pipette = protocol.load_instrument('p300_multi', mount='left', tip_racks=[p300_tip_rack])

    # Define locations
    well_A1 = culture_plate['A1']
    wells_to_transfer = culture_plate.wells()[:5]
    pbs_col = 10
    scm_col = 11

    # Perform transfer
    pipette.pick_up_tip()
    for well in wells_to_transfer:
        pipette.transfer(900, well.bottom(1), reservoir.cols[pbs_col][0], new_tip='never')
        pipette.transfer(900, well.bottom(1), reservoir.cols[scm_col][0], new_tip='never')
        pipette.blow_out()
    pipette.drop_tip()
