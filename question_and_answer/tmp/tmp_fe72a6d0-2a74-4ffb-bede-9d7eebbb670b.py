from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    medium_dmem = protocol.load_labware('nest_1_reservoir_195ml', '2')
    medium_dmem_high_glucose = protocol.load_labware('nest_1_reservoir_195ml', '3')
    dex = protocol.load_labware('nest_1_reservoir_195ml', '4')
    aa = protocol.load_labware('nest_1_reservoir_195ml', '5')
    bgp = protocol.load_labware('nest_1_reservoir_195ml', '6')
    cells = protocol.load_labware('nest_1_reservoir_195ml', '7')
    plate_os_minus = protocol.load_labware('nest_96_wellplate_200ul_flat', '8')
    plate_os_plus = protocol.load_labware('nest_96_wellplate_200ul_flat', '9')

    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for well in plate_os_minus.wells():
        p300.transfer(100, medium_dmem.wells()[0], well)

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(100, medium_dmem_high_glucose.wells()[0], well)

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(0.1, dex.wells()[0], well)
        p300.transfer(1, aa.wells()[0], well)
        p300.transfer(1, bgp.wells()[0], well)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in plate_os_minus.wells():
        p300.transfer(100, cells.wells()[0], well)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in plate_os_plus.wells():
        p300.transfer(100, cells.wells()[0], well)
