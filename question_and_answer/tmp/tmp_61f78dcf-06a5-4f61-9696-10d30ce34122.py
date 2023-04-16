from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids',
    'author': 'Your Name Here',
    'description': 'Automated production of hMSC spheroids with and without osteoinduction supplements using Opentrons robot.',
    'apiLevel': '2.10'
}

def load_labware_or_die(
            protocol_context: protocol_api.ProtocolContext,
            labware_name: str,
            location: str) -> protocol_api.labware.Labware:
    if labware_name not in protocol_context.load_labware_by_name:
        raise RuntimeError(f"labware {labware_name} is not recognized in Opentrons ecosystem")
    try:
        labware = protocol_context.load_labware(
            labware_name,
            location)
    except Exception as e:
        raise RuntimeError(f"cannot load labware {labware_name} at {location}: {str(e)}") from e
    return labware

def run(protocol: protocol_api.ProtocolContext):
    
    # Load labware
    plate_96_os_plus = load_labware_or_die(protocol, 'corning_96_wellplate_360ul_flat', '1')
    plate_96_os_minus = load_labware_or_die(protocol, 'corning_96_wellplate_360ul_flat', '2')
    plate_6_os_plus = load_labware_or_die(protocol, 'nunc_6_wellplate_16.7ml', '3')
    tiprack_1 = load_labware_or_die(protocol, 'opentrons_96_tiprack_300ul', '4')
    tiprack_2 = load_labware_or_die(protocol, 'opentrons_96_tiprack_10ul', '5')

    # Load pipettes
    p300 = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tiprack_1])
    p10 = protocol.load_instrument('p10_single', mount='right', tip_racks=[tiprack_2])
    pipette_offset = 12  # distance to add between wells when using the same tips

    # Transferring medium (DMEM) to both plates
    target_wells = plate_96_os_plus.wells() + plate_96_os_minus.wells()
    p300.pick_up_tip()
    for target_well in target_wells:
        p300.transfer(100, protocol.load_labware('axygen_96_degree_1.2ml_cluster_tubes', '7').wells(0), target_well.top(), new_tip='never')
        p300.blow_out(target_well.top())
        p300.move_to(target_well.top(-5))
        protocol.max_speeds['Z'] = 10
        p300.move_to(target_well.top())
        p300.move_to(target_well.top(-5))
        p300.drop_tip()
        p300.pick_up_tip()

    # Making spheroids without osteoinduction supplements (OS-)
    p300.drop_tip()
    for i, target_well in enumerate(plate_96_os_minus.wells()):
        p300.pick_up_tip()
        p300.aspirate(100, protocol.load_labware('axygen_96_degree_1.2ml_cluster_tubes', '8').wells(i))
        p300.dispense(100, target_well)
        p300.blow_out(target_well.top())
        p300.touch_tip(radius=0.5, v_offset=-5)
        p300.move_to(target_well.top(-5))
        protocol.max_speeds['Z'] = 10
        p300.move_to(target_well.top())
        p300.move_to(target_well.top(-5))
        p300.drop_tip()

    # Making spheroids with osteoinduction supplements (OS+)
    for i, (target_well, sup_well) in enumerate(zip(plate_96_os_plus.wells(), protocol.load_labware('thermofisher_96_wellplate_100ul', '9').wells())):
        p300.pick_up_tip()
        p300.aspirate(100, protocol.load_labware('axygen_96_degree_1.2ml_cluster_tubes', '8').wells(i))
        p300.dispense(100, target_well)
        p300.blow_out(target_well.top())
        p10.pick_up_tip()
        p10.aspirate(0.1, sup_well.bottom(6))
        p10.touch_tip(radius=0.5, v_offset=-5)
        p10.dispense(0.1, target_well.bottom(2))
        p10.drop_tip()
        p10.pick_up_tip()
        p10.aspirate(1, sup_well.bottom(6))
        p10.touch_tip(radius=0.5, v_offset=-5)
        p10.dispense(1, target_well.bottom(2))
        p10.drop_tip()
        p10.pick_up_tip()
        p10.aspirate(1, sup_well.bottom(6))
        p10.touch_tip(radius=0.5, v_offset=-5)
        p10.dispense(1, target_well.bottom(2))
        p10.drop_tip()
        p300.touch_tip(radius=0.5, v_offset=-5)
        p300.move_to(target_well.top(-pipette_offset))
        protocol.max_speeds['Z'] = 10
        p300.move_to(target_well.top())
        p300.move_to(target_well.top(-pipette_offset))
        p300.drop_tip()   

    # Transfering hMSC cells
    source_plate_96 = load_labware_or_die(protocol, 'biorad_96_wellplate_200ul_pcr', '10')
    for i, target_well in enumerate(plate_96_os_plus.rows('A')):
        p300.pick_up_tip()
        p300.aspirate(100, source_plate_96.rows('A').wells(i))
        p300.dispense(100, target_well)
        p300.blow_out(target_well.top())
        p300.touch_tip(radius=0.5, v_offset=-5)
        p300.move_to(target_well.top(-pipette_offset))
        protocol.max_speeds


:*************************


