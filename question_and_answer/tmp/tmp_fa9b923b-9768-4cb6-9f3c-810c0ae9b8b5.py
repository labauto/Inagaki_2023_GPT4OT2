from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Experiment',
    'author': 'Your Name <your_email@example.com>',
    'description': 'Transfer hMSC cells and osteoinduction supplements into 96-well plates',
    'apiLevel': '2.0'
}

def transfer_medium(pipette, source, plate, volume):
    for well in plate.wells():
        pipette.transfer(volume, source, well)

def transfer_supplements(pipette, sources, plate, volumes):
    for supplement, volume in zip(sources, volumes):
        pipette.transfer(volume, supplement, plate.wells(), new_tip='always')

def transfer_cells(pipette, source, plate, volume):
    for well in plate.wells():
        pipette.transfer(volume, source, well, mix_after=(3, volume / 2))

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    medium1 = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 1)
    medium2 = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 2)
    supplements_tuberack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3)
    cell_src = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 4)
    dest_plate1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    dest_plate2 = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=protocol.load_labware('opentrons_96_tiprack_20ul', 7))
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=protocol.load_labware('opentrons_96_tiprack_300ul', 8))

    # Reagents
    dm_lg = medium1.wells()[0]
    dm = medium2.wells()[0]
    dex = supplements_tuberack.wells_by_name()['A1']
    aa = supplements_tuberack.wells_by_name()['A2']
    bgp = supplements_tuberack.wells_by_name()['A3']
    hmsc_cells = cell_src.wells()[0]

    # Experiment
    transfer_medium(p300, dm, dest_plate1, 100)
    transfer_medium(p300, dm_lg, dest_plate2, 100)
    transfer_supplements(p20, [dex, aa, bgp], dest_plate2, [0.1, 1, 1])
    transfer_cells(p300, hmsc_cells, dest_plate1, 100)
    transfer_cells(p300, hmsc_cells, dest_plate2, 100)

