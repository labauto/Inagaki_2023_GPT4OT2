from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    dmem_container = protocol.load_labware('nest_1_reservoir_195ml', '1')
    dmem_high_glucose_container = protocol.load_labware('nest_1_reservoir_195ml', '2')
    hmsc_container = protocol.load_labware('nest_1_reservoir_195ml', '3')
    plate_os_negative = protocol.load_labware('corning_96_wellplate', '5')
    plate_os_positive = protocol.load_labware('corning_96_wellplate', '6')

    supplements_container = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '4')
    dex = supplements_container['A1']
    aa = supplements_container['B1']
    bgp = supplements_container['C1']

    # Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right')
    p10 = protocol.load_instrument('p10_single_gen2', 'left')

    # Functions
    def transfer_medium(pipette, source_medium, destination_plate, volume):
        for well in destination_plate.wells():
            pipette.transfer(volume, source_medium, well)

    def add_supplements(pipette, supplements, destination_plate, volumes):
        for well in destination_plate.wells():
            for supplement, volume in zip(supplements, volumes):
                pipette.transfer(volume, supplement, well)

    def transfer_cells(pipette, source_cells, destination_plate, volume):
            for well in destination_plate.wells():
                pipette.transfer(volume, source_cells, well)

    # Main Function
    transfer_medium(p1000, dmem_container['A1'], plate_os_negative, 100) # OS- DMEM transfer
    transfer_medium(p1000, dmem_high_glucose_container['A1'], plate_os_positive, 100) # OS+ DMEM High Glucose transfer
    add_supplements(p10, [dex, aa, bgp], plate_os_positive, [0.1, 1, 1]) # Add supplements to OS+ wells
    transfer_cells(p1000, hmsc_container['A1'], plate_os_negative, 100) # Transfer hMSC to OS- wells
    transfer_cells(p1000, hmsc_container['A1'], plate_os_positive, 100) # Transfer hMSC to OS+ wells
