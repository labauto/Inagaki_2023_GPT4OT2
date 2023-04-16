from opentrons import protocol_api

metadata = {
    'protocolName': 'Cell Culture Media Exchange',
    'author': 'Your Name',
    'description': 'Media exchange for hMSC cell culture using PBS(-) and DMEM',
    'apiLevel': '2.10'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    p300_rack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    
    # 50 mL tubes for PBS(-) and D-MEM
    # Assuming you're using the "opentrons_6_tuberack_falcon_50ml_conical" labware
    tube_rack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', '3')
    pbs_tube = tube_rack.wells_by_name()['A1']
    dmem_tube = tube_rack.wells_by_name()['A2']
    
    # 6 well plate for cell culture
    well_plate = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '4')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])

    # Removing old media
    for well in well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(270, well)

        # Dispense to waste (assumes you have a waste container in position '5')
        p300.dispense(270, protocol.fixed_trash['A1'])
        p300.drop_tip()

    # Washing cells with PBS(-)
    for well in well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(270, pbs_tube)
        p300.dispense(270, well)
        p300.mix(3, 200, well)
        
        # Removing the PBS(-) from the wells
        p300.aspirate(270, well)
        p300.dispense(270, protocol.fixed_trash['A1'])
        p300.drop_tip()

    # Adding the new D-MEM
    for well in well_plate.wells():
        p300.pick_up_tip()
        p300.aspirate(270, dmem_tube)
        p300.dispense(270, well)
        p300.drop_tip()

