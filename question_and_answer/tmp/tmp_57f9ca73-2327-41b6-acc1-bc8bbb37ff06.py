from opentrons import robot, containers, instruments

def transfer_medium(pipette, source, dest):
    pipette.transfer(100, source, dest, new_tip='always')

def add_supplements(pipette, dest):
    pipette.distribute([0.1, 1, 1], dest)

def transfer_cells(pipette, source, dest):
    pipette.transfer(100, source, dest, new_tip='always')

def main():
    robot.connect()
    robot.home()

    # Define the 96 well plates
    plate_os_neg = containers.load('96-flat', 'B1')
    plate_os_pos = containers.load('96-flat', 'C1')

    # Define the tip rack
    tiprack = containers.load('tiprack-200ul', 'A1')

    # Define the pipettes
    pipette_200 = instruments.P200_Single(mount='right', tip_racks=[tiprack])

    # Transfer medium to the wells of the 96 well plates
    transfer_medium(pipette_200, 'DMEM', plate_os_neg)
    transfer_medium(pipette_200, 'DMEM high glucose', plate_os_pos)

    # Add supplements to the wells of the OS+ plate
    add_supplements(pipette_200, plate_os_pos)

    # Transfer cells to the wells of the 96 well plates
    transfer_cells(pipette_200, 'hMSC cells 2,500 cells/100 µl', plate_os_neg)
    transfer_cells(pipette_200, 'hMSC cells 2,500 cells/100 µl', plate_os_pos)

    # Disconnect from the robot
    robot.disconnect()

if __name__ == '__main__':
    main()
