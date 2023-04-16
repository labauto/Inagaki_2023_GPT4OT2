from opentrons import protocol_api

metadata = {
    'apiLevel': '2.0'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plates = [protocol.load_labware('corning_6_wellplate_16.8ml_flat', slot)
              for slot in ['1', '2']]

    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack_300])

    # Define reagents
    e_cadherin = plates[0].wells()[0]
    pbs = plates[0].wells()[1]
    ethanol = plates[0].wells()[2]
    methanol = plates[0].wells()[3]
    blocking_solution = plates[0].wells()[4]
    secondary_antibody = plates[0].wells()[5]

    # Define cells
    cells = plates[1].wells()

    # Transfer e-cadherin to well A1 of the cell plate
    p300.pick_up_tip()
    p300.aspirate(100, e_cadherin)
    p300.dispense(100, cells[0])
    p300.drop_tip()

    # Wash with PBS
    for i in range(3):
        # Add PBS to the well
        p300.pick_up_tip()
        p300.aspirate(150, pbs)
        p300.dispense(150, cells[0])
        p300.drop_tip()

        # Remove PBS from the well
        p300.pick_up_tip()
        p300.aspirate(200, cells[0])
        p300.dispense(200, p300.trash_container.wells()[0])
        p300.drop_tip()

    # Fix cells with methanol followed by ethanol
    # Add methanol to the well
    p300.pick_up_tip()
    p300.aspirate(150, methanol)
    p300.dispense(150, cells[0])
    p300.drop_tip()

    # Incubate for 3 min
    protocol.delay(minutes=3)

    # Remove methanol
    p300.pick_up_tip()
    p300.aspirate(200, cells[0])
    p300.dispense(200, p300.trash_container.wells()[0])
    p300.drop_tip()

    # Wash with ethanol
    for i in range(2):
        # Add ethanol to the well
        p300.pick_up_tip()
        p300.aspirate(150, ethanol)
        p300.dispense(150, cells[0])
        p300.drop_tip()

        # Remove ethanol from the well
        p300.pick_up_tip()
        p300.aspirate(200, cells[0])
        p300.dispense(200, p300.trash_container.wells()[0])
        p300.drop_tip()

    # Block with blocking solution
    p300.pick_up_tip()
    p300.aspirate(200, blocking_solution)
    p300.dispense(200, cells[0])
    p300.drop_tip()

    # Incubate for 1 hour
    protocol.delay(minutes=60)

    # Remove blocking solution
    p300.pick_up_tip()
    p300.aspirate(200, cells[0])
    p300.dispense(200, p300.trash_container.wells()[0])
    p300.drop_tip()

    # Add secondary antibody
    p300.pick_up_tip()
    p300.aspirate(150, secondary_antibody)
    p300.dispense(150, cells[0])
    p300.mix(3, 100, cells[0])
    p300.drop_tip()

    # Incubate for 1 hour
    protocol.delay(minutes=60)

    # Wash with PBS
    for i in range(3):
        # Add PBS to the well
        p300.pick_up_tip()
        p300.aspirate(150, pbs)
        p300.dispense(150, cells[0])
        p300.drop_tip()

        # Remove PBS from the well
        p300.pick_up_tip()
        p300.aspirate(200, cells[0])
        p300.dispense(200, p300.trash_container.wells()[0])
        p300.drop_tip()
