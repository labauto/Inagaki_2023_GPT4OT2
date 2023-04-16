from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining hMSC Cells to Visualize Lysosomes',
    'author': 'Assistant',
    'apiLevel': '2.9'
}

def run(protocol: protocol_api.ProtocolContext):
    
    # Labware
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    trough_12_wells = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    tiprack_1000ul = protocol.load_labware('opentrons_96_tiprack_1000ul', '3')
    
    # Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_1000ul])

    # Reagents
    cells = plate_6_wells.wells_by_name()['A1']
    lysosome_stain = trough_12_wells.wells_by_name()['A1']
    buffer = trough_12_wells.wells_by_name()['A2']

    # Protocol
    for well in plate_6_wells.wells():
        if not well == cells:
            # Transfer buffer
            p1000.pick_up_tip()
            p1000.transfer(1000, buffer, well, mix_after=(3, 950), new_tip='never')
            p1000.drop_tip()

            # Transfer lysosome stain
            p1000.pick_up_tip()
            p1000.transfer(
                10, lysosome_stain, well.top(-2), mix_after=(3, 10), new_tip='never')
            p1000.drop_tip()

            # Perform an incubation step if necessary, for example:
            # protocol.delay(minutes=30)  # Adjust the time as needed
