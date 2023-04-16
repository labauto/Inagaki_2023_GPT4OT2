from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack_200ul = protocol.load_labware('opentrons_96_tiprack_300ul', 2)

    # Pipettes
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_200ul])

    # Reagents
    hMSC_cells = plate_6_well.wells_by_name()['A1']
    primary_antibody = plate_6_well.wells_by_name()['A2']
    secondary_antibody = plate_6_well.wells_by_name()['A3']
    wash_buffer = plate_6_well.wells_by_name()['A4']
    fixed_cells = plate_6_well.wells_by_name()['A5']
    antibody_dilution_buffer = plate_6_well.wells_by_name()['A6']

    # Protocol
    # 1. Fix cells
    p300.transfer(200, hMSC_cells, fixed_cells)

    # 2. Incubate cells with primary antibody
    p300.pick_up_tip()
    p300.distribute(50, primary_antibody, fixed_cells, new_tip='never')
    p300.drop_tip()

    protocol.delay(minutes=60)  # Incubation time for primary antibody

    # 3. Wash cells with wash buffer
    for _ in range(3):
        p300.transfer(100, wash_buffer, fixed_cells, mix_after=(3, 100))

    # 4. Incubate cells with secondary antibody
    p300.transfer(50, secondary_antibody, fixed_cells)
    protocol.delay(minutes=60)  # Incubation time for secondary antibody

    # 5. Final wash
    for _ in range(3):
        p300.transfer(100, wash_buffer, fixed_cells, mix_after=(3, 100))

    # 6. Add antibody dilution buffer
    p300.transfer(150, antibody_dilution_buffer, fixed_cells)
