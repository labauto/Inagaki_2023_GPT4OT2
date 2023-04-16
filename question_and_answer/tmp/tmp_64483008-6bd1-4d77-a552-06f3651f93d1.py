from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining hMSC cells for E-Cadherin',
    'author': 'Opentrons',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    
    # Setup Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_1])
    
    # Reagents
    cell_culture_medium = reservoir.wells_by_name()['A1']
    blocking_solution = reservoir.wells_by_name()['A2']
    primary_antibody_solution_ecad = reservoir.wells_by_name()['A3']
    secondary_antibody_solution = reservoir.wells_by_name()['A4']
    
    # Perform the experiment
    # --- Step 1: Aspirate cells from cell culture medium
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(50, cell_culture_medium)
        p300.dispense(50, well)
        p300.mix(3, 50, well)
        p300.blow_out(well.top())
        p300.drop_tip()

    # --- Step 2: Apply blocking solution
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(50, blocking_solution)
        p300.dispense(50, well)
        p300.mix(3, 50, well)
        p300.blow_out(well.top())
        p300.drop_tip()

    # --- Step 3: Apply primary anti-E-cadherin antibody solution
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(50, primary_antibody_solution_ecad)
        p300.dispense(50, well)
        p300.mix(3, 50, well)
        p300.blow_out(well.top())
        p300.drop_tip()

    # --- Step 4: Apply secondary antibody solution
    for well in plate.wells():
        p300.pick_up_tip()
        p300.aspirate(50, secondary_antibody_solution)
        p300.dispense(50, well)
        p300.mix(3, 50, well)
        p300.blow_out(well.top())
        p300.drop_tip()
