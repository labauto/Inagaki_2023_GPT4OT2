from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'hMSC Spheroids Experiment',
    'author': 'Your Name',
    'description': 'Script for creating hMSC spheroids with and without osteoinduction supplements',
    'apiLevel': '2.10'
}

# Protocol definition
def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    dmso_rack = protocol.load_labware('opentrons_96_deepwellplate_2ml', '2')
    dmso_rack_high_glucose = protocol.load_labware('opentrons_96_deepwellplate_2ml', '3')
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul', '4')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul', '5')
    hMSC_cells_tube = protocol.load_labware('opentrons_15_tuberack_falcon_50ml_conical', '6')

    # Pipettes
    p300_single = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Reagent preparation
    hMSC_cells = hMSC_cells_tube.wells()[0]
    dmem = dmso_rack.wells()[0]
    dmem_high_glucose = dmso_rack_high_glucose.wells()[0]

    dex = dmso_rack.wells()[1]
    aa = dmso_rack.wells()[2]
    bgp = dmso_rack.wells()[3]

    # Transfer functions
    def dispense_medium_to_os_minus():
        for well in plate_os_minus.wells():
            p300_single.pick_up_tip()
            p300_single.aspirate(100, dmem)
            p300_single.dispense(100, well)
            p300_single.drop_tip()

    def dispense_medium_and_supplements_to_os_plus():
        for well in plate_os_plus.wells():
            p300_single.pick_up_tip()
            p300_single.aspirate(100, dmem_high_glucose)
            p300_single.dispense(100, well)

            p300_single.aspirate(0.1, dex)
            p300_single.dispense(0.1, well)

            p300_single.aspirate(1, aa)
            p300_single.dispense(1, well)

            p300_single.aspirate(1, bgp)
            p300_single.dispense(1, well)
            p300_single.drop_tip()

    def transfer_hMSC_cells(os_minus=True):
        if os_minus:
            target_wells = plate_os_minus.wells()
        else:
            target_wells = plate_os_plus.wells()

        for well in target_wells:
            p300_single.pick_up_tip()
            p300_single.aspirate(100, hMSC_cells)
            p300_single.dispense(100, well)
            p300_single.drop_tip()

    # Perform experiment
    dispense_medium_to_os_minus()
    dispense_medium_and_supplements_to_os_plus()
    transfer_hMSC_cells(os_minus=True)
    transfer_hMSC_cells(os_minus=False)

