from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3')
    scm_tuberack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '6')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '8')

    # Pipette
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Wells
    pbs_well = pbs_tuberack['A1']
    scm_well = scm_tuberack['A1']
    plate_wells = ['A1', 'B1', 'A2', 'B2']

    # Protocol
    for well in plate_wells:
        dest = six_well_plate.wells_by_name()[well]
        p300.pick_up_tip()
        p300.aspirate(200, pbs_well)
        p300.dispense(200, dest)
        p300.mix(5, 200, dest)
        p300.aspirate(200, dest)
        p300.dispense(200, pbs_well)
        p300.drop_tip()
        
        p300.pick_up_tip()
        p300.aspirate(200, scm_well)
        p300.dispense(200, dest)
        p300.mix(5, 200, dest)
        p300.blow_out(dest)
        p300.drop_tip()
