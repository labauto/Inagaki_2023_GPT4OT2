from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium',
    'author': 'Your Name',
    'description': 'Protocol for exchanging hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')

    # Load reagents
    pbs = protocol.load_labware('usascientific_12_reservoir_22ml', '2').wells()[0]
    dmem = protocol.load_labware('usascientific_12_reservoir_22ml', '2').wells()[1]

    # Set up tip racks
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')

    # Set up pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Define transfer volumes
    pbs_vol = 300
    dmem_vol = 300

    # Perform exchange
    for well in plate.wells():
        # Aspirate the old media using PBS(-)
        p300.pick_up_tip()
        p300.aspirate(pbs_vol, well.bottom(5))
        p300.dispense(pbs_vol, pbs)
        p300.blow_out()
        p300.drop_tip()

        # Aspirate the PBS(-) using pipette and discard it
        p300.pick_up_tip()
        p300.aspirate(pbs_vol, pbs)
        p300.dispense(pbs_vol, well.bottom(5))
        p300.blow_out()
        p300.drop_tip()

        # Add D-MEM using pipette
        p300.pick_up_tip()
        p300.aspirate(dmem_vol, dmem)
        p300.dispense(dmem_vol, well.bottom(5))
        p300.blow_out()
        p300.drop_tip()
