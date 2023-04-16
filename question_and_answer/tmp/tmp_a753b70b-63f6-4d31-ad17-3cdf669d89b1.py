from opentrons import protocol_api

metadata = {
    'protocolName': 'Exchange Cell Culture Medium',
    'author': 'Your Name',
    'description': 'Exchange hMSC cell culture medium using PBS(-) and D-MEM in a 6 well plate',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_labware = protocol.load_labware('nest_1_reservoir_195ml', '2') # Please replace 'nest_1_reservoir_195ml' with the correct reservoir
    dmem_labware = protocol.load_labware('nest_1_reservoir_195ml', '3') # Please replace 'nest_1_reservoir_195ml' with the correct reservoir
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300_multi = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack])

    # Variables
    pbs_volume = 100 # Volume of PBS(-) to add, in uL
    dmem_volume = 100 # Volume of D-MEM to add, in uL

    # Replace well_index with the well number you want to perform medium exchange
    # (e.g., A1, B1, C1, etc.)
    well_index = 'A1'

    # Protocol
    # Remove existing medium
    p300_multi.pick_up_tip()
    p300_multi.transfer(200, well_plate[well_index], p300_multi.waste_container.top(), mix_after=(1, 200))
    p300_multi.drop_tip()

    # Wash with PBS
    p300_multi.pick_up_tip()
    p300_multi.transfer(pbs_volume, pbs_labware.wells()[0], well_plate[well_index], mix_after=(1, 100), new_tip='never')
    p300_multi.transfer(200, well_plate[well_index], p300_multi.waste_container.top(), mix_after=(1, 200))
    p300_multi.drop_tip()

    # Add D-MEM
    p300_multi.pick_up_tip()
    p300_multi.transfer(dmem_volume, dmem_labware.wells()[0], well_plate[well_index], mix_after=(1, 100), new_tip='never')
    p300_multi.drop_tip()
