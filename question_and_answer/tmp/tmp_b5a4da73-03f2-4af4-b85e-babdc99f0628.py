from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load custom labware
    custom_labware_dir = "/path/to/your/custom/labware"
    custom_plate_def = "6_well_plate.json"
    plate_6_well = protocol.load_labware_from_definition(
        custom_labware_dir + "/" + custom_plate_def, location='1', label='6_well_plate'
    )

    # Load tips and pipettes
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    pipette_300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Specify the wells containing reagents
    cell_culture_wells = ['A1', 'A2', 'A3']
    primary_antibody = plate_6_well['A4']
    secondary_antibody = plate_6_well['B1']
    wash_buffer = plate_6_well['B2']

    # Perform steps for the immunostaining protocol
    for well in cell_culture_wells:
        # Wash with wash buffer
        pipette_300.pick_up_tip()
        pipette_300.transfer(200, wash_buffer, plate_6_well[well], mix_after=(3, 200), new_tip='never')
        pipette_300.drop_tip()

        # Incubate with primary antibody
        pipette_300.pick_up_tip()
        pipette_300.transfer(200, primary_antibody, plate_6_well[well], mix_after=(3, 200), new_tip='never')
        pipette_300.drop_tip()

    protocol.delay(minutes=60)  # Incubation time for primary antibody

    for well in cell_culture_wells:
        # Wash with wash buffer
        pipette_300.pick_up_tip()
        pipette_300.transfer(200, wash_buffer, plate_6_well[well], mix_after=(3, 200), new_tip='never')
        pipette_300.drop_tip()

        # Incubate with secondary antibody
        pipette_300.pick_up_tip()
        pipette_300.transfer(200, secondary_antibody, plate_6_well[well], mix_after=(3, 200), new_tip='never')
        pipette_300.drop_tip()

    protocol.delay(minutes=60)  # Incubation time for secondary antibody
