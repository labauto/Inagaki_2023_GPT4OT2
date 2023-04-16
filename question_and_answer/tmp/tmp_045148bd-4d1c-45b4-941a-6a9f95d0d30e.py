from opentrons import simulate, execute

metadata = {
    'protocolName': 'hMSC Spheroids Culture',
    'author': 'Your Name Here',
    'description': 'Culture hMSC spheroids with and without osteoinduction supplements',
    'apiLevel': '2.0'
}

def transfer_medium(volume, source, destination):
    pipette.transfer(volume, source, destination)

def add_supplements(dex, aa, bgp, wells):
    for well in wells:
        pipette.aspirate(dex, dex_well)
        pipette.dispense(dex, well)
        pipette.aspirate(aa, aa_well)
        pipette.dispense(aa, well)
        pipette.aspirate(bgp, bgp_well)
        pipette.dispense(bgp, well)

def transfer_cells(volume, source, destination):
    pipette.transfer(volume, source, destination)

def run(protocol):
    # Define Labware
    plate_96well = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_6well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    tip_rack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '3')
    p1000_tip_rack = protocol.load_labware('opentrons_96_tiprack_1000ul', '4')
    
    # Define Pipettes
    p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[p1000_tip_rack])
    pipette = protocol.load_instrument('p300_multi', 'left', tip_racks=[tip_rack])
    
    # Define Wells and Volumes
    os_plus_wells = plate_96well.rows()[0][:3]
    medium_wells = plate_96well.rows()[1][:3]
    
    dex_well = plate_6well.wells()[0]
    aa_well = plate_6well.wells()[1]
    bgp_well = plate_6well.wells()[2]
    
    medium_vol = 100
    cells_vol = 100
    cells_concentration = 2500
    
    # Transfer Medium for both conditions
    transfer_medium(medium_vol, plate_96well.rows()[0][:3], plate_96well.rows()[1][:3])
    transfer_medium(medium_vol, plate_96well.rows()[0][3:6], plate_96well.rows()[1][3:6],)
    
    # Add Supplements for os_plus_wells
    add_supplements(0.1, 1, 1, os_plus_wells)

    # Transfer Cells for both conditions
    for col in range(6):
        transfer_cells(cells_vol, plate_6well.wells()[col], plate_96well.columns()[col])
    
# simulate the run
simulate.run(run, "protocol.py", api_level="2.0")
# execute the run
# execute.run(run, metadata={'apiLevel': '2.0'})
