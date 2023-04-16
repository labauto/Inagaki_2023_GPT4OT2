from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Your Name',
    'description': 'Experiment with OS+ and OS- conditions',
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    dmem = protocol.load_labware('usascientific_12_reservoir_22ml', '2')['A1']
    dmem_high_glucose = protocol.load_labware('usascientific_12_reservoir_22ml', '2')['A2']
    dex = protocol.load_labware('usascientific_12_reservoir_22ml', '3')['A1']
    aa = protocol.load_labware('usascientific_12_reservoir_22ml', '3')['A2']
    bgp = protocol.load_labware('usascientific_12_reservoir_22ml', '3')['A3']
    hmsc_cells = protocol.load_labware('usascientific_12_reservoir_22ml', '4')['A1']
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')

    # Pipettes
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])

    # Step 1: Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for well in plate_os_minus.wells():
        p300.transfer(100, dmem, well)

    # Step 2: Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(100, dmem_high_glucose, well)

    # Step 3: Add osteoinduction supplements to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(0.1, dex, well, mix_after=(3, 50))
        p300.transfer(1, aa, well, mix_after=(3, 50))
        p300.transfer(1, bgp, well, mix_after=(3, 50))

    # Step 4: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in plate_os_minus.wells():
        p300.transfer(100, hmsc_cells, well)

    # Step 5: Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(100, hmsc_cells, well)
