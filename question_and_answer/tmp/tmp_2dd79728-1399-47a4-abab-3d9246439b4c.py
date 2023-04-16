
#Import Necessary Libraries
import opentrons
from opentrons import labware, instruments

#Define the functions
def transfer_medium_to_OSminus_plate(pipette, source_plate, dest_plate):
    """
    This function will transfer 100 µl of medium (DMEM) to each well of 96 well plate (OS-)
    """
    for source_well, dest_well in zip(source_plate.wells('A1', to='H12'), dest_plate.wells('A1', to='H12')):
        pipette.transfer(100, source_well, dest_well, new_tip='always')

def transfer_medium_and_supplements_to_OSplus_plate(pipette, source_plate, dest_plate):
    """
    This function will transfer 100 µl of medium (DMEM high glucose) to each well of 96 well plate (OS+),
    and then add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well.
    """
    dex = source_plate.wells('A13')
    aa = source_plate.wells('A14')
    bgp = source_plate.wells('A15')
    for source_well, dest_well in zip(source_plate.wells('A1', to='H12'), dest_plate.wells('A1', to='H12')):
        pipette.transfer(100, source_well, dest_well, new_tip='always')
        pipette.transfer(0.1, dex, dest_well, new_tip='always')
        pipette.transfer(1, aa, dest_well, new_tip='always')
        pipette.transfer(1, bgp, dest_well, new_tip='always')

def transfer_cells_to_plates(pipette, source_plate, dest_plate):
    """
    This function will transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate.
    """
    for source_well, dest_well in zip(source_plate.wells('A1', to='H12'), dest_plate.wells('A1', to='H12')):
        pipette.transfer(100, source_well, dest_well, new_tip='always')
    
    
#Load Labware
plate_6well = labware.load('6-well-plate', '1')
plate_96well_OSminus = labware.load('96-well-plate', '2')
plate_96well_OSplus = labware.load('96-well-plate', '3')
plate_supplements = labware.load('96-well-plate', '4')

#Load Pipettes
pipette = instruments.P300_Multi(mount='left', tip_racks=['A1'])

#Experiment
#Step 1: Transfer medium (DMEM) to 96 well plate (OS-)
transfer_medium_to_OSminus_plate(pipette, plate_6well, plate_96well_OSminus)

#Step 2: Transfer medium (DMEM high glucose) and supplements to 96 well plate (OS+)
transfer_medium_and_supplements_to_OSplus_plate(pipette, plate_6well, plate_96well_OSplus)

#Step 3: Transfer hMSC cells (2,500 cells/100 µl) to both plates
transfer_cells_to_plates(pipette, plate_6well, plate_96well_OSminus)
transfer_cells_to_plates(pipette, plate_6well, plate_96well_OSplus)


:*************************


