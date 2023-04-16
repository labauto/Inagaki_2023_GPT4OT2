# Import necessary Opentrons modules and protocols
from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell culture medium exchange',
    'author': 'Your Name',
    'description': 'Protocol for exchanging hMSC cell culture medium using PBS(-) and SCM130',
    'apiLevel': '2.10'
}

# Define a protocol function
def run(protocol: protocol_api.ProtocolContext):

    # Load labware
    plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', '2')
    tip_racks = [protocol.load_labware('opentrons_96_tiprack_300ul', slot)
                 for slot in ['3', '6', '9']]

    # Load pipettes
    p50_single = protocol.load_instrument('p50_single', 'left', tip_racks=tip_racks)

    # Define plate wells
    plate_wells = [well for row in plate.rows() for well in row]

    # Define reagent wells
    pbs_well = tube_rack['A1']
    scm130_well = tube_rack['A2']

    # Define waste well
    waste_well = plate.wells()[1]

    # Distribute PBS to wells
    p50_single.pick_up_tip()
    for well in plate_wells:
        p50_single.transfer(150, pbs_well, well.bottom(2), new_tip='never')
    p50_single.drop_tip()

    # Remove PBS from wells
    p50_single.pick_up_tip()
    for well in plate_wells:
        p50_single.transfer(175, well.bottom(1), waste_well, new_tip='never')
    p50_single.drop_tip()

    # Distribute SCM130 to wells
    p50_single.pick_up_tip()
    for well in plate_wells:
        p50_single.transfer(150, scm130_well, well.bottom(2), new_tip='never')
    p50_single.drop_tip()

