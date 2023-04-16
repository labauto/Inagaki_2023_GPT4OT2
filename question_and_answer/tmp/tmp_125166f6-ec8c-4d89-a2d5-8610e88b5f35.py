from opentrons import protocol_api

metadata = {
    'protocolName': 'ImmunoStaining of hMSC Cells',
    'author': 'Your Name',
    'description': 'Automated cell preparation to visualize lysosomes in hMSC cells',
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Wells in the 6-well plate (assuming four wells are filled with hMSC cells)
    wells = ['A1', 'A2', 'A3', 'A4']

    # Reagents (assuming you have fixed and permeabilized cells)
    immunostain_solution = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '3')
    staining = immunostain_solution.wells_by_name()['A1']

    wash_solution = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '4')
    wash = wash_solution.wells_by_name()['A2']

    # Perform the immunostaining experiment
    for well in wells:
        # Pipette the staining solution into the well
        p300.pick_up_tip()
        p300.aspirate(100, staining)
        p300.dispense(100, six_well_plate.wells_by_name()[well])
        p300.blow_out()
        p300.drop_tip()

        # Incubate for desired time (e.g., 1 hour) at room temperature in the dark
        protocol.delay(minutes = 60)

        # Wash the wells
        for wash_round in range(3):
            p300.pick_up_tip()
            p300.aspirate(200, wash)
            p300.dispense(200, six_well_plate.wells_by_name()[well])
            p300.blow_out()
            p300.drop_tip()

            # Incubate for desired time (e.g., 5 minutes) at room temperature
            protocol.delay(minutes = 5)
