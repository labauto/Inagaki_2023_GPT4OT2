from opentrons import protocol_api

metadata = {
    'protocolName': 'Immunostaining of hMSC cells to visualize lysosomes',
    'author': 'Your Name',
    'description': 'Automated immunostaining protocol for lysosomes in hMSC cells',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):

    # Labware
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '9')
    reagent_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '5')
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', '8')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '3')

    # Pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])

    # Reagents
    pbs_wash = reagent_reservoir.wells()[0]
    primary_antibody = reagent_reservoir.wells()[1]
    secondary_antibody = reagent_reservoir.wells()[2]
    cell_culture_medium = reagent_reservoir.wells()[3]

    # Immunostaining Procedure

    # Aspirate the culture medium
    for well in plate_6_wells.wells():
        p300.pick_up_tip()
        p300.aspirate(200, well)
        p300.dispense(200, p300.waste_container)
        p300.drop_tip()

    # Wash the cells 3 times with PBS
    for _ in range(3):
        for well in plate_6_wells.wells():
            p300.transfer(200, pbs_wash, well, mix_after=(3, 150), new_tip='always')

    # Add primary antibody
    p20.transfer(20, primary_antibody, [well.top() for well in plate_6_wells.wells()], new_tip='always')

    # Incubate for 1 hour at room temperature
    protocol.delay(minutes=60)

    # Aspirate the primary antibody
    for well in plate_6_wells.wells():
        p300.pick_up_tip()
        p300.aspirate(200, well)
        p300.dispense(200, p300.waste_container)
        p300.drop_tip()

    # Wash the cells 3 times with PBS
    for _ in range(3):
        for well in plate_6_wells.wells():
            p300.transfer(200, pbs_wash, well, mix_after=(3, 150), new_tip='always')

    # Add secondary antibody
    p20.transfer(20, secondary_antibody, [well.top() for well in plate_6_wells.wells()], new_tip='always')

    # Incubate for 1 hour at room temperature
    protocol.delay(minutes=60)

    # Aspirate the secondary antibody
    for well in plate_6_wells.wells():
        p300.pick_up_tip()
        p300.aspirate(200, well)
        p300.dispense(200, p300.waste_container)
        p300.drop_tip()

    # Wash the cells 3 times with PBS
    for _ in range(3):
        for well in plate_6_wells.wells():
            p300.transfer(200, pbs_wash, well, mix_after=(3, 150), new_tip='always')

    # Add cell culture medium
    for well in plate_6_wells.wells():
        p300.transfer(200, cell_culture_medium, well, mix_after=(3, 150), new_tip='always')
