from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'protocolName': 'Exchange hMSC Cell Culture Medium',
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_20ul', '1')
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')
    cell_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')
    # Pipettes
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_200])
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tiprack_1000])
    # Reagents
    pbs_minus = reagent_reservoir.wells_by_name()['A1']
    d_mem = reagent_reservoir.wells_by_name()['A2']
    # Protocol
    for well in cell_plate.wells():
        # Remove existing medium
        p1000.pick_up_tip()
        p1000.aspirate(1000, well)
        p1000.dispense(1000, pbs_minus)  # Waste medium disposal
        p1000.drop_tip()

        # Wash cells with PBS(-)
        for _ in range(2):  # Repeat the wash step twice
            p1000.pick_up_tip()
            p1000.aspirate(1000, pbs_minus)
            p1000.dispense(1000, well)
            p1000.mix(3, 800, well)  # Mix to make sure cells are washed
            p1000.aspirate(1000, well)  # Aspirate the wash solution
            p1000.dispense(1000, pbs_minus)  # Waste wash solution disposal
            p1000.drop_tip()

        # Add fresh D-MEM
        p1000.pick_up_tip()
        p1000.aspirate(1000, d_mem)
        p1000.dispense(1000, well)
        p1000.drop_tip()
