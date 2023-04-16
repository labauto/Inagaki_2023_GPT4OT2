from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC spheroids experiment',
    'author': 'Assistant',
    'description': 'Automating hMSC spheroids experiment with Opentrons',
    'apiLevel': '2.9'
}

def transfer_medium(pipette, source, dmem_wells, hg_wells):
    for well in dmem_wells:
        pipette.transfer(100, source, well)

    for well in hg_wells:
        pipette.transfer(100, source, well)

def add_supplements(pipette, source, os_plus_wells):
    for supp in source:  # Assumes sources are in a list (Dex, AA, BGP)
        volume = [0.1, 1, 1]  # Corresponding volumes for Dex, AA, BGP
        for well in os_plus_wells:
            pipette.transfer(volume[i], supp, well)

def transfer_cells(pipette, source, os_minus_wells, os_plus_wells):
    for well in os_minus_wells:
        pipette.transfer(100, source, well)

    for well in os_plus_wells:
        pipette.transfer(100, source, well)

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', location='1')
    hmsc_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location='2')
    medium_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location='3')
    dmem_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_15ml_conical', location='4')
    dmem_tube = dmem_tube_rack['A1']
    hhg_tube = dmem_tube_rack['A2']
    supplements_tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', location='5')
    dexamethasone = supplements_tube_rack['A1']
    ascorbic_acid = supplements_tube_rack['A2']
    beta_glycerophosphate = supplements_tube_rack['A3']
    source_supplements = [dexamethasone, ascorbic_acid, beta_glycerophosphate]
    hmsc_tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_15ml_conical', location='6')
    hmsc_source = hmsc_tube_rack['A1']

    # Load Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips])

    # Distribute medium
    os_minus_wells = hmsc_plate.columns()[0:6]
    os_plus_wells = hmsc_plate.columns()[6:12]

    transfer_medium(p300,dmem_tube, os_minus_wells, os_minus_wells)
    transfer_medium(p300,hhg_tube, os_plus_wells, os_minus_wells)

    # Add supplements
    add_supplements(p300, source_supplements, os_plus_wells)

    # Transfer hMSC cells
    transfer_cells(p300, hmsc_source, os_minus_wells, os_plus_wells)

    protocol.end()

