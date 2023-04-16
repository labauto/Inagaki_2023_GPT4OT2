from opentrons import protocol_api

metadata = {
    "protocolName": "Exchange hMSC Cell Culture Medium",
    "author": "Opentrons",
    "apiLevel": "2.9",
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips = protocol.load_labware("opentrons_96_tiprack_300ul", 1)
    well_plate = protocol.load_labware("corning_6_wellplate_16.8ml_flat", 2)
    pbs = protocol.load_labware("nest_12_reservoir_15ml", 3)["A1"]
    dmem = protocol.load_labware("nest_12_reservoir_15ml", 4)["A1"]
    trash = protocol.fixed_trash

    # Pipettes
    p300_multi = protocol.load_instrument("p300_multi_gen2", "left", tip_racks=[tips])

    # Step 1: Remove existing medium
    p300_multi.pick_up_tip()
    for well_index in range(0, 6):
        p300_multi.transfer(200, well_plate.rows()[0][well_index * 2], trash['A1'].top(), new_tip='never')

    p300_multi.drop_tip()

    # Step 2: Add PBS
    p300_multi.pick_up_tip()
    for well_index in range(0, 6):
        p300_multi.transfer(200, pbs, well_plate.rows()[0][well_index * 2], new_tip='never')

    p300_multi.mix(3, 200, well_plate['A1']) 
    p300_multi.drop_tip()

    # Step 3: Remove PBS
    p300_multi.pick_up_tip()
    for well_index in range(0, 6):
        p300_multi.transfer(200, well_plate.rows()[0][well_index * 2], trash['A1'].top(), new_tip='never')
        
    p300_multi.drop_tip()

    # Step 4: Add fresh D-MEM
    for well_index in range(0, 6):
        p300_multi.transfer(200, dmem, well_plate.rows()[0][well_index * 2])
