import opentrons.simulation

# Define the main function to run the experiment
def main():

    # Load the 6-well and 96-well plates
    plate_6_well = opentrons.simulation.plate('corning_6_wellplate_16.8ml_flat')
    plate_96_well = opentrons.simulation.plate('corning_96_wellplate_flat')

    # Define the locations of the wells in the plates
    wells_6_well = [well for col in plate_6_well.cols() for well in col]
    wells_96_well = [well for col in plate_96_well.cols() for well in col]

    # Define the volumes of the reagents and cells to transfer
    vol_medium = 100 # µl
    vol_suppl = {'Dex': 0.1, 'AA': 1, 'BGP': 1} # µl
    vol_cells = 100 # µl
    cell_density = 2500 # cells/100 µl

    # Transfer medium to the 96-well plate for OS-
    opentrons.simulation.comment('Adding DMEM medium to the 96-well plate for OS-')
    for well in wells_96_well:
        opentrons.simulation.pipette(
            source=None,
            dest=well,
            volume=vol_medium,
            trash=False
        )

    # Transfer medium and supplements to the 96-well plate for OS+
    opentrons.simulation.comment('Adding DMEM high-glucose medium and supplements to the 96-well plate for OS+')
    for well in wells_96_well:
        opentrons.simulation.pipette(
            source=None,
            dest=well,
            volume=vol_medium,
            trash=False
        )
        for suppl, vol in vol_suppl.items():
            opentrons.simulation.pipette(
                source=None,
                dest=well,
                volume=vol,
                trash=False
            )

    # Transfer cells to the 96-well plate for OS- and OS+
    opentrons.simulation.comment('Adding cells to the 96-well plate for both conditions')
    for i, well in enumerate(wells_96_well):
        source_well = wells_6_well[i % 6]
        opentrons.simulation.pipette(
            source=source_well,
            dest=well,
            volume=vol_cells,
            trash=False
        )

# Run the experiment in simulation
opentrons.simulation.run(main)
