from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Opentrons',
    'description': 'Automated hMSC spheroid experiment with and without OS'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

    # Reagents
    dmem = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A1']
    dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A2']
    dex = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A3']
    aa = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A4']
    bgp = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A5']
    hmsc_cells = protocol.load_labware('nest_12_reservoir_15ml', '3').wells_by_name()['A6']

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Protocol
    for i, well in enumerate(plate_96_well.columns()[0:6]):  # OS-
        p300.pick_up_tip()
        p300.transfer(100, dmem, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_96_well.columns()[6:]):  # OS+
        p300.pick_up_tip()
        p300.transfer(100, dmem_high_glucose, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_96_well.columns()[6:]):  # OS+ supplements
        p300.pick_up_tip()
        p300.transfer(0.1, dex, well, new_tip='never')
        p300.transfer(1, aa, well, new_tip='never')
        p300.transfer(1, bgp, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_96_well.columns()[0:6]):  # OS- cells
        p300.pick_up_tip()
        p300.transfer(100, hmsc_cells, well, new_tip='never')
        p300.drop_tip()

    for i, well in enumerate(plate_96_well.columns()[6:]):  # OS+ cells
        p300.pick_up_tip()
        p300.transfer(100, hmsc_cells, well, new_tip='never')
        p300.drop_tip()
