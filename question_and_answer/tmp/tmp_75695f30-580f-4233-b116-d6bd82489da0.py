# Import necessary modules
from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
}

def transfer_medium(ctx, source, dest, volume):
    pipette.pick_up_tip()
    pipette.transfer(volume, source, dest, new_tip='never')
    pipette.drop_tip()

def transfer_cells(ctx, source, dest, volume):
    pipette.pick_up_tip()
    pipette.transfer(volume, source, dest, new_tip='never', mix_before=(3, 100))
    pipette.drop_tip()

def add_supplements(ctx, sources, dest, volumes):
    for i, source in enumerate(sources):
        pipette.pick_up_tip()
        pipette.transfer(volumes[i], source, dest, new_tip='never')
        pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('tiprack', '1')
    well_plate_96_OS_minus = protocol.load_labware("well_plate_96_osminus", "2")
    well_plate_96_OS_plus = protocol.load_labware("well_plate_96_osplus", "3")
    tuberack = protocol.load_labware("tube_rack", "4")

    # Pipettes
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Reagents
    DMEM = tuberack.wells_by_name()["A1"]
    DMEM_high_glucose = tuberack.wells_by_name()["A2"]
    Dex = tuberack.wells_by_name()["B1"]
    AA = tuberack.wells_by_name()["B2"]
    BGP = tuberack.wells_by_name()["B3"]
    hMSC_cells = tuberack.wells_by_name()["C1"]

    # Protocol steps
    for well in well_plate_96_OS_minus.wells():
        transfer_medium(ctx, DMEM, well, 100)
        transfer_cells(ctx, hMSC_cells, well, 100)
    
    for well in well_plate_96_OS_plus.wells():
        transfer_medium(ctx, DMEM_high_glucose, well, 100)
        add_supplements(ctx, [Dex, AA, BGP], well, [0.1, 1, 1])
        transfer_cells(ctx, hMSC_cells, well, 100)

