from opentrons import protocol_api

metadata = {
    'protocolName': 'Exchange hMSC Cell Culture Medium',
    'author': 'Assistant',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_source = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    dmem_source = protocol.load_labware('usascientific_12_reservoir_22ml', '3')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')
    
    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Protocol
    pbs_well = pbs_source.wells()[0]
    dmem_well = dmem_source.wells()[0]

    for well in well_plate.wells():
        # Remove old medium with PBS
        p300.pick_up_tip()
        p300.aspirate(290, pbs_well)
        p300.dispense(290, well)
        p300.mix(3, 200, well)
        p300.aspirate(290, well)
        p300.dispense(290, pbs_well)
        p300.drop_tip()

        # Add new D-MEM medium
        p300.pick_up_tip()
        p300.aspirate(290, dmem_well)
        p300.dispense(290, well)
        p300.mix(3, 200, well)
        p300.drop_tip()
