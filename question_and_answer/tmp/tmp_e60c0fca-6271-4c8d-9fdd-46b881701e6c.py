from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    
    slot_3_tube_rack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3')
    
    heater_shaker = protocol.load_module('temperature', 11)
    plate = heater_shaker.load_labware("corning_96_wellplate_360ul_flat", label="96well_plate")
    
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200ul])
    
    # Your custom Python script for the experiment would be here
    # ...

if __name__ == '__main__':
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.10')
    run(protocol)
