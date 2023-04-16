from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Experiment',
    'author': 'Opentrons',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    p300_multi = protocol.load_instrument('p300_multi', 'left')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', location='1')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location='2')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location='3')
    dmem_tube_rack = protocol.load_labware('<your_correct_labware>', location='4')
    dmem_high_glucose_tube_rack = protocol.load_labware('<your_correct_labware>', location='5')
    supplements_tube_rack = protocol.load_labware('<your_correct_labware>', location='6')
    hmsc_tube = protocol.load_labware('<your_correct_labware>', location='7')

    # Locations
    dmem_tube = dmem_tube_rack['A1']
    dmem_high_glucose_tube = dmem_high_glucose_tube_rack['A1']
    dex_tube = supplements_tube_rack['A1']
    aa_tube = supplements_tube_rack['B1']
    bgp_tube = supplements_tube_rack['C1']
    hmsc_cell_tube = hmsc_tube['A1']

    # Transfer Medium (DMEM) to 96 well plate OS(-)
    p300_multi.pick_up_tip(tiprack['A1'])
    for well in os_minus_plate.wells():
        p300_multi.transfer(100, dmem_tube, well, new_tip='never')
    p300_multi.drop_tip()

    # Transfer Medium (DMEM high glucose) to 96 well plate OS(+)
    p300_multi.pick_up_tip(tiprack['A2'])
    for well in os_plus_plate.wells():
        p300_multi.transfer(100, dmem_high_glucose_tube, well, new_tip='never')
    p300_multi.drop_tip()

    # Add Supplements to each Well of 96 well plate for OS(+)
    for well in os_plus_plate.wells():
        p300_multi.pick_up_tip(tiprack['A3'])
        p300_multi.transfer(0.1, dex_tube, well, new_tip='never', mix_before=(3, 50))
        p300_multi.transfer(1, aa_tube, well, new_tip='never', mix_before=(3, 50))
        p300_multi.transfer(1, bgp_tube, well, new_tip='never', mix_before=(3, 50))
        p300_multi.drop_tip()

    # Transfer hMSC cells (2,500 cells / 100 µl) to each well of 96 well plate OS(-)
    for well in os_minus_plate.wells():
        p300_multi.pick_up_tip()
        p300_multi.transfer(100, hmsc_cell_tube, well, new_tip='never', mix_after=(3, 100))
        p300_multi.drop_tip()

    # Transfer hMSC cells (2,500 cells / 100 µl) to each well of 96 well plate OS(+)
    for well in os_plus_plate.wells():
        p300_multi.pick_up_tip()
        p300_multi.transfer(100, hmsc_cell_tube, well, new_tip='never', mix_after=(3, 100))
        p300_multi.drop_tip()

if __name__ == "__main__":
    from opentrons import simulate
    protocol = simulate.get_protocol_api('2.11')
    run(protocol)
