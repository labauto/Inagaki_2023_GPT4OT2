from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Opentrons',
    'description': 'Automated hMSC spheroid culture with and without osteoinduction (OS+ and OS-)',
    'apiLevel': '2.7'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    medium1_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', 1)
    medium2_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', 4)
    hMSC_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_50ml_conical', 3)
    reagent_tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 5)
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 6)])
    p10 = protocol.load_instrument('p10_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_10ul', 7)])
    
    # Reagents
    dm_low = medium1_tuberack.wells()[0]
    dm_high = medium2_tuberack.wells()[0]
    dex = reagent_tuberack.wells("A1")
    aa = reagent_tuberack.wells("A2")
    bgp = reagent_tuberack.wells("A3")
    hMSC = hMSC_tuberack.wells()[0]
    
    # Protocol
    for well in plate.wells():
        # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
        p300.transfer(100, dm_low, well)

    for well_number, well in enumerate(plate.wells()):
        # Skip the first half of the wells (OS- wells)
        if well_number < 48:
            continue
        # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
        p300.transfer(100, dm_high, well)
        # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
        p10.transfer(0.1, dex, well, mix_after=(3, 5))
        p10.transfer(1, aa, well, mix_after=(3, 5))
        p10.transfer(1, bgp, well, mix_after=(3, 5))

    for well_number, well in enumerate(plate.wells()):
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
        if well_number < 48:
            p300.transfer(100, hMSC, well, mix_after=(3, 5))
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
        else:
            p300.transfer(100, hMSC, well, mix_after=(3, 5))

