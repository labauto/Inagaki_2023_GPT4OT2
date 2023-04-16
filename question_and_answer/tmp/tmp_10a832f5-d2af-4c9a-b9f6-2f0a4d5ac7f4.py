
def transfer_medium_os_minus(pipette):
    """Transfer 100 µl of DMEM medium to each well of 96 well plate (OS-)
    Args:
        pipette (obj): Opentrons Pipette
    Returns:
        None
    """
    # Move pipette to source bottle containing DMEM medium
    pipette.pick_up_tip()
    
    # Aspirate 100 µl of DMEM medium into pipette
    pipette.aspirate(100) 
    
    # Move pipette to 96 well plate (OS-)
    pipette.move_to_well('A1')
     
    # Dispense DMEM medium into each well of the 96 well plate
    pipette.dispense(100)
    
    # Move pipette to trash container
    pipette.move_to_trash() 
    
    # Drop the used pipette tip
    pipette.drop_tip()

def transfer_medium_os_plus(pipette):
    """Transfer 100 µl of DMEM high glucose medium to each well of 96 well plate (OS+)
    Args:
        pipette (obj): Opentrons Pipette
    Returns:
        None
    """
    # Move pipette to source bottle containing DMEM high glucose medium
    pipette.pick_up_tip()
    
    # Aspirate 100 µl of DMEM high glucose medium into pipette
    pipette.aspirate(100) 
    
    # Move pipette to 96 well plate (OS+)
    pipette.move_to_well('A1')
     
    # Dispense DMEM high glucose medium into each well of the 96 well plate
    pipette.dispense(100)
    
    # Move pipette to trash container
    pipette.move_to_trash() 
    
    # Drop the used pipette tip
    pipette.drop_tip()

def add_supplements_os_plus(pipette):
    """Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    Args:
        pipette (obj): Opentrons Pipette
    Returns:
        None
    """
    # Move pipette to source bottle containing Dexamethasone
    pipette.pick_up_tip()
    
    # Aspirate 0.1 µl of Dexamethasone into pipette
    pipette.aspirate(0.1) 
    
    # Move pipette to 96 well plate (OS+)
    pipette.move_to_well('A1')
     
    # Dispense Dexamethasone into each well of the 96 well plate
    pipette.dispense(0.1)
    
    # Move pipette to source bottle containing Ascorbic acid
    pipette.move_to_source('Ascorbic Acid')
    
    # Aspirate 1 µl of Ascorbic acid into pipette
    pipette.aspirate(1) 
    
    # Move pipette to 96 well plate (OS+)
    pipette.move_to_well('A1')
     
    # Dispense Ascorbic acid into each well of the 96 well plate
    pipette.dispense(1)
    
    # Move pipette to source bottle containing beta-glycerophosphate
    pipette.move_to_source('Beta-Glycerophosphate')
    
    # Aspirate 1 µl of beta-glycerophosphate into pipette
    pipette.aspirate(1) 
    
    # Move pipette to 96 well plate (OS+)
    pipette.move_to_well('A1')
     
    # Dispense beta-glycerophosphate into each well of the 96 well plate
    pipette.dispense(1)
    
    # Move pipette to trash container
    pipette.move_to_trash() 
    
    # Drop the used pipette tip
    pipette.drop_tip()
    
def transfer_cells_os_minus(pipette):
    """Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    Args:
        pipette (obj): Opentrons Pipette
    Returns:
        None
    """
    # Move pipette to source bottle containing hMSC cells
    pipette.pick_up_tip()
    
    # Aspirate 100 µl of hMSC cells into pipette
    pipette.aspirate(100) 
    
    # Move pipette to 96 well plate (OS-)
    pipette.move_to_well('A1')
     
    # Dispense hMSC cells into each well of the 96 well plate
    pipette.dispense(100)
    
    # Move pipette to trash container
    pipette.move_to_trash() 
    
    # Drop the used pipette tip
    pipette.drop_tip()

def transfer_cells_os_plus(pipette):
    """Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    Args:
        pipette (obj): Opentrons Pipette
    Returns:
        None
    """
    # Move pipette to source bottle containing hMSC cells
    pipette.pick_up_tip()
    
    # Aspirate 100 µl of hMSC cells into pipette
    pipette.aspirate(100) 
    
    # Move pipette to 96 well plate (OS+)
    pipette.move_to_well('A1')
     
    # Dispense hMSC cells into each well of the 96 well plate
    pipette.dispense(100)
    
    # Move pipette to trash container
    pipette.move_to_trash() 
    
    # Drop the used pipette tip
    pipette.drop_tip()

def main():
    """Main function, run the experiment
    Args:
        None
    Returns:
        None
    """
    # Create Opentrons pipette
    pipette = opentrons.instruments.Pipette(axis='b')

    # Transfer DMEM medium to each well of 96 well plate (OS-)
    transfer_medium_os_minus(pipette)
    
    # Transfer DMEM high glucose medium to each well of 96 well plate (OS+)
    transfer_medium_os_plus(pipette)
    
    # Add supplements to each well of 96 well plate (OS+)
    add_supplements_os_plus(pipette)
    
    # Transfer hMSC cells to each well of 96 well plate (OS-)
    transfer_cells_os_minus(pipette)
    
    # Transfer hMSC cells to each well of 96 well plate (OS+)
    transfer_cells_os_plus(pipette)

if __name__ == '__main__':
    main()


:*************************


