from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Culture Medium exchange',
    'author': 'John Smith <john.smith@example.com>',
    'description': 'Opentrons Sample Protocol'
}

def run(protocol: protocol_api.ProtocolContext):

    # labware
    wells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    dmem = protocol.load_labware('usascientific_12_reservoir_22ml', '3')

    # instrument
    pipette = protocol.load_instrument('p1000_single_gen2', 'left')
    tip_rack = protocol.load_labware('opentrons_96_tiprack_1000ul', '4')
    pipette.start_at_tip(tip_rack.wells()[0])

    # perform experiment
    for well_idx in range(6):
        # aspiration
        pipette.pick_up_tip()
        pipette.aspirate(1000, wells.wells()[well_idx])
        pipette.dispense(1000, pbs.wells()[1])
        pipette.mix(10, 800, pbs.wells()[1])
        pipette.aspirate(1000, pbs.wells()[1])
        pipette.dispense(1000, wells.wells()[well_idx])
        # wash with PBS
        for i in range(2):
            pipette.mix(10, 800, wells.wells()[well_idx])
            pipette.aspirate(1000, wells.wells()[well_idx])
            pipette.dispense(1000, pbs.wells()[i])
        # exchange medium with DMEM
        pipette.aspirate(1000, wells.wells()[well_idx])
        pipette.dispense(1000, dmem.wells()[1])
        pipette.mix(10, 800, dmem.wells()[1])
        pipette.aspirate(1000, dmem.wells()[1])
        pipette.dispense(1000, wells.wells()[well_idx])
        pipette.drop_tip()
