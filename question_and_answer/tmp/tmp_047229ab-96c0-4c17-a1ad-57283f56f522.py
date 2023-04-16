from opentrons import protocol_api

metadata = {
    'apiLevel': '2.2'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware and instruments
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 6)
    dilution_rack = protocol.load_labware('opentrons_20_tuberack_nest_box_reservoir_single_row', 7)
    tips20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tips200 = protocol.load_labware('opentrons_96_tiprack_200ul', 4)
    
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tips20])
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips200])
    
    # A549 cell seeding
    cell_suspension = tube_rack.wells_by_name()['A1']
    for well in plate_96.wells():
        p300.pick_up_tip()
        p300.aspirate(60, cell_suspension)
        p300.dispense(60, well)
        p300.blow_out()
        p300.drop_tip()
    
    # Prepare dilutions
    tuberack_dilutions = dilution_rack.wells_by_name()
    tuberack_sources = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1']
    dilutions_sources = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    
    for source, dest in zip(tuberack_sources, dilutions_sources):
        p20.pick_up_tip()
        p20.aspirate(25, tuberack_dilutions[source])
        p20.dispense(25, tuberack_dilutions[dest])
        p20.blow_out()
        p20.drop_tip()
    
    for source, dest in zip(dilutions_sources, tuberack_sources):
        p20.pick_up_tip()
        p20.mix(3, 25, tuberack_dilutions[source])
        p20.aspirate(25, tuberack_dilutions[source])
        p20.dispense(25, tuberack_dilutions[dest])
        p20.blow_out()
        p20.drop_tip()
    
    # Adding various concentrations of Thapsigargin
    for index, well in enumerate(plate_96.wells()):
        if index + 1 <= 72:  # Skip medium control
            volume = 60
            source_index = index % 8
            drug_source_well = dilution_rack.wells()[source_index]
            
            p20.pick_up_tip()
            p20.transfer(volume, drug_source_well, well, mix_before=(3, 20), new_tip='never')
            p20.blow_out()
            p20.drop_tip()
    
    # Implementation of additional steps (incubation, measurement of viability and cytotoxicity, etc.)
    # will depend on the specific devices used in your setup, as well as possible integration with other scripts.
    # It is recommended to consult the official Opentrons and the device manufacturer's documentation for further information.

