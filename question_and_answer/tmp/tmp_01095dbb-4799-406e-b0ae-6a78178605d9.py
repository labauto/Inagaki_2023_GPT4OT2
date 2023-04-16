
#Import packages 
import opentrons
import time

# Start the Opentrons robot
robot = opentrons.Robot()

# Define functions for each step
def transfer_medium(plate_type):
    """ Transfer 100 µl of medium (DMEM) or medium (DMEM high glucose) to each well of 96 well plate (OS-) or 96 well plate (OS+)
    
    Args:
        plate_type (str): either "OS-" or "OS+"
    """
    
    # Define the source and destination for each plate type
    if plate_type == "OS-":
        source_plate = opentrons.labware.load('96-flat', '7')
        dest_plate = opentrons.labware.load('96-flat', '10')
    elif plate_type == "OS+":
        source_plate = opentrons.labware.load('96-flat', '9')
        dest_plate = opentrons.labware.load('96-flat', '11')
    
    # Transfer 100 µl of medium to each well of the destination plate
    tip_rack = opentrons.labware.load('tiprack-200ul', '5')
    pipette = robot.new_pipette(
        axis='a',
        max_volume=200,
        tip_racks=[tip_rack],
        )
    for well in dest_plate.rows():
        for source_well in source_plate.rows():
            pipette.transfer(
                volume=100,
                source=source_well,
                dest=well
            )

def add_osteoinduction_supplements(plate_type):
    """ Add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid), and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    
    Args:
        plate_type (str): either "OS-" or "OS+"
    """
    
    # Add osteoinduction supplements to OS+ plate
    if plate_type == "OS+":
        dest_plate = opentrons.labware.load('96-flat', '11')
        
        tip_rack = opentrons.labware.load('tiprack-200ul', '6')
        pipette = robot.new_pipette(
            axis='a',
            max_volume=200,
            tip_racks=[tip_rack],
            )
        for well in dest_plate.rows():
            pipette.transfer(
                volume=0.1,
                source=opentrons.labware.load('trough-12row', '8')['A1'],
                dest=well
                )
            pipette.transfer(
                volume=1,
                source=opentrons.labware.load('trough-12row', '8')['A2'],
                dest=well
                )
            pipette.transfer(
                volume=1,
                source=opentrons.labware.load('trough-12row', '8')['A3'],
                dest=well
                )

def transfer_cells(plate_type):
    """ Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-) or 96 well plate (OS+)
    
    Args:
        plate_type (str): either "OS-" or "OS+"
    """
    
    # Transfer cells to the appropriate plate
    if plate_type == "OS-":
        dest_plate = opentrons.labware.load('96-flat', '10')
    elif plate_type == "OS+":
        dest_plate = opentrons.labware.load('96-flat', '11')
    
    # Transfer 100 µl of cells to each well of the destination plate
    tip_rack = opentrons.labware.load('tiprack-200ul', '4')
    pipette = robot.new_pipette(
        axis='a',
        max_volume=200,
        tip_racks=[tip_rack],
        )
    for well in dest_plate.rows():
        pipette.transfer(
            volume=100,
            source=opentrons.labware.load('trough-12row', '8')['A4'],
            dest=well
            )

# Main function
def run_experiment():
    """Run the Opentrons robot to make hMSC spheroids with two different conditions"""
    
    robot.reset()
    robot.home()
    
    #Transfer medium
    transfer_medium("OS-")
    transfer_medium("OS+")
    
    #Add osteoinduction supplements
    add_osteoinduction_supplements("OS+")
    
    #Transfer cells
    transfer_cells("OS-")
    transfer_cells("OS+")
    
    #End
    robot.reset()
    robot.home()
    print('Experiment finished!')
    return

#Run the experiment
run_experiment()


:*************************


