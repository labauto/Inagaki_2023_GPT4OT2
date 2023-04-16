from opentrons import protocol_api
metadata = {
    'apiLevel': '2.9',
    'protocolName': 'Cell Viability Assay',
    'author': 'Your Name',
    'description': 'A549 cell treatment with Thapsigargin and Cell Viability Assay',
}
def run(protocol: protocol_api.ProtocolContext):

    # Labware
    # Slots
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    Snapcapped_tubes_225 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    heater_shaker = protocol.load_module('heater_shaker_module', 5)
    well_plate = heater_shaker.load_labware('ot2_96_tctrisplate_200ul')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 9)

    # Pipettes
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])


    # Protocol

    # Step 1-3: Preparing cell suspension and transferring it to tube rack
    # Step 4-8: Preparing drug dilutions and transferring them to 96-well plate
    # Steps 9-14: Preparing 2X thapsigargin and transferring to 96-well plate
    # Steps are performed manually since they require cell count and concentration adjustments
    
    # Step 10: Add CellTox Green Reagent
    left_pipette.pick_up_tip(tiprack_20.wells('A1'))
    for well in plate_96.wells():
        left_pipette.transfer(15, tube_rack.wells('B2'), well, new_tip='never')
    left_pipette.drop_tip()

    # Step 11: Orbital shaking
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    heater_shaker.shake(minutes=2)

    # Step 12: Incubate at RT
    protocol.delay(minutes=15)

    # Step 13: Read fluorescence with Biotek microplate reader (Step is performed manually)

    # Step 14: Add Cell Titer Glo 2.0 Reagent
    right_pipette.pick_up_tip(tiprack_200.wells('A1'))
    for well in plate_96.wells():
        right_pipette.transfer(80, tube_rack.wells('B1'), well, new_tip='never')
    right_pipette.drop_tip()

    # Step 15: Orbital shaking again
    heater_shaker.shake(minutes=2)

    # Step 16: Incubate at RT
    protocol.delay(minutes=10)

    # Step 17: Read luminescence with Biotek microplate reader (Step is performed manually)
