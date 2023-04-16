from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'hMSC Cell Culture Media Exchange',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate',
    'author': 'Your Name'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_trough = protocol.load_labware('nest_12_reservoir_15ml', '2')
    d_mem_trough = protocol.load_labware('nest_12_reservoir_15ml', '3')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Protocol
    pbs_well = pbs_trough.wells_by_name()['A1']
    d_mem_well = d_mem_trough.wells_by_name()['A1']

    # Constants for media exchange
    remove_volume = 2000
    add_volume = 2000

    for well in well_plate.wells():
        # Remove media with spent PBS(-)
        p300.pick_up_tip()
        p300.aspirate(remove_volume, well, rate=0.5)
        p300.dispense(remove_volume, pbs_well)
        p300.blow_out()
        p300.return_tip()

        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(add_volume, d_mem_well)
        p300.dispense(add_volume, well, rate=0.5)
        p300.blow_out()
        p300.return_tip()
