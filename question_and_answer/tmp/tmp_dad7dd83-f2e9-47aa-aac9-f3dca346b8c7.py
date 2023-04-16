from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture',
    'author': 'Assistant',
    'description': 'Automated hMSC Spheroid Culture with Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    tips_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    tuberack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '4')

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips_200])

    # Reagents
    dmem = tuberack.wells_by_name()['A1']
    dmem_high_glucose = tuberack.wells_by_name()['A2']
    hmsc = tuberack.wells_by_name()['B1']
    dex = tuberack.wells_by_name()['B2']
    aa = tuberack.wells_by_name()['C1']
    bgp = tuberack.wells_by_name()['C2']

    def transfer_medium():
        for well in plate_96.wells():
            p300.pick_up_tip()
            p300.aspirate(100, dmem)
            p300.dispense(100, well)
            p300.drop_tip()

    def transfer_high_glucose_medium():
        for well in plate_96.wells():
            p300.pick_up_tip()
            p300.aspirate(100, dmem_high_glucose)
            p300.dispense(100, well)
            p300.drop_tip()

    def add_supplements():
        for well in plate_96.wells():
            p20.pick_up_tip()
            p20.aspirate(0.1, dex)
            p20.dispense(0.1, well)
            p20.aspirate(1, aa)
            p20.dispense(1, well)
            p20.aspirate(1, bgp)
            p20.dispense(1, well)
            p20.drop_tip()

    def transfer_hmsc_cells():
        for well in plate_96.wells():
            p300.pick_up_tip()
            p300.aspirate(100, hmsc)
            p300.dispense(100, well)
            p300.drop_tip()

    # Main Protocol
    transfer_medium()              # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    transfer_high_glucose_medium() # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    add_supplements()              # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    transfer_hmsc_cells()          # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    transfer_hmsc_cells()          # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
