from opentrons import labware, instruments

# Set up labware
source_plate = labware.load('corning_96_wellplate_360ul_flat', '1')
target_plate_os_minus = labware.load('corning_96_wellplate_360ul_flat', '2')
target_plate_os_plus = labware.load('corning_96_wellplate_360ul_flat', '3')

# Set up pipettes
pipette_100 = instruments.P100_Single(mount='right')

def transfer_medium(volume, source_well, target_well):
    # Transfer medium (DMEM) to each well
    pipette_100.transfer(volume, source_plate.wells(source_well),
                         target_plate_os_minus.wells(target_well))

def add_osteo_induction_supplements(dex_volume, aa_volume, bgp_volume, target_well):
    # Add Dex, AA, and BGP to each well in the OS+ plate
    pipette_100.transfer(dex_volume, source_plate.wells('A1'),
                         target_plate_os_plus.wells(target_well))
    pipette_100.transfer(aa_volume, source_plate.wells('A2'),
                         target_plate_os_plus.wells(target_well))
    pipette_100.transfer(bgp_volume, source_plate.wells('A3'),
                         target_plate_os_plus.wells(target_well))

def transfer_cells(volume, source_well, target_well):
    # Transfer cells to each well
    pipette_100.transfer(volume, source_plate.wells(source_well),
                         target_plate_os_minus.wells(target_well))
    pipette_100.transfer(volume, source_plate.wells(source_well),
                         target_plate_os_plus.wells(target_well))

def run_experiment():
    # Transfer medium to all wells in both plates
    for well_idx in range(96):
        transfer_medium(100, well_idx, well_idx)

    # Add osteoinduction supplements to OS+ plate
    for well_idx in range(96):
        add_osteo_induction_supplements(0.1, 1, 1, well_idx)

    # Add cells to all wells in both plates
    for well_idx in range(96):
        transfer_cells(100, 0, well_idx)

if __name__ == '__main__':
    run_experiment()
