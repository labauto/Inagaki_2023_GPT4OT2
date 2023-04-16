from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'MSC spheroid',
    'author': 'Name <email@example.com>',
    'description': 'Culture hMSC cells and form spherorids with or without osteoinduction supplements',
    'apiLevel': '2.10'
}

# number of tipracks to load for each pipette
tipracks_300_count = 2
tipracks_10_count = 1

# labware
plate_96_well = 'corning_96_wellplate_360ul_flat'
plate_6_well = 'corning_6_wellplate_16.8ml_flat'

tiprack_300_name = 'opentrons_96_tiprack_300ul'
tiprack_10_name = 'opentrons_96_tiprack_10ul'

if not protocol_api.labware.get_labware(plate_96_well):
    raise Exception(f"Labware {plate_96_well} not found in the labware library")
plate_96_well = protocol_api.labware.get_labware(plate_96_well)

if not protocol_api.labware.get_labware(plate_6_well):
    raise Exception(f"Labware {plate_6_well} not found in the labware library")
plate_6_well = protocol_api.labware.get_labware(plate_6_well)

tiprack_300_ul = [protocol_api.labware.get_labware(tiprack_300_name)]
for i in range(tipracks_300_count - 1):
    tiprack_300_ul.append(protocol_api.labware.load(tiprack_300_name, str(i)))

tiprack_10_ul = [protocol_api.labware.get_labware(tiprack_10_name)]
for i in range(tipracks_10_count - 1):
    tiprack_10_ul.append(protocol_api.labware.load(tiprack_10_name, str(i)))

# pipettes
pipette_300 = protocol.load_instrument('p300_single', mount='right', tip_racks=tiprack_300_ul)
pipette_10 = protocol.load_instrument('p10_single', mount='left', tip_racks=tiprack_10_ul)

def run(protocol: protocol_api.ProtocolContext):
    # transfer 100ul DMEM to each well of 96 well plate (OS-)
    pipette_300.pick_up_tip()
    for well in plate_96_well.rows_by_name()['A']:
        pipette_300.transfer(100, protocol_api.labware.get_labware('nest_12_reservoir_15ml').wells()[0], well, new_tip='never')
    pipette_300.drop_tip()

    # transfer 100ul DMEM high glucose and supplements to each well of 96 well plate (OS+)
    pipette_10.pick_up_tip()
    for well in plate_96_well.rows_by_name()['B']:
        pipette_10.transfer(100, protocol_api.labware.get_labware('nest_12_reservoir_15ml').wells()[1], well, new_tip='never')
    pipette_10.drop_tip()

    pipette_10.pick_up_tip()
    for well in plate_96_well.rows_by_name()['C']:
        pipette_10.transfer(
            0.1, 
            protocol_api.labware.get_labware('nest_12_reservoir_1.5ml').wells()[0],
            well, 
            new_tip='never'
        )
        pipette_10.transfer(
            1,
            protocol_api.labware.get_labware('nest_12_reservoir_1.5ml').wells()[1],
            well, 
            new_tip='never'
        )
        pipette_10.transfer(
            1,
            protocol_api.labware.get_labware('nest_12_reservoir_1.5ml').wells()[2],
            well, 
            new_tip='never'
        )
    pipette_10.drop_tip()

    # transfer 100ul hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS-)
    pipette_300.pick_up_tip()
    for well in plate_96_well.rows_by_name()['A']:
        pipette_300.transfer(100, protocol_api.labware.get_labware('nest_12_reservoir_15ml').wells()[2], well, mix_after=(3, 100), new_tip='always')
    pipette_300.drop_tip()

    # transfer 100ul hMSC cells (2,500 cells/100 µl) to each well of 96 well plate (OS+)
    pipette_300.pick_up_tip()
    for well in plate_96_well.rows_by_name()['B']:
        pipette_300.transfer(100, protocol_api.labware.get_labware('nest_12_reservoir_15ml').wells()[2], well, mix_after=(3, 100), new_tip='always')
    pipette_300.drop_tip()
