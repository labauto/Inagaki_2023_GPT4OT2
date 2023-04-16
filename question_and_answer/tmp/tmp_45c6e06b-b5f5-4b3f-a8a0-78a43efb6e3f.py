from opentrons import protocol_api

metadata = {
    'protocolName': 'Viability and Cytotoxicity Assay',
    'author': 'Your Name',
    'description': 'Automation of A549 cell viability and cytotoxicity measurements',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    slot_6_tubes = protocol.load_labware('opentrons_15_tuberack_falcon_14ml', 6)
    slot_7_tubes = protocol.load_labware('opentrons_15_tuberack_falcon_14ml', 7)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    
    # Define pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])

    heater_shaker = protocol.load_module('thermo_shaker', 8)
    hs_plate = heater_shaker.load_labware('corning_96_wellplate_360ul_flat')

    # Define initial stocks, 4X and 2X concentrations
    stocks = slot_7_tubes.wells()[:7]
    four_x_concentrations = slot_7_tubes.wells()[16:28]
    two_x_concentrations = slot_6_tubes.wells()[:12]
    
    # Prepare dilutions
    prepare_dilutions(p300, stocks, four_x_concentrations, two_x_concentrations)

    # Add negative controls and thapsigargin treatments
    add_negative_controls(p300, plate_96)
    add_thapsigargin_treatment(p300, two_x_concentrations, plate_96)

    # Measure cytotoxicity
    measure_cytotoxicity(p20, slot_6_tubes, hs_plate, plate_96)

    # Measure viability
    measure_viability(p300, slot_6_tubes, hs_plate, plate_96)


def prepare_dilutions(p300, stocks, four_x_concentrations, two_x_concentrations):
    # Prepare 4X dilutions
    for i in range(12):
        p300.pick_up_tip()
        p300.transfer(100, stocks[i % 7], four_x_concentrations[i], mix_after=(3, 100), new_tip='never')
        p300.drop_tip()

    # Prepare 2X dilutions
    p300.transfer(100, slot_6_tubes.wells()[8:20], two_x_concentrations)
    for i in range(12):
        p300.pick_up_tip()
        p300.transfer(100, four_x_concentrations[i], two_x_concentrations[i], mix_after=(5, 100), new_tip='never')
        p300.drop_tip()


def add_negative_controls(p300, plate_96):
    p300.transfer(50, slot_6_tubes['A1'], plate_96.columns()[0], mix_after=(3, 50))
    p300.transfer(50, slot_6_tubes['A1'], plate_96.columns()[6], mix_after=(3, 50))


def add_thapsigargin_treatment(p300, two_x_concentrations, plate_96):
    for i in range(12):
        p300.pick_up_tip()
        if i < 6:
            wells = plate_96.wells()[i*8+1:i*8+4]
            p300.distribute(50, two_x_concentrations[i], wells, mix_after=(3, 50), new_tip='never')
        else:
            wells = plate_96.wells()[i*8+5:i*8+8]
            p300.distribute(50, two_x_concentrations[i], wells, mix_after=(3, 50), new_tip='never')
        p300.drop_tip()


def measure_cytotoxicity(p20, slot_6_tubes, hs_plate, plate_96):
    for col in hs_plate.columns():
        p20.pick_up_tip()
        p20.transfer(15, slot_6_tubes['B2'], col[0], mix_after=(1, 15), new_tip='never')
        p20.drop_tip()

    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.stop()
    heater_shaker.set_temperature(None)

    protocol.comment("Incubate at room temperature for 15 minutes.")


def measure_viability(p300, slot_6_tubes, hs_plate, plate_96):
    for col in hs_plate.columns():
        p300.pick_up_tip()
        p300.transfer(80, slot_6_tubes['B1'], col[0], mix_after=(1, 80), new_tip='never')
        p300.drop_tip()

    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    protocol.delay(minutes=2)
    heater_shaker.stop()
    heater_shaker.set_temperature(None)

    protocol.comment("Incubate at room temperature for 10 minutes.")

