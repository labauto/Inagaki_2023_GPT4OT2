from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids',
    'author': 'Assistant',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    medium_dmem = protocol.load_labware('usascientific_12_reservoir_22ml', 1).wells_by_name()['A1']
    medium_dmem_high = protocol.load_labware('usascientific_12_reservoir_22ml', 1).wells_by_name()['A2']
    reagents = protocol.load_labware('usascientific_12_reservoir_22ml', 1)
    dex = reagents.wells_by_name()['A3']  # Dexamethasone
    aa = reagents.wells_by_name()['A4']  # Ascorbic Acid
    bgp = reagents.wells_by_name()['A5']  # Beta-glycerophosphate
    cells = reagents.wells_by_name()['A6']  # hMSC cells
    plate_os_minus = protocol.load_labware('costar_96_wellplate_360ul_flat', 2)
    plate_os_plus = protocol.load_labware('costar_96_wellplate_360ul_flat', 3)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    # Pipette
    p50 = protocol.load_instrument('p50_single', mount='right', tip_racks=[tiprack])

    # Steps
    # Transfer medium (100 µl) to plate OS-
    for well in plate_os_minus.wells():
        p50.pick_up_tip()
        p50.transfer(100, medium_dmem, well)
        p50.drop_tip()

    # Transfer medium (100 µl) to plate OS+
    for well in plate_os_plus.wells():
        p50.pick_up_tip()
        p50.transfer(100, medium_dmem_high, well)
        p50.drop_tip()

    # Add supplements to plate OS+
    for well in plate_os_plus.wells():
        p50.pick_up_tip()
        p50.transfer(0.1, dex, well)
        p50.transfer(1, aa, well)
        p50.transfer(1, bgp, well)
        p50.drop_tip()

    # Transfer hMSC cells (100 µl) to plate OS-
    for well in plate_os_minus.wells():
        p50.pick_up_tip()
        p50.transfer(100, cells, well)
        p50.drop_tip()

    # Transfer hMSC cells (100 µl) to plate OS+
    for well in plate_os_plus.wells():
        p50.pick_up_tip()
        p50.transfer(100, cells, well)
        p50.drop_tip()
