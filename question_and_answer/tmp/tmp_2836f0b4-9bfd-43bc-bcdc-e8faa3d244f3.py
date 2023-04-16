from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroid Culture Protocol',
    'author': 'Your Name Here',
    'description': 'A protocol for culturing hMSC spheroids with or without osteoinduction supplements using the Opentrons machine',
    'apiLevel': 2.0
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate_96_well_TC = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    plate_6_well_TC = protocol.load_labware('corning_6_wellplate_16.4ml_flat', '2')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300])

    # Reagent and Sample Location
    source_location_os = plate_6_TC['A1']
    source_location_aa = plate_6_TC['B1']
    source_location_bgp = plate_6_TC['C1']
    source_location_dex = plate_6_TC['D1']

    dest = { 'OS+': plate_96_well_TC.rowsByWell()[0]['1'], 'OS-': plate_96_well_TC.rowsByWell()[0]['2'] }

    # Transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    for well in dest['OS-']:
        transfer(source_location_os, well, 100)

    # Transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+)
    for well in dest['OS+']:
        transfer(source_location_os, well, 100)

    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in dest['OS+']:
        p300.pick_up_tip()
        p300.aspirate(0.1, source_location_dex)
        p300.dispense(0.1, well)
        p300.aspirate(1, source_location_aa)
        p300.dispense(1, well)
        p300.aspirate(1, source_location_bgp)
        p300.dispense(1, well)
        p300.drop_tip()

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    for well in dest['OS-']:
        transfer(source_location_os, well, 100)

    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    for well in dest['OS+']:
        transfer(source_location_os, well, 100)

def transfer(source, dest, vol):
    p300.pick_up_tip()
    p300.aspirate(vol, source)
    p300.dispense(vol, dest)
    p300.aspirate(20, dest.top())
    p300.drop_tip()
