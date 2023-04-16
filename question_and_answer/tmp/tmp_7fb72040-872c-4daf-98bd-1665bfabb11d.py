from opentrons import simulate, containers, instruments

# create custom labware for 96-well plates
backward_compatible_tiprack_1ml = containers.load(
    "opentrons_96_tiprack_300ul", "A1", "tiprack-200ul"
)

os_minus_plate = containers.load(
    "96-flat",
    "B1",
    "os-minus-plate"
)
os_plus_plate = containers.load(
    "96-flat",
    "C1",
    "os-plus-plate"
)

samples = containers.load(
    "96-flat",
    "D1",
    "samples"
)


def prepare_os_minus_wells():
    os_minus_wells = os_minus_plate.wells()
    # transfer 100 µl DMEM to each well of 96 well plate (OS-)
    m300.transfer(100, dmem.wells()[0], os_minus_wells, new_tip='always')


def prepare_os_plus_wells():
    os_plus_wells = os_plus_plate.wells()
    # transfer 100 µl DMEM high glucose to each well of 96 well plate (OS+)
    m300.transfer(100, dmem_high_glucose.wells()[0], os_plus_wells, new_tip='always')
    # add 0.1 µl of Dex (Dexamethasone), 1 µl of AA (Ascorbic acid),
    # and 1 µl of BGP (beta-glycerophosphate) to each well of 96 well plate (OS+)
    for well in os_plus_wells:
        m10.transfer(0.1, dex.wells()[0], well, new_tip='always')
        m10.transfer(1.0, aa.wells()[0], well, new_tip='always')
        m10.transfer(1.0, bgp.wells()[0], well, new_tip='always')


def transfer_hmsc_cells():
    num_samples = len(samples.wells())
    for i in range(num_samples):
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
        m300.transfer(100, samples.wells()[i], os_minus_plate.wells()[i], new_tip='always')
        # Transfer 100 µl of hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
        m300.transfer(100, samples.wells()[i], os_plus_plate.wells()[i], new_tip='always')


def main():
    prepare_os_minus_wells()
    prepare_os_plus_wells()
    transfer_hmsc_cells()


if __name__ == '__main__':
    # set up
    m300 = instruments.P300_Multi(
        mount="left",
        tip_racks=[backward_compatible_tiprack_1ml],
    )
    m10 = instruments.P10_Multi(
        mount="right",
        tip_racks=[backward_compatible_tiprack_1ml],
    )
    dmem = containers.load("trough-12row", "A1")
    dmem_high_glucose = containers.load("trough-12row", "A2")
    dex = containers.load("trough-12row", "A3")
    aa = containers.load("trough-12row", "A4")
    bgp = containers.load("trough-12row", "A5")

    # run the experiment
    main()
