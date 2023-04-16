from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware and modules
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', '1')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '2')
    falcon_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')
    tube_rack_15ml = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '4')
    tube_rack_eppendorf = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '5')
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    heater_shaker_module = protocol.load_module('heaterShakerModuleV1', '9')

    # Load pipettes
    p20 = protocol.load_instrument('p20_gen2', 'left', tip_racks=[tiprack_20])
    p200 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_200])

    # Experiment steps
    # Add your protocol steps here

    # Example: aspirate and dispense Cell Titer Glo 2.0 reagent
    p200.pick_up_tip()
    p200.aspirate(80, falcon_tube_rack.wells_by_name()['A1'])
    p200.dispense(80, plate_96_well.wells()[0])
    p200.drop_tip()

