from opentrons import protocol_api

metadata = {
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    pbs_minus_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')
    dmem_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '4')

    # pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_200])

    # reagents
    pbs_minus = pbs_minus_tube.wells_by_name()['A1']
    dmem = dmem_tube.wells_by_name()['A1']

    # protocol

    for well_idx in range(6):  # Iterate through each well in the 6-well plate
        well = six_well_plate.wells()[well_idx]

        # Aspirate the cell culture medium
        pipette.pick_up_tip()
        pipette.aspirate(300, well)
        pipette.dispense(300, pbs_minus)
        pipette.drop_tip()

        # Wash the well with PBS(-)
        for _ in range(2):
            pipette.pick_up_tip()
            pipette.transfer(300, pbs_minus, well, new_tip='never')
            pipette.aspirate(300, well)
            pipette.dispense(300, pbs_minus)
            pipette.drop_tip()

        # Transfer D-MEM to the well
        pipette.pick_up_tip()
        pipette.transfer(300, dmem, well, new_tip='never')
        pipette.mix(3, 300, well)
        pipette.drop_tip()
