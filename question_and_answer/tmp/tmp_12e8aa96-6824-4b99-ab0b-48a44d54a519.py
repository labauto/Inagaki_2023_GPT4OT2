from opentrons import protocol_api

metadata = {
    'protocolName': 'Medium Exchange',
    'author': 'Assistant',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and DMEM',
    'apiLevel': '2.10'
}

# Protocol

def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_well = protocol.load_labware('nest_1_reservoir_195ml', '2').wells()[0]
    dmem_well = protocol.load_labware('nest_1_reservoir_195ml', '3').wells()[0]
    plate_6 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Load the pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300])

    # Exchange medium for each well
    for well in plate_6.wells():

        # Remove medium with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(150, pbs_well, rate=0.5)  # Adjust the volume to stay within pipette capacity
        p300.dispense(150, well, rate=0.5)
        p300.mix(3, 150, well)  # Mix the well
        p300.blow_out(well.top())
        p300.return_tip()

        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(150, dmem_well, rate=0.5)  # Adjust the volume to stay within pipette capacity
        p300.dispense(150, well, rate=0.5)
        p300.mix(3, 150, well)  # Mix the well
        p300.blow_out(well.top())
        p300.return_tip()

