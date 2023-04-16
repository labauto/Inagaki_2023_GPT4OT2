from opentrons import protocol_api

metadata = {'apiLevel': '2.4'}


def run(protocol: protocol_api.ProtocolContext):
    
    # Labware Setup
    plate_96 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 2)
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    tube_rack_6 = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', 4)
    tube_rack_10 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 5)
    Tube = tube_rack_6['A1']
    
    # Pipette Setup
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_200])

    # Protocol Steps
    p20.pick_up_tip()
    p20.aspirate(30, tube_rack_10['A1'])
    p20.dispense(30, Tube)
    p20.mix(3, 20, Tube)
    p20.blow_out()
    p20.drop_tip()

    p300.pick_up_tip()
    p300.aspirate(50, tube_rack_10['A2'])
    p300.dispense(50, Tube)
    p300.mix(5, 40, Tube)
    p300.blow_out()
    p300.drop_tip()

    p300.pick_up_tip()
    p300.aspirate(200, tube_rack_10['B1'])
    p300.dispense(200, plate_96['A1'])
    p300.drop_tip()


def main():
    protocol = simulate.get_protocol_api('2.4')
    run(protocol)


if __name__ == '__main__':
    main()
