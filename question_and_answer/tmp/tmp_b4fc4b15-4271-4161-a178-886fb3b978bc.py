from opentrons import protocol_api

metadata = {
    'protocolName': 'hMSC Spheroids',
    'author': 'Your Name',
    'description': 'Automated hMSC spheroids culture with and without osteoinduction supplements',
    'apiLevel': '2.10'
}

# define the experiment
def run(protocol: protocol_api.ProtocolContext):

    # load labware
    plate_96_well_OSminus = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate_96_well_OSplus = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    plate_6_well = protocol.load_labware('corning_6_wellplate_16.8ml_flat', 3)
    tiprack_1000ul = protocol.load_labware('opentrons_96_tiprack_1000ul', 4)

    # load pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', mount='left', tip_racks=[tiprack_1000ul])

    # transfer DMEM to 96 well plates 'plate_96_well_OSminus' and 'plate_96_well_OSplus'
    p1000.pick_up_tip()
    for well in plate_96_well_OSminus.wells():
        p1000.aspirate(100, plate_6_well.wells_by_name()['A1'])
        p1000.dispense(plate_96_well_OSminus.wells_by_name()[well])
    p1000.drop_tip()

    p1000.pick_up_tip()
    for well in plate_96_well_OSplus.wells():
        p1000.aspirate(100, plate_6_well.wells_by_name()['A2'])
        p1000.dispense(plate_96_well_OSplus.wells_by_name()[well])
    p1000.drop_tip()

    # add OS+ supplements to plate_96_well_OSplus
    p1000.pick_up_tip()
    for well in plate_96_well_OSplus.wells():
        p1000.aspirate(0.1, plate_6_well.wells_by_name()['B1'])
        p1000.aspirate(1, plate_6_well.wells_by_name()['B2'])
        p1000.aspirate(1, plate_6_well.wells_by_name()['B3'])
        p1000.dispense(plate_96_well_OSplus.wells_by_name()[well])
    p1000.drop_tip()

    # transfer hMSC cells to plate_96_well_OSminus and plate_96_well_OSplus
    p1000.pick_up_tip()
    for i, (well1, well2) in enumerate(zip(plate_96_well_OSminus.wells(), plate_96_well_OSplus.wells())):
        p1000.aspirate(100, plate_6_well.wells_by_name()['C{}'.format(i+1)])
        p1000.dispense(plate_96_well_OSminus.wells_by_name()[well1])
        p1000.dispense(plate_96_well_OSplus.wells_by_name()[well2])
    p1000.drop_tip()

    protocol.comment('Protocol complete')
