from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', 4)
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 1)
    tips_200 = [protocol.load_labware('opentrons_96_tiprack_200ul', slot)
                for slot in [2, 3, 6, 7, 8, 9]]

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tips_200)

    # Reagents
    dmemo_os_minus = tuberack['A1']
    dmemo_high_glucose_os_plus = tuberack['A2']
    dex = tuberack['A3']
    aa = tuberack['A4']
    bgp = tuberack['A5']

    # Helper functions
    def transfer_medium(src, dest_plate):
        dest_wells = dest_plate.wells()
        for well in dest_wells:
            p300.pick_up_tip()
            p300.aspirate(100, src)
            p300.dispense(100, well)
            p300.drop_tip()

    def transfer_high_glucose_medium():
        transfer_medium(dmemo_high_glucose_os_plus, plate_os_plus)

    def transfer_dmemo_os_minus_medium():
        transfer_medium(dmemo_os_minus, plate_os_minus)

    def add_supplements():
        dest_wells = plate_os_plus.wells()
        for well in dest_wells:
            p300.pick_up_tip()
            p300.aspirate(0.1, dex)
            p300.aspirate(1, aa)
            p300.aspirate(1, bgp)
            p300.dispense(2.1, well)
            p300.drop_tip()

    # Protocol
    transfer_dmemo_os_minus_medium()  # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    transfer_high_glucose_medium()  # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    add_supplements()  # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
