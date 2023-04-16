from opentrons import protocol_api

metadata = {'apiLevel': '2.9'}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tuberack_snap = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", 6)
    tuberack_dilutions = protocol.load_labware("opentrons_24_tuberack_generic_2ml_screwcap", 7)
    plate_96 = protocol.load_labware("corning_96_wellplate_360ul_flat", 5)

    # Pipettes
    p20 = protocol.load_instrument("p20_single_gen2", "right", tip_racks=[tiprack_20])
    p200 = protocol.load_instrument("p300_single_gen2", "left", tip_racks=[tiprack_200])

    # Constants
    tube_positions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    drug_concentration_wells = ["D1", "D2", "D3", "D4", "D5", "D6"]
    two_times_drug_wells = ["C1", "C3", "C5", "D1", "D2", "D3", "D4", "D5", "D6"]
    control_wells = ["A1", "B1", "C1"]
    thapsigargin_wells = [[f"D{i}", f"E{i}", f"F{i}"] for i in range(1, 5)]

    # Step 6 and 7
    p200.transfer(35, tuberack_snap["B2"], tuberack_dilutions["A1"])  # Addition of initial 35µl

    for source, dest in zip(tube_positions[:-1], tube_positions[1:]):
        p20.pick_up_tip()
        p20.mix(3, 25, tuberack_dilutions[source])
        p20.aspirate(25, tuberack_dilutions[source])
        p20.dispense(25, tuberack_dilutions[dest])
        p20.drop_tip()

    # Step 8
    for source, dest in zip(["A1"] * 6 + ["B1"] * 6, drug_concentration_wells):
        p200.pick_up_tip()
        p200.mix(3, 100, tuberack_dilutions[source])
        p200.aspirate(100, tuberack_dilutions[source])
        p200.dispense(50, tuberack_dilutions[dest])
        p200.drop_tip()

    # Step 9
    p200.pick_up_tip()
    p200.aspirate(100, tuberack_snap['C1'], tuberack_snap['D1'])
    p200.drop_tip()
    for source, dest in zip(two_times_drug_wells[:-1], two_times_drug_wells[1:]):
        p200.pick_up_tip()
        p200.mix(3, 100, tuberack_snap[source])
        p200.aspirate(100, tuberack_snap[source])
        p200.dispense(100, tuberack_snap[dest])
        p200.drop_tip()

    # Step 10 and 11
    for well in plate_96.wells()[:96]:
        p20.transfer(15, tuberack_snap["B2"], well)

    # Step 15 and 16
    for well in plate_96.wells()[:96]:
        p200.transfer(80, tuberack_snap["B1"], well)

    # The actual shaking and incubation should be manually done according to Step 11 to 17
