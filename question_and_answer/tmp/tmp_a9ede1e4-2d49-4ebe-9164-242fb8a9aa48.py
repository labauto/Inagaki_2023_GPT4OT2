from opentrons import simulate, containers, instruments

protocol = simulate.get_protocol_api('2.3')

def count_cells():
    # perform cell counting using Countess 3 machine
    pass

def seed_cells():
    # seed 8000 cells in each well of a 96 well plate
    plate = containers.load('96-flat', 'A1')
    cells = containers.load('tube-rack-2ml', 'B1')
    p1000 = instruments.P1000_Single(
        mount='left',
        tip_racks=[containers.load('tiprack-1000ul', 'D1')]
    )
    cell_vol = 60 # in microL
    for well in plate.wells():
        p1000.pick_up_tip()
        p1000.transfer(cell_vol, cells.wells()[0], well, new_tip='never')
        p1000.drop_tip()

def prepare_drug():
    # prepare drug dilutions and additions
    pass

def add_toxicity_reagent():
    # add CellTox Green reagent to the plate
    plate = containers.load('96-flat', 'A1')
    reagent_tube = containers.load('tube-rack-15_50ml', 'B2')
    p20 = instruments.P20_Single(
        mount='right',
        tip_racks=[containers.load('tiprack-20ul', 'C1')]
    )
    reagent_vol = 15 # in microL
    for i in range(1, 5):
        for j in range(ord('A'), ord('H') + 1):
            well = f'{chr(j)}{i}'
            if j >= ord('D'):
                if i != 4 or j >= ord('G'):
                    continue
            p20.pick_up_tip()
            p20.transfer(reagent_vol, reagent_tube.wells()[0], plate[well], new_tip='never')
            p20.drop_tip()
    # orbital shaking for 2 minutes at 500 rpm
    heater_shaker = instruments.Thermocycler(
        block=containers.load('heater-shaker', 'A1')
    )
    heater_shaker.open_lid()
    heater_shaker.set_lid_temperature(105)
    for i in range(1, 5):
        for j in range(ord('A'), ord('H') + 1):
            well = f'{chr(j)}{i}'
            if j >= ord('D'):
                if i != 4 or j >= ord('G'):
                    continue
            heater_shaker.set_block_temperature(25, hold_time_seconds=900, block_max_volume=40)
            heater_shaker.set_block_temperature(25, hold_time_seconds=60, block_max_volume=40)
            excitation = 485 # in nm
            emission = 520 # in nm
            reading = spectrophotometer.read(well, 'fluorescence', excitation, emission)
            print(f"Fluorescence reading for {well}: {reading}")

def add_viability_reagent():
    # add Cell Titer Glo2.0 reagent to the plate
    plate = containers.load('96-flat', 'A1')
    reagent_tube = containers.load('tube-rack-15_50ml', 'B1')
    p200 = instruments.P200_Single(
        mount='right',
        tip_racks=[containers.load('tiprack-200ul', 'C1')]
    )
    reagent_vol = 80 # in microL
    for i in range(1, 5):
        for j in range(ord('A'), ord('H') + 1):
            well = f'{chr(j)}{i}'
            if j >= ord('D'):
                if i != 4 or j >= ord('G'):
                    continue
            p200.pick_up_tip()
            p200.transfer(reagent_vol, reagent_tube.wells()[0], plate[well], new_tip='never')
            p200.drop_tip()
    # orbital shaking for 2 minutes at 500 rpm
    heater_shaker = instruments.Thermocycler(
        block=containers.load('heater-shaker', 'A1')
    )
    heater_shaker.open_lid()
    heater_shaker.set_lid_temperature(105)
    for i in range(1, 5):
        for j in range(ord('A'), ord('H') + 1):
            well = f'{chr(j)}{i}'
            if j >= ord('D'):
                if i != 4 or j >= ord('G'):
                    continue
            heater_shaker.set_block_temperature(25, hold_time_seconds=600, block_max_volume=200)
            excitation = 530 # in nm
            emission = 570 # in nm
            reading = spectrophotometer.read(well, 'luminescence', excitation, emission)
            print(f"Luminescence reading for {well}: {reading}")

def main():
    # define main function to run the entire protocol
    protocol.home()
    protocol.set_rail_lights(True)
    count_cells()
    seed_cells()
    prepare_drug()
    add_toxicity_reagent()
    add_viability_reagent()

if __name__ == '__main__':
    main()
