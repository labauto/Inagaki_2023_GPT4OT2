from opentrons import protocol_api

metadata = {
    'apiLevel': '2.9',
    'protocolName': 'hMSC Cell Culture Medium Exchange',
    'author': 'Assistant',
    'description': 'Automating cell culture medium exchange of hMSC cells'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tips_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')
    p300rack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    dmem = protocol.load_labware('nest_12_reservoir_15ml', '2')
    pbs = protocol.load_labware('nest_12_reservoir_15ml', '3')
    six_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '5')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[p300rack])
    p200 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips_200])

    # Wells
    dmem_media = dmem.wells_by_name()['A1']
    pbs_media = pbs.wells_by_name()['A1']

    # Cell culture wells
    well_names = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
    cell_culture_wells = [six_well_plate.wells_by_name()[well] for well in well_names]

    # Aspiration and Dispense speeds
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 150
    p200.flow_rate.aspirate = 80
    p200.flow_rate.dispense = 80

    def medium_exchange(well, old_medium_vol, pbs_vol, dmem_vol):
        # Remove old medium
        p300.pick_up_tip()
        p300.aspirate(old_medium_vol, well)
        p300.dispense(old_medium_vol, pbs.wells_by_name()['A12'])  # Discard old medium
        p300.drop_tip()

        # Wash with PBS(-) twice
        for _ in range(2):
            p200.pick_up_tip()
            p200.aspirate(pbs_vol, pbs_media)
            p200.dispense(pbs_vol, well)
            p200.aspirate(pbs_vol, well)
            p200.dispense(pbs_vol, pbs.wells_by_name()['A12'])  # Discard PBS
            p200.drop_tip()

        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(dmem_vol, dmem_media)
        p300.dispense(dmem_vol, well)
        p300.drop_tip()

    old_medium_vol = 2000
    pbs_vol = 1000
    dmem_vol = 2000

    # Perform medium exchange for each well
    for well in cell_culture_wells:
        medium_exchange(well, old_medium_vol, pbs_vol, dmem_vol)
