from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Medium Exchange',
    'author': 'Assistant',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM in 6 well plates',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs = protocol.load_labware('nest_1_reservoir_195ml', '2', 'PBS(-) reservoir').wells()[0]
    dmem = protocol.load_labware('nest_1_reservoir_195ml', '3', 'D-MEM reservoir').wells()[0]
    plate = protocol.load_labware('nest_6_wellplate_9ml_flat', '4')
    
    # Instruments
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    # Constants
    old_medium_vol = 200  # Adjust the volume of the old medium to be removed
    pbs_vol = 200 # Adjust the volume of PBS(-) to be added
    dmem_vol = 180 # Adjust the volume of D-MEM to be added

    # Function to exchange medium in a single well
    def medium_exchange(well, old_medium_vol, pbs_vol, dmem_vol):
        max_vol = p300.hw_pipette['working_volume']
        if old_medium_vol > max_vol:
            old_medium_vol = max_vol
        
        # Remove old medium
        p300.pick_up_tip()
        p300.aspirate(old_medium_vol, well)
        p300.dispense(old_medium_vol, pbs.top()) # Dispense old medium in PBS(-) reservoir
        p300.drop_tip()

        # Wash cells with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(pbs_vol, pbs)
        p300.dispense(pbs_vol, well)
        p300.mix(3, pbs_vol/2, well)  # Mix the PBS(-) in the well
        p300.aspirate(pbs_vol, well)
        p300.dispense(pbs_vol, pbs.top()) # Dispense PBS(-) back into the reservoir
        p300.drop_tip()

        # Add D-MEM
        p300.pick_up_tip()
        p300.aspirate(dmem_vol, dmem)
        p300.dispense(dmem_vol, well)
        p300.drop_tip()

    # Perform medium exchange in each well
    for well in plate.wells():
        medium_exchange(well, old_medium_vol, pbs_vol, dmem_vol)
