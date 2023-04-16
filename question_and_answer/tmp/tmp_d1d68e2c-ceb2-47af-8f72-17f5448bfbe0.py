from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Assistant',
    'description': 'Automated experiment with hMSC cells',
    'apiLevel': '2.9'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labwares
    tiprack_p20 = protocol.load_labware('opentrons_96_tiprack_20ul', 2)
    medium1_tuberack = protocol.load_labware('nest_6_tuberack_15ml_conical', 1)
    medium2_tuberack = protocol.load_labware('nest_6_tuberack_15ml_conical', 3)
    supplement_tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)
    cell_suspension_tuberack = protocol.load_labware('nest_6_tuberack_15ml_conical', 5)
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 6)
    plate_2 = protocol.load_labware('corning_96_wellplate_360ul_flat', 7)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_p20])

    # Reagents
    medium1 = medium1_tuberack.wells_by_name()['A1']
    medium2 = medium2_tuberack.wells_by_name()['A1']
    dex = supplement_tuberack.wells_by_name()['A1']
    aa = supplement_tuberack.wells_by_name()['B1']
    bgp = supplement_tuberack.wells_by_name()['C1']
    cell_suspension = cell_suspension_tuberack.wells_by_name()['A1']

    # Step 1: Transfer medium (DMEM) for OS-
    def transfer_medium_os_minus():
        for well in plate_1.wells():
            p20.transfer(100, medium1, well, mix_after=(3, 100), new_tip='always')

    # Step 2: Transfer medium (DMEM high glucose) for OS+
    def transfer_medium_os_plus():
        for well in plate_2.wells():
            p20.transfer(100, medium2, well, new_tip='always')

    # Step 3: Add supplements to OS+
    def add_supplements_to_os_plus():
        for well in plate_2.wells():
            p20.transfer(0.1, dex, well, mix_after=(3, 20), new_tip='always')
            p20.transfer(1, aa, well, mix_after=(3, 20), new_tip='always')
            p20.transfer(1, bgp, well, mix_after=(3, 20), new_tip='always')

    # Step 4: Transfer hMSC cells to OS- and OS+
    def transfer_cells_to_os_minus_and_os_plus():
        for well in plate_1.wells():
            p20.transfer(100, cell_suspension, well, mix_after=(3, 100), new_tip='always')
        for well in plate_2.wells():
            p20.transfer(100, cell_suspension, well, mix_after=(3, 100), new_tip='always')

    # Execute experiment steps
    transfer_medium_os_minus()
    transfer_medium_os_plus()
    add_supplements_to_os_plus()
    transfer_cells_to_os_minus_and_os_plus()

