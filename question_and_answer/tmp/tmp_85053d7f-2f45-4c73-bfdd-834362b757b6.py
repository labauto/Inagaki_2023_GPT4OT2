from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroid culture',
    'author': 'Your Name',
    'description': 'Protocol for hMSC spheroid culture',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8_ml_flat', '1')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    pipette = protocol.load_instrument('p10_multi', 'left', tip_racks=[protocol.load_labware("opentrons_96_tiprack_10ul", 8)])
    
    # Add DMEM to 96 well plates
    pipette.pick_up_tip()
    for well in plate_96_well.columns_by_name()["1"]:
        pipette.transfer(100, protocol.load_labware("nest_12_reservoir_15ml", 3)['A1'], well.bottom(), new_tip='never')
    pipette.drop_tip()

    # Add OS+ supplement to 96 well plates
    pipette.pick_up_tip()
    for well in plate_96_well.columns_by_name()["2"]:
        pipette.transfer(100, protocol.load_labware("nest_12_reservoir_15ml", 3)['A2'], well.bottom(), new_tip='never')
    pipette.drop_tip()
    
    # Add hMSC cells to 96 well plates
    pipette.pick_up_tip()
    for well in plate_96_well.columns_by_name()["1"]:
        pipette.transfer(100, protocol.load_labware("nest_12_reservoir_15ml", 3)['A3'], well.bottom(), new_tip='never')
    pipette.drop_tip()

    pipette.pick_up_tip()
    for well in plate_96_well.columns_by_name()["2"]:
        pipette.transfer(100, protocol.load_labware("nest_12_reservoir_15ml", 3)['A3'], well.bottom(), new_tip='never')
    pipette.drop_tip()
