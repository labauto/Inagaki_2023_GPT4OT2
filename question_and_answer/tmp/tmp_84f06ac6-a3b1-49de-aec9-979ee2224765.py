from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'A549 Cells Experiment with Thapsigargin',
    'author': 'Your Name',
    'description': 'Automated experiment for A549 cells treated with thapsigargin',
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')

    he_sh = protocol.load_module('heater_shaker', '1')

    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '6')
    drug_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '7')
    conical_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '9')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])

    ### Steps 1-8: Preparatory Steps―Performed manually ###

    ### Step 9: Prepare 2X concentrations of thapsigargin
    for idx, source_tube in enumerate(drug_rack.rows()[0][:6]):
        dest_tube = tube_rack.rows()[0][idx]
        p300.pick_up_tip()
        p300.transfer(100, source_tube, dest_tube, mix_before=(3, 100), new_tip='never')
        p300.drop_tip()

    # Additional steps for preparing the 2X concentrations
    for idx, source_tube in enumerate(drug_rack.rows()[1][:1]):
        dest_tube = tube_rack.rows()[0][6]
        p300.pick_up_tip()
        p300.transfer(100, source_tube, dest_tube, mix_before=(3, 100), new_tip='never')
        p300.drop_tip()

    ### Step 10: Add CellTox Green Reagent
    cell_tox_green_reagent = conical_rack['B2']
    for well in he_sh.plate.rows()[0][:7]:
        for row in he_sh.plate.rows():
            p20.pick_up_tip()
            p20.transfer(15, cell_tox_green_reagent, row[well.index], new_tip='always')
            p20.drop_tip()

    # Adding reagent to A5-C5 well group
    for well in he_sh.plate.rows()[3:6][4]:
        p20.pick_up_tip()
        p20.transfer(15, cell_tox_green_reagent, well, new_tip='always')
        p20.drop_tip()

    # Mixing CellTox Green Reagent
    he_sh.set_speed(500)
    protocol.delay(minutes=2)

    ### Step 11-12: Orbital shaking and incubation
    protocol.delay(minutes=15)

    ### Steps 13-14: Read plate & start viability assay―Performed manually using Biotek microplate reader ###

    ### Step 15: Add Cell Titer Glo 2.0 Reagent
    cell_titer_glo_reagent = conical_rack['B1']
    for well in he_sh.plate.rows()[0][:7]:
        for row in he_sh.plate.rows():
            p300.pick_up_tip()
            p300.transfer(80, cell_titer_glo_reagent, row[well.index], new_tip='always')
            p300.drop_tip()

    # Adding reagent to A5-C5 well group
    for well in he_sh.plate.rows()[3:6][4]:
        p300.pick_up_tip()
        p300.transfer(80, cell_titer_glo_reagent, well, new_tip='always')
        p300.drop_tip()

    # Mixing Cell Titer Glo Reagent
    he_sh.set_speed(500)
    protocol.delay(minutes=2)

    ### Step 16-17: Incubate and read plate―Performed manually using Biotek microplate reader ###
