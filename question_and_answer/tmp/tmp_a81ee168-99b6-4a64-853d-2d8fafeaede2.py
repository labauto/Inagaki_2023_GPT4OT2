from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids with OS+ and OS-',
    'author': 'Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    reagents = protocol.load_labware('usascientific_12_reservoir_22ml', 1)
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)

    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300])

    # Reagents
    medium_dmem = reagents.wells_by_name()['A1']
    medium_dmem_high = reagents.wells_by_name()['A2']
    dexamethasone = reagents.wells_by_name()['A3']
    ascorbic_acid = reagents.wells_by_name()['A4']
    beta_glycerophosphate = reagents.wells_by_name()['A5']
    hmsc_cells = reagents.wells_by_name()['A6']

    # Transfer medium (DMEM) to OS-
    for well in plate_96.wells()[:48]:
        p300.pick_up_tip()
        p300.transfer(100, medium_dmem, well, new_tip='never')
        p300.drop_tip()

    # Transfer medium (DMEM high glucose) to OS+
    for well in plate_96.wells()[48:]:
        p300.pick_up_tip()
        p300.transfer(100, medium_dmem_high, well, new_tip='never')
        p300.drop_tip()

    # Add osteoinduction supplements to OS+
    for well in plate_96.wells()[48:]:
        p300.pick_up_tip()
        p300.transfer(0.1, dexamethasone, well, new_tip='never')
        p300.transfer(1, ascorbic_acid, well, new_tip='never')
        p300.transfer(1, beta_glycerophosphate, well, new_tip='never')
        p300.drop_tip()

    # Transfer hMSC cells (2,500 cells/100 µl) to OS- and OS+
    for well in plate_96.wells():
        p300.pick_up_tip()
        p300.transfer(100, hmsc_cells, well, new_tip='never')
        p300.drop_tip()
