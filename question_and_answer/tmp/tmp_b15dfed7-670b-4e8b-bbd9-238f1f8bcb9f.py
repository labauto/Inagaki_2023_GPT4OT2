from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining hMSC cells for lysosome visualization',
    'author': 'Your Name',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Setup labware
    cell_6_well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2)
    
    # Setup pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_1000ul', 3)])

    # Reagent locations
    dpbs = reagent_reservoir.wells_by_name()['A1']
    fixative = reagent_reservoir.wells_by_name()['A2']
    permeabilization_buffer = reagent_reservoir.wells_by_name()['A3']
    blocking_buffer = reagent_reservoir.wells_by_name()['A4']
    primary_antibody_dilution = reagent_reservoir.wells_by_name()['A5']
    secondary_antibody_dilution = reagent_reservoir.wells_by_name()['A6']

    def wash_cells(well):
        for _ in range(3):
            p1000.transfer(1000, dpbs, well, mix_after=(3, 500), new_tip='always')

    # Immunostaining protocol
    for well in cell_6_well_plate.wells():
        # Fixation
        p1000.transfer(500, fixative, well, new_tip='always')
        protocol.delay(minutes=15)
        wash_cells(well)

        # Permeabilization
        p1000.transfer(500, permeabilization_buffer, well, new_tip='always')
        protocol.delay(minutes=10)
        wash_cells(well)

        # Blocking
        p1000.transfer(500, blocking_buffer, well, new_tip='always')
        protocol.delay(minutes=60)
        wash_cells(well)

        # Primary antibody
        p1000.transfer(500, primary_antibody_dilution, well, new_tip='always')
        protocol.delay(minutes=60)
        wash_cells(well)

        # Secondary antibody
        p1000.transfer(500, secondary_antibody_dilution, well, new_tip='always')
        protocol.delay(minutes=60)
        wash_cells(well)
