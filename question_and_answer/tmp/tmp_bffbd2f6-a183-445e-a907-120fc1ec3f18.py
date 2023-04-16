from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Immunostaining E-Cadherin in iPS cells'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # Pipettes
    pipette = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack])

    # Protocol
    cell_well = plate.wells_by_name()['A1']  # Select the well containing the iPS cells

    # Aspirate and dispense to mix the cells gently
    pipette.pick_up_tip(tiprack['A1'])
    pipette.aspirate(200, cell_well)
    pipette.dispense(200, cell_well)
    pipette.drop_tip()

    # Stain the cells
    # Customize the values as per your staining protocol.
    primary_antibody = plate.wells_by_name()['A2']  # Provide the well containing the primary antibody
    secondary_antibody = plate.wells_by_name()['A3']  # Provide the well containing the secondary antibody

    # Aspirate the cell media
    pipette.pick_up_tip(tiprack['A2'])
    pipette.aspirate(1000, cell_well)
    pipette.dispense(1000, pipette.waste_container.bottom())
    pipette.drop_tip()

    # Add primary antibody
    pipette.pick_up_tip(tiprack['A3'])
    pipette.transfer(200, primary_antibody, cell_well)
    pipette.drop_tip()

    # Incubate the cells
    # Please set the incubation time and temperature as per your protocol
    protocol.delay(minutes=60)  

    # Wash the cells
    # Please customize the washing process as per your protocol
    wash_solution = plate.wells_by_name()['A4']  # Provide the well containing the wash solution
    for i in range(3):
        pipette.pick_up_tip(tiprack['A4'])
        pipette.transfer(1000, wash_solution, cell_well)
        pipette.drop_tip()

    # Add secondary antibody
    pipette.pick_up_tip(tiprack['A5'])
    pipette.transfer(200, secondary_antibody, cell_well)
    pipette.drop_tip()

    # Incubate the cells
    # Please set the incubation time and temperature as per your protocol
    protocol.delay(minutes=60)
