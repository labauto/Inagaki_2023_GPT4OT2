from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11',
    'protocolName': 'hMSC Spheroids Experiment'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    plate_os_plus = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    plate_os_minus = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    tuberack = protocol.load_labware('opentrons_15_tuberack_falcon_50ml_conical', '4')
    
    # Pipettes
    pipette = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tip_rack])

    # Reagents
    dmso = tuberack['A1']
    high_glucose_dmso = tuberack['A2']
    dex = tuberack['A3']
    ascorbic_acid = tuberack['A4']
    beta_glycerophosphate = tuberack['A5']
    hmsc_cells = tuberack['A6']

    # Transfer Functions
    def transfer_medium(destination_plate, medium):
        for well in destination_plate.wells():
            pipette.transfer(100, medium, well)
            
    def transfer_supplements(destination_plate):
        for well in destination_plate.wells():
            pipette.transfer(0.1, dex, well)
            pipette.transfer(1, ascorbic_acid, well)
            pipette.transfer(1, beta_glycerophosphate, well)
            
    def transfer_cells(destination_plate):
        for well in destination_plate.wells():
            pipette.transfer(100, hmsc_cells, well)

    # Experiment Steps
    transfer_medium(plate_os_minus, dmso)
    transfer_medium(plate_os_plus, high_glucose_dmso)
    transfer_supplements(plate_os_plus)
    transfer_cells(plate_os_minus)
    transfer_cells(plate_os_plus)

