from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC cell culture and spheroid creation',
    'author': 'Your Name Here',
    'description': 'Automated cell culture and spheroid formation using Opentrons',
    'apiLevel': '2.0'
}

# Define custom function for adding supplements to OS+ wells
def add_supplements(pipette, plate):
    pipette.pick_up_tip()
    for well in plate.wells():
        pipette.aspirate(0.1, dex)
        pipette.aspirate(1, aa)
        pipette.aspirate(1, bgp)
        pipette.dispense(2.1, well) # aspirate vol + dispense vols = 2.1 µl
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):

    # Load the tiprack and pipette
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '1')
    pipette_1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Load the 6-well plate
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Load the 96-well plate
    plate_96_well = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')

    # Define the media (DMEM and DMEM high glucose)
    dmem = plate_96_well.rows()[0][0].top()  # used for both OS- and OS+
    dmem_high_glucose = plate_96_well.rows()[0][1].top()  # used only for OS+

    # Define the supplements (Dexamethasone, Ascorbic acid, beta-glycerophosphate)
    dex = protocol.load_labware('opentrons_96_tiprack_1.5ml_snapcap', '4').wells_by_name()['A1']
    aa = protocol.load_labware('opentrons_96_tiprack_1.5ml_snapcap', '5').wells_by_name()['A1']
    bgp = protocol.load_labware('opentrons_96_tiprack_1.5ml_snapcap', '6').wells_by_name()['A1']

    # Add 100 µl of DMEM to each well in plate_96_well (OS-)
    pipette_1000.pick_up_tip()
    for well in plate_96_well.wells():
        pipette_1000.aspirate(100, dmem)
        pipette_1000.dispense(100, well.top(-5))
    pipette_1000.drop_tip()

    # Add 100 µl of DMEM high glucose to each well in plate_96_well (OS+)
    pipette_1000.pick_up_tip()
    for well in plate_96_well.wells():
        pipette_1000.aspirate(100, dmem_high_glucose)
        pipette_1000.dispense(100, well.top(-5))
    pipette_1000.drop_tip()

    # Add supplements to OS+ wells (0.1 µl Dexamethasone, 1 µl Ascorbic acid, and 1 µl beta-glycerophosphate)
    add_supplements(pipette_1000, plate_96_well.columns()[1])

    # Add 100 µl of hMSC cells to each well in plate_96_well (OS-)
    pipette_1000.pick_up_tip()
    for well in plate_96_well.wells():
        pipette_1000.aspirate(100, plate_6_well.wells_by_name()['A1'])
        pipette_1000.dispense(100, well.top(-5))
    pipette_1000.drop_tip()

    # Add 100 µl of hMSC cells to each well in plate_96_well (OS+)
    pipette_1000.pick_up_tip()
    for well in plate_96_well.wells():
        pipette_1000.aspirate(100, plate_6_well.wells_by_name()['A1'])
        pipette_1000.dispense(100, well.top(-5))
    pipette_1000.drop_tip()
