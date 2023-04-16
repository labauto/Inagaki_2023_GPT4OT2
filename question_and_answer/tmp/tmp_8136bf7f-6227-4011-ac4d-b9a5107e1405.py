from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_tube = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '2')
    dmem_tube = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', '3')
    
    # Pipettes
    left_pipette = protocol.load_instrument('p1000_single', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', '4')])
    right_pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '5')])
    
    # Wells
    wells = six_well_plate.wells()
    pbs_well = pbs_tube['A1']
    dmem_well = dmem_tube['A1']

    # Exchanging cell culture medium
    for well in wells:
        # Aspirating old medium (you can adjust the volume according to the medium amount in your wells)
        left_pipette.pick_up_tip()
        left_pipette.aspirate(1000, well)
        left_pipette.dispense(1000, well.top()) # Dispense to waste
        left_pipette.drop_tip()

        # Washing with PBS(-) 2 times (you can adjust the volume and the times if necessary)
        for _ in range(2):
            right_pipette.pick_up_tip()
            right_pipette.aspirate(200, pbs_well)
            right_pipette.dispense(200, well)
            right_pipette.mix(3, 200, well) # Mixing PBS(-) and old medium
            right_pipette.aspirate(200, well)
            right_pipette.dispense(200, well.top()) # Dispense to waste
            right_pipette.drop_tip()

        # Adding D-MEM (you can adjust the volume according to the desired amount in your wells)
        right_pipette.pick_up_tip()
        right_pipette.aspirate(200, dmem_well)
        right_pipette.dispense(200, well)
        right_pipette.drop_tip()

    protocol.comment('Cell culture medium exchange completed.')
