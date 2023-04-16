# Importing Required Libraries
from opentrons import protocol_api

# Metadata
metadata = {'apiLevel': '2.0', 'protocolName': 'HM-Spheroid-Protocol'}

# Defining Protocol
def run(protocol: protocol_api.ProtocolContext):
    # Assigning Required Labware
    plate_6_wells = protocol.load_labware('corning_6_wellplate_16.8mL_flat', 1)
    plate_96_wells = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    tip_rack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 4)

    # Assigning Required Pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tip_rack_1000])

    # Assigning Required Reagents
    medium = plate_96_wells['A1']
    dmem = plate_96_wells['A2']
    os_plus = [plate_96_wells['A3'], plate_96_wells['B3']]
    supplements_source = plate_6_wells['A1']
    supplements_os_plus = [plate_6_wells['B1'], plate_6_wells['C1']]

    # Adding Required Medium and Supplements to each well
    for well in plate_96_wells.wells():
        p1000.pick_up_tip()
        if well in os_plus:
            p1000.transfer(100, dmem, well, new_tip='never')
            p1000.aspirate(0.1, supplements_source)
            p1000.dispense(0.1, well)
            for idx, supplement in enumerate([1, 1]):
                p1000.aspirate(supplement, supplements_source)
                p1000.dispense(supplement, supplements_os_plus[idx])
        else:
            p1000.transfer(100, medium, well, new_tip='never')
        p1000.drop_tip()

    # Seeding Cells in each well
    for well in plate_96_wells.wells():
        p1000.pick_up_tip()
        p1000.transfer(100, supplements_source, well, new_tip='never')
        for _ in range(2):
            p1000.mix(3, 250, supplements_source)
            p1000.blow_out(supplements_source)
        p1000.transfer(100, supplements_source, well.top(), new_tip='never')
        p1000.drop_tip()

    protocol.comment('Protocol complete!')
