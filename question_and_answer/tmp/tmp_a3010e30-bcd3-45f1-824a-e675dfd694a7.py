metadata = {
    'protocolName': 'Cell Culture Experiment',
    'author': 'Your Name',
    'description': 'Automating the process of cell culture using the Opentrons machine.',
    'apiLevel': '2.0'
}

def transfer_medium(volume, plate, condition):
    """
    Transfer 100 µl of medium (DMEM or DMEM high glucose) each well of 96 well plate (OS- or OS+).
    """
    tiprack_1 = labware.load('opentrons-tiprack-300ul', '7')
    p300 = instruments.P300_Single(
        mount='right',
        tip_racks=[tiprack_1]
    )
    for well in plate:
        if condition == "OS+":
            p300.transfer(volume, medium_high_glucose.wells(well), plate.wells(well), new_tip='always')
        elif condition == "OS-":
            p300.transfer(volume, medium.wells(well), plate.wells(well), new_tip='always')

def add_supplements(volume, plate):
    """
    Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl \
    of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    """
    tiprack_1 = labware.load('opentrons-tiprack-300ul', '7')
    p10 = instruments.P10_Single(
        mount='left',
        tip_racks=[tiprack_1]
    )
    for well in plate:
        p10.transfer(0.1, dex, plate.wells(well), new_tip='always')
        p10.transfer(1, aa, plate.wells(well), new_tip='always')
        p10.transfer(1, bgp, plate.wells(well), new_tip='always')

def transfer_cells(volume, plate, cells):
    """
    Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS- or OS+)
    """
    tiprack_1 = labware.load('opentrons-tiprack-300ul', '7')
    p300 = instruments.P300_Single(
        mount='right',
        tip_racks=[tiprack_1]
    )
    for well in plate:
        p300.transfer(volume, cells.wells(0), plate.wells(well), new_tip='always')

def run(protocol):
    """
    This is your protocol's run function.
    """
    tiprack_2 = labware.load('opentrons-tiprack-10ul', '6')
    p10 = instruments.P10_Single(
        mount='left',
        tip_racks=[tiprack_2]
    )

    # Load labwares and reagents
    pcr_plate_96 = protocol.load_labware('sarstedt_96_wellplate_200ul', '1')
    medium = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    medium_high_glucose = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    dex = reagents.load('dexamethasone', '4', 'dexamethasone')
    aa = reagents.load('ascorbic_acid', '5', 'ascorbic_acid')
    bgp = reagents.load('beta-glycerophosphate', '6', 'beta-glycerophosphate')
    hMSC_cells = reagents.load('hMSC_cells', '8', 'hMSC_cells')

    # Define the plate wells for each condition (OS- and OS+)
    os_neg_wells = [str(i) for i in range(1, 7)]
    os_pos_wells = [str(i) for i in range(7, 13)]

    # Transfer medium
    transfer_medium(100, pcr_plate_96, "OS+")
    transfer_medium(100, pcr_plate_96, "OS-")

    # Add supplements to OS+
    add_supplements(100, pcr_plate_96.columns(os_pos_wells))

    # Transfer cells
    transfer_cells(100, pcr_plate_96.columns(os_pos_wells), hMSC_cells)
    transfer_cells(100, pcr_plate_96.columns(os_neg_wells), hMSC_cells)
