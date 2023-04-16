from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_tube = protocol.load_labware('eppendorf_5ml_snapcap', '2')
    dmem_tube = protocol.load_labware('eppendorf_5ml_snapcap', '3')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300])

    # Protocol
    pbs_source = pbs_tube['A1']
    dmem_source = dmem_tube['A1']

    for well in well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(200, pbs_source)
        p300.dispense(200, well)
        p300.mix(3, 200, well)
        p300.aspirate(200, well)
        p300.dispense(200, pbs_source)
        p300.drop_tip()

        p300.pick_up_tip()
        p300.aspirate(200, dmem_source)
        p300.dispense(200, well)
        p300.mix(3, 200, well)
        p300.drop_tip()
