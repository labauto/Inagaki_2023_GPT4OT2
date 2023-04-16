from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC cell culture medium exchange',
    'author': 'Your Name <your.email@example.com>',
    'description': 'Medium exchange for hMSC cells using PBS(-) and D-MEM',
    'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '1')
    pbs_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '2')
    dmem_tube = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '3')
    tip_racks_300 = [protocol.load_labware('opentrons_96_tiprack_300ul', slot) for slot in ['4', '5']]

    # Define pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=tip_racks_300)

    # Define reagent positions and volume
    pbs_tube_well = pbs_tube.wells_by_name()['A1']
    dmem_tube_well = dmem_tube.wells_by_name()['A2']
    pbs_volume = 250  # Adjust as necessary
    dmem_volume = 250  # Adjust as necessary

    # Media exchange for all wells in the 6-well plate
    for well in plate_6_well.wells():
        # Aspirate PBS(-)
        p300.pick_up_tip()
        p300.aspirate(pbs_volume, pbs_tube_well)
        
        # Dispense PBS(-) into the cell culture
        p300.dispense(pbs_volume, well) 
        p300.mix(3, int(pbs_volume/2), well)  # Mix the well
        p300.return_tip()
        
        # Aspirate the medium
        p300.pick_up_tip()
        p300.aspirate(pbs_volume, well)
        
        # Discard aspirated medium into the waste container (replace 'waste' with the actual waste container)
        waste = protocol.load_labware('agilent_1_reservoir_290ml', '6').wells_by_name()['A1']
        p300.dispense(pbs_volume, waste)
        p300.return_tip()
        
        # Add fresh D-MEM
        p300.pick_up_tip()
        p300.aspirate(dmem_volume, dmem_tube_well)
        
        # Dispense fresh D-MEM into the 6-well plate
        p300.dispense(dmem_volume, well)
        p300.mix(5, int(dmem_volume/2), well)  # Mix the well
        p300.return_tip()
