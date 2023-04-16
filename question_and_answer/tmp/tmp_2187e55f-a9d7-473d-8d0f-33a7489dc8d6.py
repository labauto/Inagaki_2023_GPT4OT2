from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '2')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '3')
    supplements = protocol.load_labware('nest_12_reservoir_15ml', '4')
    cells = protocol.load_labware('nest_12_reservoir_15ml', '5')
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '7')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips])

    # Transfer Medium (DMEM) to OS(-) wells
    for well in plate_os_minus.wells():
        p300.transfer(100, medium_dmem.wells()[0], well)

    # Transfer Medium (DMEM high glucose) to OS(+) wells
    for well in plate_os_plus.wells():
        p300.transfer(100, medium_dmem_high_glucose.wells()[0], well)

    # Add osteoinduction supplements to OS(+) wells
    for well in plate_os_plus.wells():
        p300.transfer(0.1, supplements.wells_by_name()['A1'], well)  # Dexamethasone
        p300.transfer(1, supplements.wells_by_name()['A2'], well)    # Ascorbic Acid
        p300.transfer(1, supplements.wells_by_name()['A3'], well)    # beta-glycerophosphate

    # Transfer hMSC cells to OS(-) wells
    for well in plate_os_minus.wells():
        p300.transfer(100, cells.wells()[0], well)

    # Transfer hMSC cells to OS(+) wells
    for well in plate_os_plus.wells():
        p300.transfer(100, cells.wells()[0], well)
