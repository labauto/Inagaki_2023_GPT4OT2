from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def load_labware():
    # Load labware
    mode_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    mode_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    dex_source = protocol.load_labware('opentrons_6_tuberack_nest_1.5ml_snapcap', '5')['A1']
    aa_source = protocol.load_labware('opentrons_6_tuberack_nest_1.5ml_snapcap', '5')['B1']
    bgp_source = protocol.load_labware('opentrons_6_tuberack_nest_1.5ml_snapcap', '5')['C1']
    
    return mode_os_minus, mode_os_plus, dex_source, aa_source, bgp_source

def transfer_cells(well_os_minus, well_os_plus, hmsc_cells):
    p300.transfer(100, hmsc_cells, well_os_minus, new_tip='always')
    p300.transfer(100, hmsc_cells, well_os_plus, new_tip='always')

def transfer_supplements(well_os_plus):
    p300.pick_up_tip()

    p300.transfer(0.1, dex_source, well_os_plus, mix_after=(3, 10), new_tip='never')
    p300.transfer(1, aa_source, well_os_plus, mix_after=(3, 10), new_tip='never')
    p300.transfer(1, bgp_source, well_os_plus, mix_after=(3, 10), new_tip='never')

    p300.drop_tip()

def transfer_medium(well_os_minus, well_os_plus, medium_os_minus, medium_os_plus):
    p300.transfer(100, medium_os_minus, well_os_minus, new_tip='always')
    p300.transfer(100, medium_os_plus, well_os_plus, new_tip='always')

def run(protocol: protocol_api.ProtocolContext):
    # Load labware and pipettes
    protocol = protocol_api.get_protocol_api('2.11')

    plate_os_minus, plate_os_plus, dex, aa, bgp = load_labware()
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '11')])
    
    # Source labware (Change these variables to match your source labware)
    medium_os_minus = protocol.load_labware('nest_12_reservoir_15ml', '4')['A1']
    medium_os_plus = protocol.load_labware('nest_12_reservoir_15ml', '4')['A2']
    hmsc_cells = protocol.load_labware('nest_12_reservoir_15ml', '4')['A3']

    for well_os_minus, well_os_plus in zip(plate_os_minus.wells(), plate_os_plus.wells()):
        transfer_medium(well_os_minus, well_os_plus, medium_os_minus, medium_os_plus)
        transfer_supplements(well_os_plus)
        transfer_cells(well_os_minus, well_os_plus, hmsc_cells)
