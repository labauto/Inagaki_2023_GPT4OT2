from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining of hMSC Cells',
    'author': 'Opentrons',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')

    # Pipette
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000])

    # Reagents
    primary_antibody = plate_6_well['A1']
    secondary_antibody = plate_6_well['A2']
    wash_buffer = plate_6_well['A3']

    # Wells with cells
    cell_wells = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']

    # Protocol

    # 1. Aspirate 500uL from the primary antibody well and dispense to each well containing cells
    for well in cell_wells:
        p1000.pick_up_tip()
        p1000.aspirate(500, primary_antibody)
        p1000.dispense(500, plate_6_well[well])
        p1000.drop_tip()

    protocol.delay(minutes=60)  # Incubation time for primary antibody

    # 2. Aspirate from the wells containing cells, then wash the wells with wash buffer 3 times
    for i in range(3):  # 3 wash cycles
        for well in cell_wells:
            p1000.pick_up_tip()
            p1000.aspirate(1000, plate_6_well[well])
            p1000.dispense(1000, plate_6_well[wash_buffer])
            p1000.drop_tip()

            p1000.pick_up_tip()
            p1000.aspirate(1000, wash_buffer)
            p1000.dispense(1000, plate_6_well[well])
            p1000.drop_tip()

    # 3. Aspirate 500uL from the secondary antibody well and dispense to each well containing cells
    for well in cell_wells:
        p1000.pick_up_tip()
        p1000.aspirate(500, secondary_antibody)
        p1000.dispense(500, plate_6_well[well])
        p1000.drop_tip()

    protocol.delay(minutes=60)  # Incubation time for secondary antibody

    # 4. Aspirate from the wells containing cells, then wash the wells with wash buffer 3 times
    for i in range(3):  # 3 wash cycles
        for well in cell_wells:
            p1000.pick_up_tip()
            p1000.aspirate(1000, plate_6_well[well])
            p1000.dispense(1000, plate_6_well[wash_buffer])
            p1000.drop_tip()

            p1000.pick_up_tip()
            p1000.aspirate(1000, wash_buffer)
            p1000.dispense(1000, plate_6_well[well])
            p1000.drop_tip()

    protocol.comment('Immunostaining procedure is finished.')
