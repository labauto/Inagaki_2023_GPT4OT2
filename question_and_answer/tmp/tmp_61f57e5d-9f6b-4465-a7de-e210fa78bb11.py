from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'Cell Culture Experiment',
    'author': 'Opentrons'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips20 = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '4')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '5')
    chemicals = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '6')
    cell_suspension = protocol.load_labware('opentrons_96_tiprack_300ul', '7')

    # Pipettes
    p20_single = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips20])

    # Reagents
    dex = chemicals['A1']
    aa = chemicals['B1']
    bgp = chemicals['C1']

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for dest_os_minus in os_minus_plate.wells():
        p20_single.transfer(100, medium_dmem.wells()[0], dest_os_minus)

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for dest_os_plus in os_plus_plate.wells():
        p20_single.transfer(100, medium_dmem_high_glucose.wells()[0], dest_os_plus)

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for dest_os_plus in os_plus_plate.wells():
        p20_single.transfer(0.1, dex, dest_os_plus, mix_after=(3, 20))
        p20_single.transfer(1, aa, dest_os_plus, mix_after=(3, 20))
        p20_single.transfer(1, bgp, dest_os_plus, mix_after=(3, 20))

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for cell_source, dest_os_minus in zip(cell_suspension.wells(), os_minus_plate.wells()):
        p20_single.transfer(100, cell_source, dest_os_minus)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for cell_source, dest_os_plus in zip(cell_suspension.wells(), os_plus_plate.wells()):
        p20_single.transfer(100, cell_source, dest_os_plus)

