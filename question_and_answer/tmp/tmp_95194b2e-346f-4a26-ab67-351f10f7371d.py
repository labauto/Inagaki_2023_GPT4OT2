from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tip300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    dmem = protocol.load_labware('usascientific_12_reservoir_22ml', '2')['A1']
    dmem_high_glucose = protocol.load_labware('usascientific_12_reservoir_22ml', '3')['A1']
    osteo_supplements = {'Dex': 'A2', 'AA': 'A3', 'BGP': 'A4'}
    supplements = protocol.load_labware('usascientific_12_reservoir_22ml', '4', 'Osteo Supplements')

    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip300])

    # Adding DMEM to OS- 96 well plate
    for well in os_minus_plate.wells():
        p300.transfer(100, dmem, well)

    # Adding high glucose DMEM to OS+ 96 well plate
    for well in os_plus_plate.wells():
        p300.transfer(100, dmem_high_glucose, well)

    # Adding osteoinduction supplements to OS+ 96 well plate
    for well in os_plus_plate.wells():
        p300.transfer(0.1, supplements[osteo_supplements['Dex']], well)
        p300.transfer(1, supplements[osteo_supplements['AA']], well)
        p300.transfer(1, supplements[osteo_supplements['BGP']], well)

    # Transferring hMSC cells to both OS- and OS+ 96 well plates
    hMSC_cells = protocol.load_labware('corning_96_wellplate_360ul_flat', '7', 'hMSC cells')

    for cell_well, os_minus_well, os_plus_well in zip(hMSC_cells.wells(), os_minus_plate.wells(), os_plus_plate.wells()):
        p300.transfer(100, cell_well, os_minus_well)
        p300.transfer(100, cell_well, os_plus_well)
