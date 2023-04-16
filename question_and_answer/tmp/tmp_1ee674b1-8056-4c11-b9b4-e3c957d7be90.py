from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Exchange hMSC Cell Culture Medium',
    'author': 'Assistant',
    'description': 'An Opentrons protocol for exchanging hMSC cell culture medium in a 6 well plate',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
  
    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    pbs_tube = protocol.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', '3')
    dmem_tube = protocol.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', '4')

    # Load pipette
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Pick up a tip
    pipette.pick_up_tip()

    # Remove old medium
    for well in plate.wells():
        pipette.aspirate(1000, well)
        pipette.dispense(1000, well.top())

    # Wash wells with PBS
    for well in plate.wells():
        pipette.transfer(1000, pbs_tube.wells()[0], well, mix_after=(3, 1000), new_tip='never')

    # Remove PBS
    for well in plate.wells():
        pipette.aspirate(1000, well)
        pipette.dispense(1000, well.top())

    # Add new D-MEM
    for well in plate.wells():
        pipette.transfer(1000, dmem_tube.wells()[0], well, new_tip='never')

    # Drop the tip
    pipette.drop_tip()
