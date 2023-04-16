import opentrons.execute
from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Culture Medium Exchange',
    'author': 'Your Name',
    'description': 'Protocol for exchanging hMSC cell culture medium using PBS(-) and D-MEM in a 6-well plate',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '1')
    pbs_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    dmem_tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '3')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200ul])

    # Reagents
    pbs = pbs_reservoir.wells_by_name()['A1']
    dmem = dmem_tube_rack.wells_by_name()['A1']

    # Cell culture wells
    well_names = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
    cell_wells = [six_well_plate.wells_by_name()[well_name] for well_name in well_names]

    # Protocol
    ## Remove PBS(-)
    for well in cell_wells:
        p300.pick_up_tip()
        p300.aspirate(200, well.bottom(1))
        p300.dispense(200, pbs.top()) # Dispose of the old medium
        p300.drop_tip()

    ## Add D-MEM to cell culture
    p300.pick_up_tip()
    for well in cell_wells:
        p300.aspirate(200, dmem)
        p300.dispense(200, well)
        p300.blow_out()
    p300.drop_tip()

    protocol.comment("hMSC Culture Medium Exchange is complete.")
