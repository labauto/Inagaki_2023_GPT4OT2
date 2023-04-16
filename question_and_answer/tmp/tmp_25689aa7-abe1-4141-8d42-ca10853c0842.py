from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Assistant',
    'description': 'Automated medium exchange for hMSC cell culture using Opentrons',
    'apiLevel': '2.11'
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    pbs_labware = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '3')
    dmem_labware = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '6')
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')

    # Pipette
    p300_multi = protocol.load_instrument('p300_multi', 'right', tip_racks=[tips])

    # Protocol
    pbs_wells = pbs_labware.wells()
    dmem_wells = dmem_labware.wells()
    well_plate_wells = well_plate.wells()

    for well_index, (pbs_well, dmem_well) in enumerate(zip(pbs_wells, dmem_wells)):
        p300_multi.pick_up_tip()

        # Removing the existing medium and wash with PBS(-)
        p300_multi.transfer(200, well_plate_wells[well_index*2], p300_multi.fixed_trash['A1'].top(), new_tip='never')

        # Aspirate PBS(-) from the source tube
        p300_multi.aspirate(200, pbs_well)

        # Dispense into well, mix 3 times, and aspirate
        p300_multi.dispense(200, well_plate_wells[well_index*2])
        p300_multi.mix(3, 200, well_plate_wells[well_index*2])
        p300_multi.aspirate(200, well_plate_wells[well_index*2])

        # Aspirate D-MEM from the source tube
        p300_multi.aspirate(200, dmem_well)

        # Dispense into the well and mix 3 times
        p300_multi.dispense(200, well_plate_wells[well_index*2])
        p300_multi.mix(3, 200, well_plate_wells[well_index*2])

        p300_multi.drop_tip()
