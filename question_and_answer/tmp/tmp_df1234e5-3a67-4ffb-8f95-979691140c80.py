
def transferMedium_OSMinus(dest_plate):
    # Transfer 100 µl of medium (DMEM) to each well of the destination plate (OS-)
    # Use the pippette to aspirate 100 µl from the source plate
    pipette.aspirate(100, source_plate)
    # Dispense the 100 µl to each well of the destination plate
    pipette.dispense(dest_plate)

def transferMedium_OSPlus(dest_plate):
    # Transfer 100 µl of medium (DMEM high glucose) to each well of the destination plate (OS+)
    # Use the pippette to aspirate 100 µl from the source plate
    pipette.aspirate(100, source_plate_high_glucose)
    # Dispense the 100 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    
def addSupplements_OSPlus(dest_plate):
    # Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of the destination plate (OS+)
    # Use the pippette to aspirate 0.1 µl of Dex from the source plate
    pipette.aspirate(0.1, source_plate_dex)
    # Dispense the 0.1 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    # Use the pippette to aspirate 1 µl of AA from the source plate
    pipette.aspirate(1, source_plate_aa)
    # Dispense the 1 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    # Use the pippette to aspirate 1 µl of BGP from the source plate
    pipette.aspirate(1, source_plate_bgp)
    # Dispense the 1 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    
def transferCells_OSMinus(dest_plate):
    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of the destination plate (OS-)
    # Use the pippette to aspirate 100 µl from the source plate
    pipette.aspirate(100, source_plate_cells)
    # Dispense the 100 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    
def transferCells_OSPlus(dest_plate):
    # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of the destination plate (OS+)
    # Use the pippette to aspirate 100 µl from the source plate
    pipette.aspirate(100, source_plate_cells)
    # Dispense the 100 µl to each well of the destination plate
    pipette.dispense(dest_plate)
    
def automate_hMSC_spheroids():
    # Automate the process of making hMSC spheroids
    # Transfer medium to the OS- plate
    transferMedium_OSMinus(plate_os_minus)
    # Transfer medium to the OS+ plate
    transferMedium_OSPlus(plate_os_plus)
    # Add supplements to the OS+ plate
    addSupplements_OSPlus(plate_os_plus)
    # Transfer cells to the OS- plate
    transferCells_OSMinus(plate_os_minus)
    # Transfer cells to the OS+ plate
    transferCells_OSPlus(plate_os_plus)
    
    # End
    print("Experiment Finished!")
    
automate_hMSC_spheroids()


:*************************


