from opentrons import protocol_api

metadata = {
    'author': 'Your Name',
    'description': 'Exchanging hMSC cell culture medium using PBS(-) and D-MEM.',
    'protocolName': 'hMSC Culture Medium Exchange'
}

def run(protocol: protocol_api.ProtocolContext):
    # Configure labware and pipettes
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2)
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left')
    
    # Parameters
    pbs_well_id = 0  # well A1 in the reservoir
    d_mem_well_id = 1  # well A2 in the reservoir
    culture_volume_to_exchange = 500

    # Distribute PBS(-)
    pbs_well = reagent_reservoir.wells()[pbs_well_id]
    for well in plate.wells():
        p1000.transfer(culture_volume_to_exchange, pbs_well, well.top(), new_tip='always')
    
    # Incubate with PBS(-) - this only simulates the incubation time on the Opentrons robot
    protocol.delay(minutes=5)  # customize the incubation time as needed
    
    # Aspirate PBS(-) and discard
    waste_well = reagent_reservoir.wells()[11] # well A12 in the reservoir
    for well in plate.wells():
        p1000.transfer(culture_volume_to_exchange, well, waste_well.top(), new_tip='always')

    # Distribute D-MEM
    d_mem_well = reagent_reservoir.wells()[d_mem_well_id]
    for well in plate.wells():
        p1000.transfer(culture_volume_to_exchange, d_mem_well, well.top(), new_tip='always')
