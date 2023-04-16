from opentrons import protocol_api

metadata = {
    'protocolName': 'Automating A549 Cells Viability and Cytotoxicity',
    'author': 'Your Name <youremail@example.com>',
    'description': 'Automating A549 Cells Viability and Cytotoxicity with Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '6')
    tube_rack_slot_7 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '7')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    heater_shaker = protocol.load_module('HeaterShakerModule', '9')

    # Pipettes
    pipette_20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    pipette_200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Reagents
    celltox_green = tube_rack.wells_by_name()['B2']
    cell_titer_glo = tube_rack.wells_by_name()['B1']
  
    # Specify the wells for drug treatment
    drug_treatment_rows = ['D', 'E', 'F']

    # Add CellTox Green reagent
    for i in range(1, 6):
        for well in plate_96.rows_by_name()['A']:
            pipette_20.pick_up_tip()
            pipette_20.aspirate(15, celltox_green)
            pipette_20.dispense(15, well)
            pipette_20.drop_tip()

    # Shake and incubate
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    heater_shaker.load_labware('corning_96_wellplate_360ul_flat')  # Load a plate if not already added
    protocol.delay(minutes=2)
    heater_shaker.deactivate()

    # Read fluorescence
    # Ensure the Biotek microplate reader is integrated and configured properly.
    # Read fluorescence at 485 nm excitation and 520 nm emission.

    # Add Cell Titer Glo 2.0 reagent
    for i in range(1, 6):
        for well in plate_96.rows_by_name()['A']:
            pipette_200.pick_up_tip()
            pipette_200.aspirate(80, cell_titer_glo)
            pipette_200.dispense(80, well)
            pipette_200.drop_tip()

    # Shake and incubate
    heater_shaker.set_temperature(25)
    heater_shaker.set_speed(500)
    heater_shaker.load_labware('corning_96_wellplate_360ul_flat')  # Load a plate if not already added
    protocol.delay(minutes=2)
    heater_shaker.deactivate()

    # Read luminescence
    # Ensure the Biotek microplate reader is integrated and configured properly.
    # Read luminescence.
