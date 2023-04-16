# Import necessary Opentrons modules
from opentrons import protocol_api, labware, instruments

# Define the protocol
metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):

    # Load the labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 1)

    # Define the pipettes and tips
    p300 = instruments.P300_Single(mount='left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', 2)])

    # Protocol steps
    # Add 300 uL of PBS to each well and mix briefly
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, p300.trash_container.top(), well.top(), new_tip='never')
        p300.mix(3, 250, well)
        p300.drop_tip()

    # Remove PBS and add 250 uL of 4% paraformaldehyde, then incubate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, well.top(), p300.trash_container.top(), new_tip='never')
        p300.transfer(250, p300.trash_container.top(), well, new_tip='always')
        p300.mix(3, 200, well)
        p300.drop_tip()

    protocol.comment('Incubating for 15 minutes at room temperature')

    # Remove paraformaldehyde and wash with PBS
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(500, well.top(), p300.trash_container.top(), new_tip='never')
        for i in range(3):
            p300.transfer(700, p300.trash_container.top(), well.top(), mix_after=(3, 500))
        p300.drop_tip()

    # Add permeabilization solution and incubate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, 'permeabilization_solution', well, new_tip='always')
        p300.mix(3, 150, well)
        p300.drop_tip()

    protocol.comment('Incubating for 15 minutes at room temperature')

    # Remove permeabilization solution and wash with PBS
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(500, well.top(), p300.trash_container.top(), new_tip='never')
        for i in range(3):
            p300.transfer(700, p300.trash_container.top(), well.top(), mix_after=(3, 500))
        p300.drop_tip()

    # Add primary antibodies and incubate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, 'primary_antibodies', well, new_tip='always')
        p300.mix(3, 150, well)
        p300.drop_tip()

    protocol.comment('Incubating for 30 minutes at room temperature')

    # Remove primary antibodies and wash with PBS
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(500, well.top(), p300.trash_container.top(), new_tip='never')
        for i in range(3):
            p300.transfer(700, p300.trash_container.top(), well.top(), mix_after=(3, 500))
        p300.drop_tip()

    # Add secondary antibodies and incubate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(300, 'secondary_antibodies', well, new_tip='always')
        p300.mix(3, 150, well)
        p300.drop_tip()

    protocol.comment('Incubating for 30 minutes at room temperature')

    # Remove secondary antibodies and wash with PBS
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(500, well.top(), p300.trash_container.top(), new_tip='never')
        for i in range(3):
            p300.transfer(700, p300.trash_container.top(), well.top(), mix_after=(3, 500))
        p300.drop_tip()

    # Add DAPI and incubate
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(150, 'DAPI', well, new_tip='always')
        p300.mix(3, 75, well)
        p300.drop_tip()

    protocol.comment('Incubating for 10 minutes at room temperature')

    # Finally, remove DAPI and wash with PBS
    for well in plate.wells():
        p300.pick_up_tip()
        p300.transfer(500, well.top(), p300.trash_container.top(), new_tip='never')
        for i in range(3):
            p300.transfer(700, p300.trash_container.top(), well.top(), mix_after=(3, 500))
        p300.drop_tip()

    protocol.comment('Experiment complete!')
