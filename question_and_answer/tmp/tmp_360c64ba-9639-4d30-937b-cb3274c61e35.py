from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    # labware setup
    plate_6 = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)

    # instrument setup
    pipette_200 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])
    
    # reagent setup
    buffer_wash = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)['A1']

    # perform immunostaining protocol
    for well in plate_6.wells():
        # Add fixative
        pipette_200.pick_up_tip()
        pipette_200.aspirate(100, buffer_wash)
        pipette_200.dispense(plate['A1'])
        pipette_200.mix(5, 80)
        pipette_200.drop_tip()

        # Add permeabilization buffer
        pipette_200.pick_up_tip()
        pipette_200.aspirate(100, buffer_wash)
        pipette_200.dispense(plate['B1'])
        pipette_200.mix(5, 80)
        pipette_200.drop_tip()

        # Add primary antibody
        pipette_200.pick_up_tip()
        pipette_200.aspirate(50, buffer_wash)
        pipette_200.dispense(plate['C1'])
        pipette_200.mix(5, 50)
        pipette_200.drop_tip()

        # Add secondary antibody
        pipette_200.pick_up_tip()
        pipette_200.aspirate(50, buffer_wash)
        pipette_200.dispense(plate['D1'])
        pipette_200.mix(5, 50)
        pipette_200.drop_tip()

        # Add DAPI
        pipette_200.pick_up_tip()
        pipette_200.aspirate(10, buffer_wash)
        pipette_200.dispense(plate['E1'])
        pipette_200.mix(5, 20)
        pipette_200.drop_tip()

        # Add wash buffer
        pipette_200.pick_up_tip()
        pipette_200.aspirate(200, buffer_wash)
        pipette_200.dispense(plate['F1'])
        pipette_200.mix(5, 150)
        pipette_200.drop_tip()
