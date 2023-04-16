from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    pbs_wells = protocol.load_labware('nest_12_reservoir_15ml', '1').wells()
    dmem_wells = protocol.load_labware('nest_12_reservoir_15ml', '2').wells()
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '3')
    trash = protocol.load_labware('nest_1_reservoir_195ml', 12).wells()[0]

    # Pipettes
    p300 = protocol.load_instrument('p300_single', 'left')

    # Homing the pipette
    p300.home()

    # Set tip trash
    p300.waste_container = trash

    # Protocol steps
    for well in well_plate.wells():
        # Set tip reuse
        p300.pick_up_tip()

        # Aspirate PBS(-) to wash cells
        p300.aspirate(2000, pbs_wells[0])
        p300.dispense(2000, well)

        # Aspirate and dispense again to wash cells
        p300.aspirate(2000, pbs_wells[0])
        p300.dispense(2000, well)

        # Aspirate D-MEM
        p300.aspirate(2000, dmem_wells[0])

        # Dispense the D-MEM to cell culture
        p300.dispense(2000, well)

        # Trash tip
        p300.drop_tip()
