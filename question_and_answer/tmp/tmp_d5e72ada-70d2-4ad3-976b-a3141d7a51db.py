from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids with Osteoinduction Supplements',
    'author': 'Assistant',
    'description': 'Automation of hMSC spheroids with and without osteoinduction supplements using Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    os_minus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    os_plus_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    
    medium_dmem = protocol.load_labware('nest_12_reservoir_15ml', '4')
    medium_dmem_high_glucose = protocol.load_labware('nest_12_reservoir_15ml', '5')
    supplements = protocol.load_labware('nest_12_reservoir_15ml', '6')
    hmsc = protocol.load_labware('corning_24_wellplate_3.4ml_flat', '8')

    # Pipettes
    p20_multi = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=[tiprack_20ul])

    # Transferring medium (DMEM) to OS- wells
    for dest_os_minus in os_minus_plate.wells():
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, medium_dmem.wells()[0], dest_os_minus, new_tip='never')
        p20_multi.drop_tip()

    # Transferring medium (DMEM high glucose) to OS+ wells
    for dest_os_plus in os_plus_plate.wells():
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, medium_dmem_high_glucose.wells()[0], dest_os_plus, new_tip='never')
        p20_multi.drop_tip()

    # Adding osteoinduction supplements (Dex, AA, BGP) to OS+ wells
    dex_well = supplements.wells()[0]
    aa_well = supplements.wells()[1]
    bgp_well = supplements.wells()[2]
    
    for dest_os_plus in os_plus_plate.wells():
        p20_multi.pick_up_tip()
        p20_multi.transfer(0.1, dex_well, dest_os_plus, mix_after=(1, 20), new_tip='never')
        p20_multi.transfer(1, aa_well, dest_os_plus, mix_after=(1, 20), new_tip='never')
        p20_multi.transfer(1, bgp_well, dest_os_plus, mix_after=(1, 20), new_tip='never')
        p20_multi.drop_tip()

    # Transferring hMSC cells to OS- and OS+ wells
    hmsc_well = hmsc.wells()[0]

    for dest_os_minus, dest_os_plus in zip(os_minus_plate.wells(), os_plus_plate.wells()):
        p20_multi.pick_up_tip()
        p20_multi.transfer(100, hmsc_well, dest_os_minus, mix_after=(2, 50), new_tip='never')
        p20_multi.transfer(100, hmsc_well, dest_os_plus, mix_after=(2, 50), new_tip='never')
        p20_multi.drop_tip()
