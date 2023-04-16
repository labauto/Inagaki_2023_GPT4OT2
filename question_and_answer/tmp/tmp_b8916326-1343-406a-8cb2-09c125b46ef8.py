from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):

    # Helper functions
    def seeding_cells():
        pass

    def prepare_thapsigargin_dilutions():
        pass

    def add_drug_to_wells():
        pass

    def incubate_cells():
        protocol.delay(minutes=72 * 60)

    def measure_cytotoxicity():
        pass

    def shake_and_incubate(sample_plate):
        sample_plate.set_temperature(25)
        protocol.delay(minutes=15)

    def read_fluorescence():
        pass

    def measure_cell_viability():
        pass

    def main():
        seeding_cells()
        prepare_thapsigargin_dilutions()
        add_drug_to_wells()
        incubate_cells()
        measure_cytotoxicity()
        shake_and_incubate(sample_plate)
        read_fluorescence()
        measure_cell_viability()

    # Execute the main experiment workflow
    main()
