from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Assay using Opentrons',
    'author': 'Opentrons Helper',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    tips_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)
    tuberack_15 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    tuberack_15_slot7 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    heater_shaker = protocol.load_module('Temperature Module Gen2', 3)

    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_20])
    p200 = protocol.load_instrument('p200_single_gen2', 'left', tip_racks=[tips_200])

    # Variables
    cell_tox_green = tuberack_15['B2']
    cell_titer_glo = tuberack_15['B1']
    thapsigargin = tuberack_15_slot_repo['A1']

    def seed_cells():
        # Code to seed cells (a specific seeding function may not be necessary if the process is mostly manual)

    def clean_robot():
        # Clean the inside of the robot with 70 % ethanol
        pass

    def turn_hepa_filter(duration, fan_speed):
        # Turn on/off HEPA filter at set fan_speed and duration
        pass

    def add_controls():
        # Add medium to wells A5 to C5 as negative control
        pass

    def prepare_stock_thapsigargin():
        # Prepare dilutions of initial stocks of thapsigargin in 10% Ham's F12K medium
        pass

    def prepare_2x_and_4x_thapsigargin():
        # Prepare 2x and 4x concentrations of thapsigargin
        pass

    def add_2x_thapsigargin_to_plate():
        # Add the equal volume of 2x thapsigargin to each well of 96 well plate
        pass

    def add_cell_tox_green():
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            for col in range(1, 6):
                well = row + str(col)
                p20.transfer(15, cell_tox_green, plate_96[well], mix_before=(3, 15))

    def shake_and_incubate(incubation_time):
        # Orbital shaking and incubation as per instructions
        pass

    def measure_fluorescence():
        # Measure fluorescence after adding CellTox Green
        pass

    def add_cell_titer_glo():
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            for col in range(1, 6):
                well = row + str(col)
                p200.transfer(80, cell_titer_glo, plate_96[well])

    def measure_luminescence():
        # Measure luminescence after adding CellTiter Glo
        pass

    def main():
        clean_robot()
        turn_hepa_filter(60, 'low')
        seed_cells()
        add_controls()
        prepare_stock_thapsigargin()
        prepare_2x_and_4x_thapsigargin()
        add_2x_thapsigargin_to_plate()
        add_cell_tox_green()
        shake_and_incubate(15)
        measure_fluorescence()
        add_cell_titer_glo()
        shake_and_incubate(10)
        measure_luminescence()

    main()
