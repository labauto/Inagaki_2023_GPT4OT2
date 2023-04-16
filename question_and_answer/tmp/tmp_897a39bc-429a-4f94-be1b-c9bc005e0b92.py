from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Your Name Here',
    'description': 'Automated hMSC spheroid culture with Opentrons',
    'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    dmem = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    cells = protocol.load_labware('corning_96_wellplate_360ul_flat', '4')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '5')])
    p10 = protocol.load_instrument('p10_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_10ul', '6')])
    
    # Steps
    def transfer_to_plate(volume, source, dest):
        for i in range(96):
            p300.pick_up_tip()
            p300.aspirate(volume, source[i])
            p300.dispense(volume, dest[i])
            p300.drop_tip()
            
    def add_supplements():
        for i in range(96):
            p10.pick_up_tip()
            p10.aspirate(0.1, protocol.parse_tube('A1', 'opentrons/opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap').bottom(1))
            p10.aspirate(1.0, protocol.parse_tube('A2', 'opentrons/opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap').bottom(1))
            p10.aspirate(1.0, protocol.parse_tube('A3', 'opentrons/opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap').bottom(1))
            p10.dispense_at_volume(0.1, os_plus[i].bottom(1))
            p10.dispense_at_volume(1.0, os_plus[i].bottom(1))
            p10.dispense_at_volume(1.0, os_plus[i].bottom(1))
            p10.blow_out()
            p10.drop_tip()
        
    transfer_to_plate(100, dmem.wells(), os_minus.wells())
    transfer_to_plate(100, protocol.parse_tube('A4', 'opentrons/opentrons_24_tuberack_eppendorf_1.5ml_snapcap').bottom(1), os_plus.wells())
    add_supplements()
    transfer_to_plate(100, cells.wells(), os_minus.wells())
    transfer_to_plate(100, cells.wells(), os_plus.wells())
