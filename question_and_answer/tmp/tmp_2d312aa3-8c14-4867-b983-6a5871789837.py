from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Viability and Cytotoxicity Assay',
    'author': 'Opentrons',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Define labware
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    falcon_15ml = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '2')
    falcon_50ml = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '3')
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '4')
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_200ul', '5')

    # Define pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20ul])
    p200 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200ul])

    # Step 1
    def clean_robot():
        pass  # Replace with your cleaning process, e.g., using magnetic module, wiping with ethanol, etc.

    # Perform steps 2-9 manually
    # set up the plate, tubes, and dilutions as instructed, then proceed

    # Step 10
    def add_celltox_green():
        celltox_green = falcon_15ml.wells_by_name()['B2']
        p20.transfer(15, celltox_green, plate_96.wells(), new_tip='always', mix_after=(3, 15), touch_tip=True)

    # Step 11
    def orbital_shaking(duration=2, rpm=500):
        pass  # Replace with a custom function to shake the thermal module or perform shaking manually

    # Step 12
    def incubate_rt(duration=15):
        protocol.delay(minutes=duration)

    # Step 13
    def read_fluorescence(excitation=485, emission=520):
        pass  # Replace with the appropriate function for reading the microplate reader or execute the reading manually

    # Step 14
    def add_celltiter_glo():
        celltiter_glo = falcon_15ml.wells_by_name()['B1']
        p200.transfer(80, celltiter_glo, plate_96.wells(), new_tip='always', mix_after=(3, 80), touch_tip=True)

    # Step 15
    def incubate_rt_2(duration=10):
        protocol.delay(minutes=duration)

    # Step 16
    def read_luminescence():
        pass  # Replace with the appropriate function for reading the microplate reader or execute the reading manually

    def main():
        clean_robot()
        add_celltox_green()
        orbital_shaking()
        incubate_rt()
        read_fluorescence()
        add_celltiter_glo()
        incubate_rt_2()
        read_luminescence()

    main()
