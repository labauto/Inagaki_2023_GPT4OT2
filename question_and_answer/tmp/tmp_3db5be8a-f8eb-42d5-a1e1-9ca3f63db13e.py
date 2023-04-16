from opentrons import protocol_api

metadata = {
    'protocolName': 'Exchange hMSC Cell Culture Medium',
    'author': 'Your Name',
    'description': 'Opentrons script to exchange hMSC cell culture medium using PBS(-) and D-MEM.',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_200ul', '1')
    pbs_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '2')
    dmem_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3')
    cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_200])

    # Wells for reagents and cell culture
    pbs = pbs_tuberack.wells_by_name()['A1']
    dmem = dmem_tuberack.wells_by_name()['A1']

    for i in range(1, 7):
        well = cell_plate.wells_by_name()[f'A{i}']

        # Remove old medium with PBS(-)
        p300.pick_up_tip()
        p300.aspirate(200, pbs)
        p300.dispense(200, well.top())  # Wash the well with PBS(-)
        p300.aspirate(200, well)  # Aspirate the medium and PBS(-)
        p300.dispense(200, pbs)
        p300.drop_tip()

        # Add D-MEM to the well
        p300.pick_up_tip()
        for _ in range(2):  # Add 400 uL of D-MEM, double pipetting to prevent volume overflow
            p300.aspirate(200, dmem)
            p300.dispense(200, well)
        p300.drop_tip()
