from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',     # You can adjust the apiLevel according to the version you have installed
    'protocolName': 'automate_hMSC_experiment'
}

def transfer_medium(pipette, source, destination_plate, volume):
    for well in destination_plate.wells():
        pipette.transfer(volume, source, well)

def transfer_cells(pipette, source, destination_plate, volume):
    for well in destination_plate.wells():
        pipette.transfer(volume, source, well)

def add_supplements(pipette, supplements, destination_plate, volumes):
    for i, supplement in enumerate(supplements):
        for well in destination_plate.wells():
            pipette.transfer(volumes[i], supplement, well)

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    temp_deck = protocol.load_module('Temperature Module', 10)
    cell_plate = temp_deck.load_labware('nest_96_wellplate_2ml_deep')
    medium_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 1)
    supplement_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 2)
    hMSC_dmem = protocol.load_labware('usascientific_12_reservoir_22ml', 3)
    hMSC_dmem_high_glucose = protocol.load_labware('usascientific_12_reservoir_22ml', 4)

    # Pipettes
    p_20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_20ul', 5)])
    p_1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', 6)])

    # Experiment
    transfer_medium(p_1000, hMSC_dmem['A1'], medium_plate.columns()[0:6], 100)
    transfer_medium(p_1000, hMSC_dmem_high_glucose['A1'], medium_plate.columns()[6:], 100)

    dex = supplement_plate['A1']
    ascorbic_acid = supplement_plate['A2']
    beta_glycerophosphate = supplement_plate['A3']
    supplements = [dex, ascorbic_acid, beta_glycerophosphate]
    volumes = [0.1, 1, 1]
    add_supplements(p_20, supplements, medium_plate.columns()[6:], volumes)

    hMSC_cells = cell_plate.wells_by_name()['A1']
    transfer_cells(p_1000, hMSC_cells, medium_plate.columns()[0:6], 100)
    transfer_cells(p_1000, hMSC_cells, medium_plate.columns()[6:], 100)
