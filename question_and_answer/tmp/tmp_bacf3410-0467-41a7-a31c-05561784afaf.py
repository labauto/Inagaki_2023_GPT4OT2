from opentrons import protocol_api

def transfer_dmem(protocol: protocol_api.ProtocolContext):
    pipette.transfer(100, medium1_tuberack['A1'], dest_plate.columns_by_name()['1'])

def transfer_dmem_high_glucose(protocol: protocol_api.ProtocolContext):
    pipette.transfer(100, medium2_tuberack['A1'], dest_plate.columns_by_name()['2'])

def add_supplements(protocol: protocol_api.ProtocolContext):
    pipette.transfer(0.1, supplement_tuberack['A1'], dest_plate.columns_by_name()['2'], new_tip='always')
    pipette.transfer(1, supplement_tuberack['A2'], dest_plate.columns_by_name()['2'], new_tip='always')
    pipette.transfer(1, supplement_tuberack['A3'], dest_plate.columns_by_name()['2'], new_tip='always')

def transfer_hmsc_cells(protocol: protocol_api.ProtocolContext):
    pipette.transfer(100, cell_tuberack['A1'], dest_plate.columns_by_name()['1'])
    pipette.transfer(100, cell_tuberack['A1'], dest_plate.columns_by_name()['2'])

def run(protocol: protocol_api.ProtocolContext):

    global pipette, medium1_tuberack, medium2_tuberack, supplement_tuberack, cell_tuberack, dest_plate

    # Load labware
    medium1_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 1)
    medium2_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 2)
    supplement_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 3)
    cell_tuberack = protocol.load_labware('opentrons_6_tuberack_nest_15ml_conical', 4)
    dest_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)

    # Load pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 6)])

    # Execute experiment steps
    transfer_dmem(protocol)
    transfer_dmem_high_glucose(protocol)
    add_supplements(protocol)
    transfer_hmsc_cells(protocol)
